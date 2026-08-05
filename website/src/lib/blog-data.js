import { getCollection } from "astro:content";
export { SITE, authors, categories, tags } from "../config/theme.config.ts";
import { authors, categories, tags } from "../config/theme.config.ts";
import placeholderThumbnail from "../assets/placeholder-thumbnail.png";

const isoDate = (date) => date?.toISOString().slice(0, 10);
const wordsPerMinute = 220;

const estimateReadingTime = (text = "") => {
  const words = text
    .replace(/```[\s\S]*?```/g, " ")
    .replace(/<[^>]+>/g, " ")
    .trim()
    .split(/\s+/)
    .filter(Boolean).length;

  return Math.max(1, Math.ceil(words / wordsPerMinute));
};

// Old, pre-2026 posts predate excerpts/summaries. Fall back to the legacy
// `description` field, then a plain-text snippet of the post body.
const excerptFrom = (data, body = "", length = 160) => {
  if (data.excerpt) return data.excerpt;
  if (data.description) return data.description;
  const plain = body
    .replace(/```[\s\S]*?```/g, " ")
    .replace(/!\[[^\]]*\]\([^)]*\)/g, " ")
    .replace(/\[([^\]]*)\]\([^)]*\)/g, "$1")
    .replace(/[#>*_`~-]/g, " ")
    .replace(/\s+/g, " ")
    .trim();
  if (plain.length <= length) return plain;
  return `${plain.slice(0, length).trimEnd()}...`;
};

export const imageSrc = (image) => (typeof image === "string" ? image : image?.src);

export const normalizePost = (entry) => ({
  slug: entry.id,
  ...entry.data,
  excerpt: excerptFrom(entry.data, entry.body),
  thumbnail: entry.data.thumbnail ?? placeholderThumbnail,
  date: isoDate(entry.data.date),
  updated: isoDate(entry.data.updated),
  readingTime: entry.data.readingTime ?? estimateReadingTime(entry.body),
});

export const posts = async () =>
  (await getCollection("blog", ({ data }) => !data.draft)).map(normalizePost);

const titleCase = (slug) =>
  slug.replace(/[-_]/g, " ").replace(/\b\w/g, (c) => c.toUpperCase());

export const getPost = async (slug) => (await posts()).find((post) => post.slug === slug);
export const getAuthor = (slug) => authors.find((author) => author.slug === slug);
export const getCategory = (slug) => categories.find((category) => category.slug === slug);
export const getTag = (slug) => tags.find((tag) => tag.slug === slug) ?? { slug, name: titleCase(slug) };

// The old Blogger-era posts carry hundreds of freeform tags, so tag pages are
// generated from whatever tags actually appear on posts rather than a fixed
// curated list (unlike categories, which are curated in theme.config.ts).
export const allTags = async () => {
  const list = await posts();
  const bySlug = new Map();
  for (const post of list) {
    for (const slug of post.tags) {
      if (!bySlug.has(slug)) bySlug.set(slug, getTag(slug));
    }
  }
  return [...bySlug.values()].sort((a, b) => a.name.localeCompare(b.name));
};
export const postsByCategory = async (slug) =>
  (await sortedPosts()).filter((post) => post.category === slug);
export const postsByTag = async (slug) =>
  (await sortedPosts()).filter((post) => post.tags.includes(slug));
export const postsByAuthor = async (slug) =>
  (await sortedPosts()).filter((post) => post.author === slug);
export const sortedPosts = async () =>
  [...(await posts())].sort((a, b) => (a.date < b.date ? 1 : -1));
export const featuredPost = async () => {
  const sorted = await sortedPosts();
  return sorted.find((post) => post.featured) ?? sorted[0];
};
export const popularPosts = async () => (await sortedPosts()).slice(0, 4);
export const relatedPosts = async (post, n = 3) =>
  (await sortedPosts())
    .filter((candidate) => candidate.slug !== post.slug)
    .sort((a, b) => {
      const score = (candidate) =>
        (candidate.category === post.category ? 2 : 0) +
        candidate.tags.filter((tag) => post.tags.includes(tag)).length;
      return score(b) - score(a);
    })
    .slice(0, n);

export const adjacentPosts = async (post) => {
  const sorted = await sortedPosts();
  const index = sorted.findIndex((candidate) => candidate.slug === post.slug);
  return { prev: sorted[index + 1], next: sorted[index - 1] };
};

export const formatDate = (iso) =>
  new Date(iso).toLocaleDateString("en-US", {
    year: "numeric",
    month: "long",
    day: "numeric",
  });
