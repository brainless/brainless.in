import { SITE, getAuthor, sortedPosts } from "../lib/blog-data.js";

const BASE_URL = SITE.url || "";

const esc = (value) =>
  value.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;").replace(/"/g, "&quot;");

export async function GET() {
  const items = (await sortedPosts()).map((post) => {
    const link = `${BASE_URL}/blog/${post.slug}`;
    const author = getAuthor(post.author);
    return [
      "    <item>",
      `      <title>${esc(post.title)}</title>`,
      `      <link>${link}</link>`,
      `      <guid isPermaLink="true">${link}</guid>`,
      `      <pubDate>${new Date(post.date).toUTCString()}</pubDate>`,
      author ? `      <dc:creator>${esc(author.name)}</dc:creator>` : "",
      `      <description>${esc(post.excerpt)}</description>`,
      "    </item>",
    ]
      .filter(Boolean)
      .join("\n");
  });

  const xml = [
    '<?xml version="1.0" encoding="UTF-8"?>',
    '<rss version="2.0" xmlns:dc="http://purl.org/dc/elements/1.1/">',
    "  <channel>",
    `    <title>${esc(SITE.name)}</title>`,
    `    <link>${BASE_URL}/</link>`,
    `    <description>${esc(SITE.description)}</description>`,
    "    <language>en-us</language>",
    ...items,
    "  </channel>",
    "</rss>",
  ].join("\n");

  return new Response(xml, {
    headers: {
      "Content-Type": "application/rss+xml; charset=utf-8",
      "Cache-Control": "public, max-age=3600",
    },
  });
}
