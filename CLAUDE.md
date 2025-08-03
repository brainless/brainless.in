# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Development Workflow
- Create a new branch for each task
- Branch names should start with chore/ or feature/ or fix/
- Please add tests for any new features added, particularly integration tests
- Please run formatters, linters and tests before committing changes
- When finished please commit and push to the new branch
- Please mention GitHub issue if provided
- After working on an issue from GitHub, update issue's tasks and open PR

## Project Structure

This is a personal website and blog built with Astro.js and styled with Tailwind CSS. The repository is organized as follows:

### Main Directories

- **`website/`** - Main Astro.js application containing the website source code
- **`posts/`** - Legacy blog posts in Markdown format (being migrated to `website/src/content/blog/`)
- **`scripts/`** - Python utilities for converting and migrating blog content from various sources
- **`Takeout/`** - Google Takeout data from Blogger exports

### Website Architecture (`website/` directory)

- **Content Collections**: Uses Astro's content collections with two main types:
  - `blog` collection: Blog posts with schema including title, description, pubDate, author, categories, and optional heroImage
  - `comments` collection: Blog comments with parent_id references and metadata
- **Layouts**:
  - `BlogPost.astro` - Blog post layout with custom typography styles
  - `Page.astro` - General page layout
  - `PageWithoutProse.astro` - Layout without prose styling
- **Components**: Modular Astro components for Header, Footer, BaseHead, etc.
- **Styling**: Custom Tailwind CSS configuration with extended colors, fonts (Funnel Sans, Barriecito), and custom shadows

## Development Commands

All development commands should be run from the `website/` directory:

```bash
cd website
```

### Primary Commands
- `pnpm install` - Install dependencies
- `pnpm dev` - Start development server (runs at http://localhost:4321)
- `pnpm build` - Build for production
- `pnpm preview` - Preview production build

### Content Migration (from `scripts/` directory)
- `python convert_blogger_to_markdown.py` - Convert Blogger Atom feeds to Markdown
- `python organize_comments.py` - Organize comment files into separate directory

## Content Management

### Blog Posts
- Located in `website/src/content/blog/`
- Use Markdown (.md) or MDX (.mdx) format
- Required frontmatter: `title`, `pubDate`
- Optional frontmatter: `id`, `description`, `updatedDate`, `author`, `categories`, `heroImage`

### Comments
- Located in `website/src/content/comments/`
- Include `parent_id` to reference the blog post they belong to

## Site Configuration

- **Site URL**: https://brainless.in
- **Integrations**: MDX support, RSS feeds, sitemap generation
- **Build Tool**: Vite with Tailwind CSS plugin
- **Dependencies**: Astro 5.x, Tailwind CSS 4.x, Sharp for image processing

## Key Technical Details

- Uses Astro's new content loader system with glob patterns
- Custom typography styles defined in BlogPost layout
- Dark theme with custom color palette (accent: #2337ff, accent-dark: #000d8a)
- Responsive design with mobile-first approach
- RSS feed generation available at `/rss.xml`
