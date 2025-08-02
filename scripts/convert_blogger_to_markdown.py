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
    
    # Extract published date
    published_elem = entry.find('published')
    if published_elem:
        try:
            published_date = datetime.strptime(
                published_elem.text, '%Y-%m-%dT%H:%M:%SZ'
            ).strftime('%Y-%m-%d')
        except ValueError:
            # Fallback for different date formats
            published_date = datetime.now().strftime('%Y-%m-%d')
    else:
        published_date = datetime.now().strftime('%Y-%m-%d')
    
    # Extract author
    author_elem = entry.find('author')
    author = "brainless"  # Default author
    if author_elem:
        name_elem = author_elem.find('name')
        if name_elem:
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


def create_markdown_file(post_data, output_dir):
    """Create a Markdown file from post data."""
    filename = clean_filename(post_data['title'])
    if not filename:
        filename = f"post-{post_data['date']}"
    
    # Convert content to markdown
    markdown_content = convert_html_to_markdown(post_data['content'])
    
    # Create frontmatter
    frontmatter = f"""---
id: {post_data['id']}
title: "{post_data['title']}"
date: {post_data['date']}
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
    output_dir = project_dir / 'posts'
    
    # Check if feed file exists
    if not feed_file.exists():
        print(f"Error: Feed file not found at {feed_file}")
        return
    
    # Create output directory
    output_dir.mkdir(exist_ok=True)
    
    print(f"Reading Blogger feed from: {feed_file}")
    print(f"Output directory: {output_dir}")
    
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
    converted_count = 0
    for i, entry in enumerate(entries, 1):
        try:
            # Check if this is a blog post (not a page or comment)
            type_elem = entry.find('blogger:type', {'blogger': 'http://schemas.google.com/blogger/2018'})
            if type_elem and type_elem.text != 'POST':
                continue
            
            post_data = extract_post_data(entry)
            output_path = create_markdown_file(post_data, output_dir)
            
            print(f"  {i:3d}. {post_data['title'][:50]}... -> {output_path.name}")
            converted_count += 1
            
        except Exception as e:
            print(f"  Error processing entry {i}: {e}")
            continue
    
    print(f"\nConversion complete! {converted_count} blog posts converted to Markdown.")
    print(f"Files saved in: {output_dir}")


if __name__ == "__main__":
    main()
