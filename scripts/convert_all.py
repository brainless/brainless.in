#!/usr/bin/env python3
"""
Complete blog conversion process - converts Blogger feed to Markdown and organizes comments.
"""

import subprocess
import sys
from pathlib import Path


def run_script(script_name):
    """Run a Python script and return its exit code."""
    try:
        result = subprocess.run([sys.executable, script_name], 
                              capture_output=True, text=True)
        print(result.stdout)
        if result.stderr:
            print(f"Warnings/Errors from {script_name}:")
            print(result.stderr)
        return result.returncode
    except Exception as e:
        print(f"Error running {script_name}: {e}")
        return 1


def main():
    """Run the complete blog conversion process."""
    print("=== Blog Conversion Process ===\n")
    
    # Step 1: Convert Blogger feed to Markdown
    print("Step 1: Converting Blogger feed to Markdown files...")
    exit_code = run_script("convert_blogger_to_markdown.py")
    if exit_code != 0:
        print("Error in conversion step. Exiting.")
        return 1
    
    print("\n" + "="*50 + "\n")
    
    # Step 2: Organize comments
    print("Step 2: Moving comments to separate folder...")
    exit_code = run_script("organize_comments.py")
    if exit_code != 0:
        print("Error in organization step. Exiting.")
        return 1
    
    print("\n" + "="*50 + "\n")
    print("✅ Blog conversion complete!")
    print("📁 Blog posts are in: ../posts/")
    print("💬 Comments are in: ../posts/comments/")


if __name__ == "__main__":
    main()
