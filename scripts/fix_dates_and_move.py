#!/usr/bin/env python3
"""
Fix date handling and move posts to Astro content directory.

This script:
1. Reads all markdown files from the posts/ directory
2. Converts 'date:' frontmatter to 'pubDate:' for Astro compatibility
3. Copies the fixed files to website/src/content/blog/
"""

import os
import re
from pathlib import Path
import shutil

def fix_frontmatter_date(content):
    """Convert 'date:' to 'pubDate:' in frontmatter."""
    # Pattern to match 'date:' in frontmatter
    pattern = r'^date:\s*(.+)$'
    replacement = r'pubDate: \1'
    
    # Replace only in frontmatter (between --- markers)
    lines = content.split('\n')
    in_frontmatter = False
    fixed_lines = []
    
    for line in lines:
        if line.strip() == '---':
            if not in_frontmatter:
                in_frontmatter = True
            else:
                in_frontmatter = False
            fixed_lines.append(line)
        elif in_frontmatter and line.startswith('date:'):
            # Replace 'date:' with 'pubDate:'
            fixed_line = re.sub(r'^date:', 'pubDate:', line)
            fixed_lines.append(fixed_line)
        else:
            fixed_lines.append(line)
    
    return '\n'.join(fixed_lines)

def main():
    """Main function to fix dates and move posts."""
    # Define paths
    script_dir = Path(__file__).parent
    project_dir = script_dir.parent
    posts_dir = project_dir / 'posts'
    blog_output_dir = project_dir / 'website' / 'src' / 'content' / 'blog'
    
    # Create output directory
    blog_output_dir.mkdir(parents=True, exist_ok=True)
    
    print(f"Reading posts from: {posts_dir}")
    print(f"Output directory: {blog_output_dir}")
    
    # Process all markdown files in posts directory
    processed_count = 0
    error_count = 0
    
    for md_file in posts_dir.glob('*.md'):
        try:
            # Read the original file
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Fix the frontmatter
            fixed_content = fix_frontmatter_date(content)
            
            # Write to the blog directory
            output_file = blog_output_dir / md_file.name
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(fixed_content)
            
            print(f"  ✓ {md_file.name}")
            processed_count += 1
            
        except Exception as e:
            print(f"  ✗ Error processing {md_file.name}: {e}")
            error_count += 1
    
    print(f"\nProcessing complete!")
    print(f"  {processed_count} files processed successfully")
    print(f"  {error_count} files had errors")
    print(f"  Files copied to: {blog_output_dir}")

if __name__ == "__main__":
    main()