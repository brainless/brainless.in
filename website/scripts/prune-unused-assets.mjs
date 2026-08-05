import { existsSync, readdirSync, readFileSync, rmSync, statSync } from "node:fs";
import { join } from "node:path";

const distDir = "dist";
const astroAssetsDir = join(distDir, "_astro");
const referenceExtensions = new Set([
  ".css",
  ".html",
  ".js",
  ".json",
  ".svg",
  ".txt",
  ".webmanifest",
  ".xml",
]);
const removableExtensions = new Set([".jpg", ".jpeg", ".png"]);

const extensionOf = (file) => {
  const match = file.match(/\.[^.]+$/);
  return match ? match[0].toLowerCase() : "";
};

const walk = (dir) =>
  readdirSync(dir, { withFileTypes: true }).flatMap((entry) => {
    const path = join(dir, entry.name);
    return entry.isDirectory() ? walk(path) : [path];
  });

if (existsSync(astroAssetsDir)) {
  const references = walk(distDir)
    .filter((file) => referenceExtensions.has(extensionOf(file)))
    .map((file) => readFileSync(file, "utf8"))
    .join("\n");

  for (const file of walk(astroAssetsDir)) {
    if (!removableExtensions.has(extensionOf(file))) continue;

    const name = file.split(/[\\/]/).at(-1);
    if (name && !references.includes(name)) {
      rmSync(file);
    }
  }

  const removed = walk(astroAssetsDir).filter(
    (file) => removableExtensions.has(extensionOf(file)) && statSync(file).size === 0,
  );
  for (const file of removed) rmSync(file);
}
