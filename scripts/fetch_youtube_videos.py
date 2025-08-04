#!/usr/bin/env python3
"""
Script to fetch videos from a YouTube playlist using YouTube API
and save details to a JSON file for the website.

This script fetches video details from a specified YouTube playlist,
including title, description, link, upload date, and thumbnail URL.
The playlist ID and API key should be configured in a .env file.

To run the script:
  pip install -r requirements.txt
  python fetch_youtube_videos.py
"""

import os
import json
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from dotenv import load_dotenv

# --- Configuration ---
OUTPUT_FILE = "website/src/data/videos.json"
MAX_RESULTS = 50
# ---------------------

def get_api_credentials():
    """Load and validate API credentials from environment variables."""
    load_dotenv()
    
    api_key = os.getenv('YOUTUBE_API_KEY')
    playlist_id = os.getenv('YOUTUBE_PLAYLIST_ID')
    
    if not api_key:
        raise ValueError("YOUTUBE_API_KEY environment variable not set.")
    if not playlist_id:
        raise ValueError("YOUTUBE_PLAYLIST_ID environment variable not set.")
    
    return api_key, playlist_id

def fetch_playlist_videos(api_key, playlist_id, max_results=50):
    """Fetch videos from a YouTube playlist."""
    try:
        youtube = build('youtube', 'v3', developerKey=api_key)
        
        print(f"Fetching videos from playlist: {playlist_id}")
        
        request = youtube.playlistItems().list(
            part='snippet',
            playlistId=playlist_id,
            maxResults=max_results
        )
        
        response = request.execute()
        return response['items']
        
    except HttpError as e:
        print(f"An HTTP error occurred: {e}")
        raise
    except Exception as e:
        print(f"An error occurred while fetching videos: {e}")
        raise

def process_video_data(items):
    """Process raw video data into structured format."""
    videos = []
    
    for item in items:
        try:
            video = {
                'title': item['snippet']['title'],
                'description': item['snippet']['description'],
                'link': f"https://www.youtube.com/watch?v={item['snippet']['resourceId']['videoId']}",
                'thumbnail': item['snippet']['thumbnails']['high']['url'] if 'high' in item['snippet']['thumbnails'] else item['snippet']['thumbnails']['default']['url'],
                'publishDate': item['snippet']['publishedAt'],
                'videoId': item['snippet']['resourceId']['videoId']
            }
            videos.append(video)
            print(f"  - Processed: {video['title']}")
        except KeyError as e:
            print(f"Warning: Missing key {e} in video data, skipping video")
            continue
    
    # Sort videos by upload date (most recent first)
    videos.sort(key=lambda x: x['publishDate'], reverse=True)
    return videos

def save_videos_data(videos, output_file):
    """Save video data to JSON file."""
    try:
        # Ensure the output directory exists
        output_dir = os.path.dirname(output_file)
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(videos, f, indent=2, ensure_ascii=False)
        
        print(f"Successfully saved {len(videos)} videos to {output_file}")
        
    except Exception as e:
        print(f"Error saving videos data: {e}")
        raise

def main():
    """Main function to fetch and process YouTube playlist videos."""
    try:
        print("=== YouTube Playlist Video Fetcher ===")
        
        # Get API credentials
        api_key, playlist_id = get_api_credentials()
        
        # Fetch videos from playlist
        video_items = fetch_playlist_videos(api_key, playlist_id, MAX_RESULTS)
        
        if not video_items:
            print("No videos found in the playlist.")
            return
        
        # Process video data
        print(f"\nProcessing {len(video_items)} videos...")
        videos = process_video_data(video_items)
        
        # Save to JSON file
        save_videos_data(videos, OUTPUT_FILE)
        
        print(f"\n✅ Successfully fetched and saved {len(videos)} videos!")
        
    except Exception as e:
        print(f"❌ An error occurred: {e}")
        return 1
    
    return 0

if __name__ == "__main__":
    exit(main())
