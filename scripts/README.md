# Management Scripts

This directory contains various management scripts for blog content conversion, project importing, and content organization.

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

### convert_all.py

**Purpose:** Complete blog conversion orchestrator that runs the full conversion pipeline.

**Usage:**
```bash
python convert_all.py
```

**Features:**
- Orchestrates the complete blog conversion process
- Runs `convert_blogger_to_markdown.py` followed by `organize_comments.py`
- Provides progress feedback and error handling
- Stops execution if any step fails

**Dependencies:** None (uses standard library only)

### convert_blogger_to_markdown.py

**Purpose:** Converts Blogger Atom feed export to individual Markdown files for Astro.

**Usage:**
```bash
python convert_blogger_to_markdown.py
```

**Features:**
- Extracts blog posts and comments from Blogger Atom feed
- Converts HTML content to Markdown using markdownify
- Creates Astro-compatible frontmatter with `pubDate` field
- Separates posts and comments into different directories
- Handles duplicate filenames automatically
- Supports multiple date formats and namespaces
- Creates clean filenames from post titles
- Sets default author to "Sumit Datta" for blog posts

**Input:** `../Takeout/Blogger/Blogs/Being brainless!/feed.atom`
**Output:** 
- Blog posts: `../website/src/content/blog/`
- Comments: `../website/src/content/comments/`

**Dependencies:** `beautifulsoup4`, `markdownify`

### convert_to_markdown.py

**Purpose:** Simple Blogger to Markdown converter (legacy version).

**Usage:**
```bash
python convert_to_markdown.py
```

**Features:**
- Basic conversion from Blogger Atom feed to Markdown
- Simpler implementation than `convert_blogger_to_markdown.py`
- Uses basic date format conversion
- Outputs to `posts/` directory

**Input:** `Takeout/Blogger/Blogs/Being brainless!/feed.atom`
**Output:** Individual `.md` files in `posts/` directory

**Dependencies:** `beautifulsoup4`, `markdownify`

### fix_dates_and_move.py

**Purpose:** Fix frontmatter date fields and move posts to Astro content directory.

**Usage:**
```bash
python fix_dates_and_move.py
```

**Features:**
- Converts `date:` frontmatter to `pubDate:` for Astro compatibility
- Processes all markdown files in `posts/` directory
- Copies fixed files to `website/src/content/blog/`
- Preserves all other frontmatter and content
- Provides detailed processing feedback

**Input:** Markdown files in `../posts/`
**Output:** Fixed files in `../website/src/content/blog/`

**Dependencies:** None (uses standard library only)

### import_projects.py

**Purpose:** Import project information from GitHub repositories and save to JSON.

**Usage:**
```bash
# Set up environment variables first (see Configuration below)
python import_projects.py
```

**Features:**
- Fetches repositories from configurable GitHub owners
- Filters for projects with recent activity (configurable timeframe)
- Extracts project details: name, description, languages, stars
- Gets README summary for each project
- Supports both user and organization accounts
- Handles API rate limiting gracefully
- Outputs structured JSON for website integration

**Configuration:**
- Create `.env` file with GitHub tokens:
  ```
  GITHUB_TOKEN_BRAINLESS=your_personal_token_here
  GITHUB_TOKEN_PIXLIE=your_org_token_here
  ```
- Modify `OWNERS`, `MONTHS_OF_ACTIVITY`, and `MIN_COMMITS` in script as needed

**Output:** `../website/src/data/projects.json`

**Dependencies:** `PyGithub`, `python-dotenv`

### fetch_youtube_videos.py

**Purpose:** Fetch videos from a YouTube playlist using YouTube API and save details to JSON for website display.

**Usage:**
```bash
# Set up environment variables first (see Configuration below)
python fetch_youtube_videos.py
```

**Features:**
- Fetches video details from a specified YouTube playlist
- Extracts title, description, YouTube link, thumbnail URL, and publish date
- Handles API errors gracefully with detailed error messages
- Sorts videos by upload date (most recent first)
- Saves structured JSON data for website integration
- Supports configurable maximum number of videos to fetch
- Provides detailed progress feedback during execution

**Configuration:**
- Create `.env` file with YouTube API credentials:
  ```
  YOUTUBE_API_KEY=your_youtube_api_key_here
  YOUTUBE_PLAYLIST_ID=your_playlist_id_here
  ```
- Modify `MAX_RESULTS` in script if you need more than 50 videos

**Output:** `../website/src/data/videos.json`

**Dependencies:** `google-api-python-client`, `python-dotenv`

### organize_comments.py

**Purpose:** Move comment files (identified as "untitled" posts) to a separate comments folder.

**Usage:**
```bash
python organize_comments.py
```

**Features:**
- Identifies files starting with "untitled" (which are comments from the blog)
- Moves them to `../posts/comments/` directory
- Leaves actual blog posts in the main `../posts/` directory
- Provides summary of moved files and remaining posts
- Creates comments directory if it doesn't exist

**Input:** Files in `../posts/`
**Output:** Organized files with comments in `../posts/comments/`

**Dependencies:** None (uses standard library only)

## Typical Workflow

### Blog Conversion (Complete Process)
```bash
# Run the complete conversion pipeline
python convert_all.py
```

### Blog Conversion (Step by Step)
```bash
# Step 1: Convert Blogger feed to Markdown
python convert_blogger_to_markdown.py

# Step 2: Organize comments (if using legacy conversion)
python organize_comments.py

# Step 3: Fix dates and move to Astro (if needed)
python fix_dates_and_move.py
```

### Project Import
```bash
# Set up GitHub tokens in .env file first
python import_projects.py
```

## Output Formats

### Blog Post Frontmatter (Astro-compatible)
```markdown
---
id: post.2006.123456789
title: "Post Title"
pubDate: 2006-05-01
author: Sumit Datta
categories: ["category1", "category2"]
---

# Post content in Markdown format

Content goes here...
```

### Comment Frontmatter
```markdown
---
id: comment.2006.987654321
title: "Comment on: Post Title"
pubDate: 2006-05-02
author: Anonymous
parent_id: post.2006.123456789
---

Comment content...
```

### Projects JSON Structure
```json
[
  {
    "name": "project-name",
    "description": "Project description",
    "url": "https://github.com/owner/project-name",
    "stars": 42,
    "languages": {"JavaScript": 12345, "Python": 6789},
    "summary": "First line from README",
    "last_updated": "2023-12-01T10:30:00Z"
  }
]
```

### Videos JSON Structure
```json
[
  {
    "title": "Video Title",
    "description": "Video description from YouTube",
    "link": "https://www.youtube.com/watch?v=VIDEO_ID",
    "thumbnail": "https://i.ytimg.com/vi/VIDEO_ID/hqdefault.jpg",
    "publishDate": "2023-12-01T10:30:00Z",
    "videoId": "VIDEO_ID"
  }
]
```
