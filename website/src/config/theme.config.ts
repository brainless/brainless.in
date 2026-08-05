const siteUrl = (
  import.meta.env.SITE_URL ||
  import.meta.env.PUBLIC_SITE_URL ||
  "https://brainless.in"
).replace(/\/$/, "");

export const SITE = {
  name: "brainless.in",
  description:
    "Sumit Datta's personal blog: software engineering, startups, and the occasional life update.",
  url: siteUrl,
  locale: "en-US",
  language: "en",
  repositoryUrl: "https://github.com/brainless/brainless.in",
};

export const NAVIGATION = [
  { to: "/", label: "Home" },
  { to: "/blog", label: "Blog" },
  { to: "/projects", label: "Projects" },
  { to: "/videos", label: "Videos" },
  { to: "/about", label: "About" },
];

export const CONTACT = {
  email: "sumitdatta@gmail.com",
  socialHandle: "@brainless",
  socialUrl: "https://twitter.com/brainless",
};

export const FORMS = {
  contact: {
    action: "",
    method: "post",
    enctype: "application/x-www-form-urlencoded",
  },
  newsletter: {
    action: "",
    method: "post",
    enctype: "application/x-www-form-urlencoded",
  },
};

export const SOCIAL_LINKS = [
  { href: "/rss.xml", label: "RSS feed", icon: "rss" },
  { href: CONTACT.socialUrl, label: `${SITE.name} on X`, icon: "twitter" },
  { href: SITE.repositoryUrl, label: `${SITE.name} on GitHub`, icon: "github" },
  { href: `mailto:${CONTACT.email}`, label: "Email", icon: "mail" },
];

export const authors = [
  {
    slug: "sumit-datta",
    name: "Sumit Datta",
    bio: "Software engineer and entrepreneur, 16+ years at fast-paced startups across the US, Canada, Germany and India.",
    longBio:
      "I am an extremely passionate software engineer with 16 years of experience, mostly at fast-paced startups. I am entrepreneurial by nature, have built and failed at a few startups, and I am very hands-on when it comes to software/product development. I blog about mental issues, personal journey, software and product development.",
    avatar: "/avatars/sumit-datta.jpg",
  },
];

export const categories = [
  { slug: "tech-engineering", name: "Tech & Engineering" },
  { slug: "startups-business", name: "Startups & Business" },
  { slug: "community-events", name: "Community & Events" },
  { slug: "web-digital-culture", name: "Web & Digital Culture" },
  { slug: "personal-reflections", name: "Personal & Reflections" },
];

export const tags = [];
