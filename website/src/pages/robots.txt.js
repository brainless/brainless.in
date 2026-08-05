import { SITE } from "../lib/blog-data.js";

export function GET() {
  return new Response(
    ["User-agent: *", "Allow: /", `Sitemap: ${SITE.url}/sitemap.xml`, ""].join("\n"),
    {
      headers: {
        "Content-Type": "text/plain; charset=utf-8",
        "Cache-Control": "public, max-age=3600",
      },
    },
  );
}
