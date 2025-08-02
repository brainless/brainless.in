import { defineCollection, z } from 'astro:content';
import { glob } from 'astro/loaders';

const blog = defineCollection({
	// Load Markdown and MDX files in the `src/content/blog/` directory.
	loader: glob({ base: './src/content/blog', pattern: '**/*.{md,mdx}' }),
	// Type-check frontmatter using a schema
	schema: ({ image }) =>
		z.object({
			id: z.string().optional(),
			title: z.string(),
			description: z.string().optional(),
			// Transform string to Date object
			pubDate: z.coerce.date(),
			updatedDate: z.coerce.date().optional(),
			author: z.string().optional(),
			categories: z.array(z.string()).optional(),
			heroImage: image().optional(),
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
