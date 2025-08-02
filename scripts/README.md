# Blog Conversion Scripts

This directory contains scripts to convert blog posts from various formats to Markdown.

## Setup

1. Create and activate the virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Linux/Mac
   # or
   venv\Scripts\activate     # On Windows
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Scripts

### convert_blogger_to_markdown.py

Converts a Blogger Atom feed export to individual Markdown files.

**Usage:**
```bash
python convert_blogger_to_markdown.py
```

**Features:**
- Extracts blog posts from Blogger Atom feed
- Converts HTML content to Markdown
- Creates proper frontmatter with title, date, author, and categories
- Handles duplicate filenames automatically
- Filters out non-POST entries (pages, comments, etc.)
- Creates clean filenames from post titles

**Input:** `../Takeout/Blogger/Blogs/Being brainless!/feed.atom`
**Output:** Individual `.md` files in `../posts/` directory

### organize_comments.py

Moves untitled blog posts (which are actually comments) to a separate comments folder.

**Usage:**
```bash
python organize_comments.py
```

**Features:**
- Identifies files starting with "untitled" (which are comments from the blog)
- Moves them to `../posts/comments/` directory
- Leaves actual blog posts in the main `../posts/` directory
- Provides summary of moved files

## Output Format

Each converted post will have the following structure:

```markdown
---
title: "Post Title"
date: 2006-05-01
author: brainless
categories: ["category1", "category2"]
---

# Post content in Markdown format

Content goes here...
```
