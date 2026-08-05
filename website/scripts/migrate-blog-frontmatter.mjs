// One-time migration: rewrites legacy Blogger-era frontmatter in
// src/content/blog/*.md to match the QuietPages-derived content schema.
// Run once with: node scripts/migrate-blog-frontmatter.mjs
import { readdirSync, readFileSync, writeFileSync } from "node:fs";
import { fileURLToPath } from "node:url";
import { dirname, join } from "node:path";

const __dirname = dirname(fileURLToPath(import.meta.url));
const blogDir = join(__dirname, "..", "src", "content", "blog");

const CATEGORY_KEYWORDS = {
  "community-events": [
    "kolkata",
    "occ",
    "meetup",
    "hackathon",
    "events",
    "adda",
    "bloggers",
  ],
  "startups-business": [
    "startup",
    "entrepreneurship",
    "founder",
    "business",
    "business plan",
    "growth",
    "job",
    "developer",
    "products",
    "product",
    "hiring",
    "mag",
    "engineer",
  ],
  "web-digital-culture": [
    "google",
    "facebook",
    "search",
    "safe browsing",
    "dth",
    "airtel",
    "page tabs",
    "social web",
    "review",
    "hd",
    "mobile",
    "technology",
    "doodle",
  ],
  "personal-reflections": [
    "mental health",
    "life",
    "non-tech",
    "movie",
    "travel",
    "fail",
    "journey",
    "personal",
    "relations",
    "terrorist",
    "writing",
  ],
};

const DEFAULT_CATEGORY = "tech-engineering";

const classify = (categories, title) => {
  const haystack = `${categories.join(" ")} ${title}`.toLowerCase();
  let best = null;
  let bestScore = 0;
  for (const [category, keywords] of Object.entries(CATEGORY_KEYWORDS)) {
    const score = keywords.filter((keyword) => haystack.includes(keyword)).length;
    if (score > bestScore) {
      bestScore = score;
      best = category;
    }
  }
  return best ?? DEFAULT_CATEGORY;
};

const parseCategories = (block) => {
  const match = block.match(/^categories:\s*\[(.*)\]\s*$/m);
  if (!match) return [];
  return match[1]
    .split(",")
    .map((s) => s.trim().replace(/^'|'$/g, ""))
    .filter(Boolean);
};

const files = readdirSync(blogDir).filter((f) => f.endsWith(".md"));
let migrated = 0;

for (const file of files) {
  const path = join(blogDir, file);
  const raw = readFileSync(path, "utf8");
  const frontmatterMatch = raw.match(/^---\n([\s\S]*?)\n---\n?([\s\S]*)$/);
  if (!frontmatterMatch) {
    console.warn(`Skipping ${file}: no frontmatter block found`);
    continue;
  }
  const [, frontmatter, body] = frontmatterMatch;

  if (/^date:/m.test(frontmatter)) {
    // Already migrated.
    continue;
  }

  const titleMatch = frontmatter.match(/^title:\s*"(.*)"\s*$/m);
  const title = titleMatch ? titleMatch[1] : file.replace(/\.md$/, "");
  const categories = parseCategories(frontmatter);
  const category = classify(categories, title);

  let next = frontmatter
    .replace(/^pubDate:/m, "date:")
    .replace(/^categories:\s*\[(.*)\]\s*$/m, (_, list) => `tags: [${list}]`);

  if (!/^author:/m.test(next)) {
    next += `\nauthor: "sumit-datta"`;
  } else {
    next = next.replace(/^author:\s*Sumit Datta\s*$/m, 'author: "sumit-datta"');
  }

  if (!/^tags:/m.test(next)) {
    next += `\ntags: []`;
  }

  next += `\ncategory: "${category}"`;

  writeFileSync(path, `---\n${next}\n---\n${body}`, "utf8");
  migrated += 1;
}

console.log(`Migrated ${migrated} of ${files.length} post(s).`);
