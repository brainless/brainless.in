#!/usr/bin/env python3
"""
Convert Blogger Atom feed to Markdown files.

This script reads the Blogger export feed.atom file and converts each blog post
to a separate Markdown file with proper frontmatter.
"""

import os
import re
import html
from pathlib import Path
from datetime import datetime
from bs4 import BeautifulSoup
from markdownify import markdownify as md


def clean_filename(title):
    """Convert title to a clean filename."""
    # Remove HTML entities and convert to lowercase
    clean_title = html.unescape(title).lower()
    # Replace non-alphanumeric characters with hyphens
    clean_title = re.sub(r'[^\w\s-]', '', clean_title)
    # Replace spaces and multiple hyphens with single hyphen
    clean_title = re.sub(r'[-\s]+', '-', clean_title)
    # Remove leading/trailing hyphens
    return clean_title.strip('-')


def convert_html_to_markdown(html_content):
    """Convert HTML content to Markdown with proper formatting."""
    if not html_content:
        return ""
    
    # Convert HTML entities
    content = html.unescape(html_content)
    
    # Convert to markdown
    markdown_content = md(content, heading_style="ATX")
    
    # Clean up extra whitespace
    markdown_content = re.sub(r'\n\s*\n\s*\n', '\n\n', markdown_content)
    
    return markdown_content.strip()


def extract_post_data(entry):
    """Extract relevant data from a blog entry."""
    # Extract post ID
    id_elem = entry.find('id')
    post_id = id_elem.text if id_elem else None
    
    # Extract title
    title_elem = entry.find('title')
    title = title_elem.text if title_elem else "Untitled"
    
    # Extract content
    content_elem = entry.find('content')
    content = content_elem.text if content_elem else ""
    
    # Extract published date - try multiple date fields and formats
    published_date = None
    
    # List of date fields to try, in order of preference
    date_fields = ['published', 'updated', 'blogger:created']
    
    # List of date formats to try
    date_formats = [
        '%Y-%m-%dT%H:%M:%SZ',      # 2006-05-01T18:42:00Z
        '%Y-%m-%dT%H:%M:%S.%fZ',   # 2007-02-18T07:33:54.634Z
        '%Y-%m-%dT%H:%M:%S%z',     # with timezone
        '%Y-%m-%d %H:%M:%S',       # simple format
        '%Y-%m-%d'                 # date only
    ]
    
    for field_name in date_fields:
        # Handle blogger namespace fields differently
        if field_name.startswith('blogger:'):
            date_elem = entry.find(field_name, {'blogger': 'http://schemas.google.com/blogger/2018'})
        else:
            # Standard Atom fields don't need namespace
            date_elem = entry.find(field_name)
        
        if date_elem and date_elem.text:
            date_text = date_elem.text.strip()
            for date_format in date_formats:
                try:
                    published_date = datetime.strptime(date_text, date_format).strftime('%Y-%m-%d')
                    break
                except ValueError:
                    continue
            if published_date:
                break
    
    # If no valid date found, skip this entry or use a warning
    if not published_date:
        print(f"    WARNING: No valid date found for entry: {title_elem.text if title_elem else 'Unknown'}")
        return None
    
    # Extract author
    author_elem = entry.find('author')
    author = "Anonymous"  # Default author for comments
    if author_elem:
        name_elem = author_elem.find('name')
        if name_elem and name_elem.text:
            author = name_elem.text
    
    # Extract parent post ID for comments
    parent_id_elem = entry.find('blogger:parent')
    parent_id = parent_id_elem.text if parent_id_elem else None

    # Extract categories/tags
    categories = []
    for category in entry.find_all('category'):
        if category.get('term'):
            categories.append(category.get('term'))
    
    return {
        'id': post_id,
        'title': title,
        'content': content,
        'date': published_date,
        'author': author,
        'categories': categories,
        'parent_id': parent_id
    }


