import { SITE, authors, categories, sortedPosts, tags } from "../lib/blog-data.js";

const BASE_URL = SITE.url || "";

export async function GET() {
  const posts = await sortedPosts();
  const entries = [
    { path: "/", changefreq: "weekly", priority: "1.0" },
    { path: "/blog", changefreq: "daily", priority: "0.9" },
    { path: "/about", changefreq: "monthly", priority: "0.6" },
    { path: "/contact", changefreq: "monthly", priority: "0.5" },
    ...posts.map((post) => ({
      path: `/blog/${post.slug}`,
      lastmod: post.updated || post.date,
      changefreq: "monthly",
      priority: "0.8",
    })),
    ...categories.map((category) => ({
      path: `/categories/${category.slug}`,
      changefreq: "weekly",
      priority: "0.6",
    })),
    ...tags.map((tag) => ({
      path: `/tags/${tag.slug}`,
      changefreq: "weekly",
      priority: "0.4",
    })),
    ...authors.map((author) => ({
      path: `/authors/${author.slug}`,
      changefreq: "monthly",
      priority: "0.5",
    })),
  ];

  const urls = entries.map((entry) =>
    [
      "  <url>",
      `    <loc>${BASE_URL}${entry.path}</loc>`,
      entry.lastmod ? `    <lastmod>${entry.lastmod}</lastmod>` : null,
      entry.changefreq ? `    <changefreq>${entry.changefreq}</changefreq>` : null,
      entry.priority ? `    <priority>${entry.priority}</priority>` : null,
      "  </url>",
    ]
      .filter(Boolean)
      .join("\n"),
  );

  const xml = [
    '<?xml version="1.0" encoding="UTF-8"?>',
    '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">',
    ...urls,
    "</urlset>",
  ].join("\n");

  return new Response(xml, {
    headers: {
      "Content-Type": "application/xml",
      "Cache-Control": "public, max-age=3600",
    },
  });
}
