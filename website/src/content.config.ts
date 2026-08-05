import { defineCollection, z } from 'astro:content';
import { glob } from 'astro/loaders';

const blog = defineCollection({
	// Load flat `slug.md` posts and, for posts with local images, `slug/index.mdx` folders.
	loader: glob({
		base: './src/content/blog',
		pattern: ['**/*.md', '**/*.mdx', '**/index.mdx'],
		generateId: ({ entry }) =>
			entry
				.replace(/[\\/]index\.mdx$/, '')
				.replace(/\.mdx?$/, '')
				.replace(/\\/g, '/'),
	}),
	// Type-check frontmatter using a schema. Most fields are optional with fallbacks
	// applied in src/lib/blog-data.js, since older posts predate this schema.
	schema: ({ image }) =>
		z.object({
			title: z.string(),
			excerpt: z.string().optional(),
			description: z.string().optional(),
			seoTitle: z.string().optional(),
			seoDescription: z.string().optional(),
			canonical: z.string().url().optional(),
			date: z.coerce.date(),
			updated: z.coerce.date().optional(),
			readingTime: z.number().int().positive().optional(),
			category: z.string().optional(),
			tags: z.array(z.string()).default([]),
			author: z.string().default('sumit-datta'),
			thumbnail: image().optional(),
			thumbnailAlt: z.string().default(''),
			imageCredit: z
				.object({
					caption: z.string().optional(),
					author: z.string(),
					authorUrl: z.string().url(),
					source: z.string().default('Unsplash'),
					sourceUrl: z.string().url(),
				})
				.optional(),
			featured: z.boolean().default(false),
			draft: z.boolean().default(false),
		}),
});

const comments = defineCollection({
	// Load Markdown files in the `src/content/comments/` directory.
	loader: glob({ base: './src/content/comments', pattern: '**/*.md' }),
	// Type-check frontmatter using a schema
	schema: z.object({
		id: z.string(),
		title: z.string(),
		pubDate: z.coerce.date(),
		author: z.string(),
		parent_id: z.string(),
		categories: z.array(z.string()).optional(),
	}),
});

export const collections = { blog, comments };
