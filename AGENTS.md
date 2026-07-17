# AGENTS.md

Instructions for AI coding agents working on the brainless.in personal website and blog.

## Project Overview

A personal website and blog built with [Astro](https://astro.build/) and styled with [Tailwind CSS](https://tailwindcss.com/). Content is authored in Markdown/MDX. The site is deployed at https://brainless.in.

## Development Workflow

- Create a new branch for each task, prefixed with `chore/`, `feature/`, or `fix/`
- Add tests for new features, particularly integration tests
- Run formatters, linters, and tests before committing
- Reference the GitHub issue (if any) in commits and PR descriptions
- After completing an issue, update its tasks and open a PR
- Commit and push to the new branch when finished

## Project Structure

```
.
├── website/          # Main Astro.js application
├── posts/            # Legacy blog posts in Markdown (migrating to website/src/content/blog/)
├── scripts/          # Python utilities for content migration and data fetching
├── Takeout/          # Google Takeout data from Blogger exports (gitignored)
├── AGENTS.md         # This file
├── CLAUDE.md         # Claude-specific instructions
└── GEMINI.md         # Gemini-specific instructions
```

## Development Commands

All website commands run from the `website/` directory:

```bash
cd website
pnpm install        # Install dependencies
pnpm dev            # Dev server at http://localhost:4321
pnpm build          # Production build
pnpm preview        # Preview production build
```

## Website Architecture (`website/`)

- **Framework:** Astro 5.x with Vite
- **Styling:** Tailwind CSS 4.x with custom config (`tailwind.config.cjs`)
- **Content Collections:**
  - `blog` — Blog posts with schema: title, description, pubDate, author, categories, optional heroImage
  - `comments` — Blog comments with `parent_id` referencing their parent post
- **Layouts:** `BlogPost.astro`, `Page.astro`, `PageWithoutProse.astro`
- **Components:** Modular Astro components (Header, Footer, BaseHead, etc.)
- **Integrations:** MDX, RSS (`/rss.xml`), sitemap
- **Fonts:** Funnel Sans, Barriecito
- **Theme:** Dark theme; accent `#2337ff`, accent-dark `#000d8a`
- **Images:** Sharp for processing

## Blog Posts

- Location: `website/src/content/blog/`
- Format: `.md` or `.mdx`
- Required frontmatter: `title`, `pubDate`
- Optional frontmatter: `id`, `description`, `updatedDate`, `author`, `categories`, `heroImage`

## Scripts (`scripts/`)

Python utilities for content migration. Set up a venv and install `requirements.txt` before running.

| Script | Purpose |
|---|---|
| `convert_all.py` | Orchestrates full Blogger-to-Markdown pipeline |
| `convert_blogger_to_markdown.py` | Converts Blogger Atom feed to Astro-compatible Markdown |
| `convert_to_markdown.py` | Simpler legacy converter |
| `fix_dates_and_move.py` | Fixes frontmatter dates and moves posts to Astro content dir |
| `organize_comments.py` | Separates comment files from blog posts |
| `import_projects.py` | Fetches GitHub repos and saves to `website/src/data/projects.json` |
| `fetch_youtube_videos.py` | Fetches YouTube playlist data to `website/src/data/videos.json` |

### Script Environment Variables

Scripts needing API access require a `.env` file (gitignored):

```
GITHUB_TOKEN_BRAINLESS=...
GITHUB_TOKEN_PIXLIE=...
YOUTUBE_API_KEY=...
YOUTUBE_PLAYLIST_ID=...
```

## Key Conventions

- Mobile-first responsive design
- Astro's content loader with glob patterns
- Custom typography styles in `BlogPost` layout
- Never commit secrets or API keys
- `.env` and `Takeout/` are gitignored
