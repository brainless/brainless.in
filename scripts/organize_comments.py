#!/usr/bin/env python3
"""
Move untitled blog posts (which are actually comments) to a comments folder.
"""

import os
import shutil
from pathlib import Path


def move_comments_to_folder():
    """Move all files starting with 'untitled' to a comments folder."""
    # Define paths
    script_dir = Path(__file__).parent
    project_dir = script_dir.parent
    posts_dir = project_dir / 'posts'
    comments_dir = posts_dir / 'comments'
    
    # Create comments directory if it doesn't exist
    comments_dir.mkdir(exist_ok=True)
    
    # Find all untitled files
    untitled_files = list(posts_dir.glob('untitled*.md'))
    
    print(f"Found {len(untitled_files)} untitled files (comments) to move")
    print(f"Moving to: {comments_dir}")
    
    moved_count = 0
    for file_path in untitled_files:
        try:
            # Move file to comments directory
            new_path = comments_dir / file_path.name
            shutil.move(str(file_path), str(new_path))
            print(f"  Moved: {file_path.name}")
            moved_count += 1
        except Exception as e:
            print(f"  Error moving {file_path.name}: {e}")
    
    print(f"\nMoved {moved_count} files to comments folder")
    
    # Count remaining posts
    remaining_posts = len(list(posts_dir.glob('*.md')))
    print(f"Remaining blog posts: {remaining_posts}")


if __name__ == "__main__":
    move_comments_to_folder()