def create_markdown_file(post_data, output_dir, is_comment=False):
    """Create a Markdown file from post data."""
    filename = clean_filename(post_data['title'])
    if not filename:
        if is_comment:
            filename = f"comment-{post_data['date']}"
        else:
            filename = f"post-{post_data['date']}"
    
    # Convert content to markdown
    markdown_content = convert_html_to_markdown(post_data['content'])
    
    # Create frontmatter - use pubDate for Astro compatibility
    frontmatter = f"""---
id: {post_data['id']}
title: "{post_data['title']}"
pubDate: {post_data['date']}
author: {post_data['author']}"""
    
    if post_data['categories']:
        frontmatter += f"\ncategories: {post_data['categories']}"
    
    if post_data['parent_id']:
        frontmatter += f"\nparent_id: {post_data['parent_id']}"

    frontmatter += "\n---\n\n"

    # Combine frontmatter and content
    full_content = frontmatter + markdown_content
    
    # Write to file
    output_path = output_dir / f"{filename}.md"
    
    # Handle duplicate filenames
    counter = 1
    while output_path.exists():
        new_filename = f"{filename}-{counter}"
        output_path = output_dir / f"{new_filename}.md"
        counter += 1
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(full_content)
    
    return output_path


def main():
    """Main conversion function."""
    # Define paths
    script_dir = Path(__file__).parent
    project_dir = script_dir.parent
    feed_file = project_dir / 'Takeout' / 'Blogger' / 'Blogs' / 'Being brainless!' / 'feed.atom'
    
    # Define Astro output directories
    blog_output_dir = project_dir / 'website' / 'src' / 'content' / 'blog'
    comments_output_dir = project_dir / 'website' / 'src' / 'content' / 'comments'
    
    # Check if feed file exists
    if not feed_file.exists():
        print(f"Error: Feed file not found at {feed_file}")
        return
    
    # Create output directories
    blog_output_dir.mkdir(parents=True, exist_ok=True)
    comments_output_dir.mkdir(parents=True, exist_ok=True)
    
    print(f"Reading Blogger feed from: {feed_file}")
    print(f"Blog posts output directory: {blog_output_dir}")
    print(f"Comments output directory: {comments_output_dir}")
    
    # Read and parse the Atom feed
    try:
        with open(feed_file, 'r', encoding='utf-8') as f:
            feed_content = f.read()
    except Exception as e:
        print(f"Error reading feed file: {e}")
        return
    
    # Parse XML
    try:
        soup = BeautifulSoup(feed_content, 'xml')
    except Exception as e:
        print(f"Error parsing XML: {e}")
        return
    
    # Find all blog entries
    entries = soup.find_all('entry')
    print(f"Found {len(entries)} blog entries")
    
    # Convert each entry
    posts_converted = 0
    comments_converted = 0
    
    for i, entry in enumerate(entries, 1):
        try:
            # Check entry type
            type_elem = entry.find('blogger:type', {'blogger': 'http://schemas.google.com/blogger/2018'})
            if type_elem and type_elem.text not in ['POST', 'COMMENT']:
                continue
            
            post_data = extract_post_data(entry)
            
            # Skip entry if no valid date was found
            if post_data is None:
                continue
            
            # Determine if this is a comment (has parent_id) or a post
            if post_data['parent_id']:
                # This is a comment
                output_path = create_markdown_file(post_data, comments_output_dir, is_comment=True)
                print(f"  {i:3d}. [COMMENT] {post_data['title'][:40]}... -> {output_path.name}")
                comments_converted += 1
            else:
                # This is a blog post - set default author to Sumit Datta
                if post_data['author'] == "Anonymous" or not post_data['author'] or post_data['author'] == "brainless":
                    post_data['author'] = "Sumit Datta"
                output_path = create_markdown_file(post_data, blog_output_dir, is_comment=False)
                print(f"  {i:3d}. [POST] {post_data['title'][:40]}... -> {output_path.name}")
                posts_converted += 1
            
        except Exception as e:
            print(f"  Error processing entry {i}: {e}")
            continue
    
    print(f"\nConversion complete!")
    print(f"  {posts_converted} blog posts converted to: {blog_output_dir}")
    print(f"  {comments_converted} comments converted to: {comments_output_dir}")


if __name__ == "__main__":
    main()
