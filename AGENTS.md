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
npm install        # Install dependencies
npm run dev        # Dev server at http://localhost:4321
npm run build      # Production build
npm run preview    # Preview production build
```

## Website Architecture (`website/`)

- **Framework:** Astro 7.x with Vite
- **Theme:** Based on [QuietPages](https://github.com/andreialba/quietpages), adapted for a
  single-author personal blog
- **Styling:** Tailwind CSS 4.x, CSS-first config in `src/styles.css` (no `tailwind.config.cjs`)
- **Content Collections:**
  - `blog` — flat `slug.md` files, or `slug/index.mdx` + local images. Schema: title, date,
    optional excerpt/category/tags/author/thumbnail (see `content.config.ts`); missing fields
    fall back to sensible defaults in `src/lib/blog-data.js` since most older posts predate them
  - `comments` — legacy Blogger comments with `parent_id` referencing their parent post; not
    currently rendered anywhere
- **Layout:** `BaseLayout.astro` (shared page shell)
- **Components:** Modular Astro components (Header, Footer, PostCard, Sidebar, etc.)
- **Config:** `src/config/theme.config.ts` — site name/nav/contact, curated categories, author(s)
- **Integrations:** MDX; RSS/sitemap/robots.txt are hand-rolled in `src/pages/` (no
  `@astrojs/rss`/`@astrojs/sitemap`)
- **Fonts:** Inter (sans), Fraunces (serif), JetBrains Mono (code) — self-hosted
- **Theme:** Light/dark with system preference + manual toggle
- **Images:** Sharp for processing; posts without a real photo fall back to a placeholder image

## Blog Posts

- Location: `website/src/content/blog/`
- Format: `.md` (flat file) or `.mdx` inside a `slug/index.mdx` folder (for posts with local
  images, alongside the image files)
- Required frontmatter: `title`, `date`
- Optional frontmatter: `excerpt`, `category` (must match a slug in `theme.config.ts`), `tags`
  (freeform), `author`, `thumbnail`, `thumbnailAlt`, `featured`, `draft`, `updated`,
  `seoTitle`, `seoDescription`, `canonical`, `imageCredit`

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
