"""
Resizes photos dropped in original_photos/ (repo root) and writes web-ready
JPEGs into website/src/assets/photos/, for use as thumbnails/hero images.

To run the script:
  pip install -r requirements.txt
  python process_photos.py
"""

import os
from pathlib import Path

from PIL import Image, ImageOps

REPO_ROOT = Path(__file__).resolve().parent.parent
SOURCE_DIR = REPO_ROOT / "original_photos"
TARGET_DIR = REPO_ROOT / "website" / "src" / "assets" / "photos"

MAX_WIDTH = 1400
JPEG_QUALITY = 80
SOURCE_EXTENSIONS = {".jpg", ".jpeg", ".png", ".webp", ".heic", ".heif", ".tif", ".tiff"}


def process_photo(source_path, target_path):
    with Image.open(source_path) as image:
        image = ImageOps.exif_transpose(image)
        if image.mode != "RGB":
            image = image.convert("RGB")
        if image.width > MAX_WIDTH:
            height = round(image.height * MAX_WIDTH / image.width)
            image = image.resize((MAX_WIDTH, height), Image.LANCZOS)
        image.save(target_path, "JPEG", quality=JPEG_QUALITY, optimize=True)


def main():
    if not SOURCE_DIR.is_dir():
        print(f"No original_photos/ folder found at {SOURCE_DIR}")
        return

    TARGET_DIR.mkdir(parents=True, exist_ok=True)

    files = sorted(
        f for f in os.listdir(SOURCE_DIR)
        if (SOURCE_DIR / f).is_file() and Path(f).suffix.lower() in SOURCE_EXTENSIONS
    )

    if not files:
        print(f"No photos found in {SOURCE_DIR}")
        return

    processed = 0
    skipped = 0
    for name in files:
        source_path = SOURCE_DIR / name
        target_path = TARGET_DIR / f"{Path(name).stem}.jpg"

        if target_path.exists() and target_path.stat().st_mtime >= source_path.stat().st_mtime:
            skipped += 1
            continue

        process_photo(source_path, target_path)
        print(f"{name} -> website/src/assets/photos/{target_path.name}")
        processed += 1

    print(f"Processed {processed} photo(s), skipped {skipped} already up to date.")


if __name__ == "__main__":
    main()
