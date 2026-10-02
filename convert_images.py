"""Write a .webp next to every large PNG/JPG directly under a folder (not recursive).
Originals are kept; the page-image include uses the .webp when it exists.
Outputs newer than the source are skipped, and a .webp that is not clearly smaller is removed.
Usage: python convert_images.py [folder]   (default: assets/images; needs ffmpeg on PATH)
"""
import subprocess, sys
from pathlib import Path

root = Path(sys.argv[1] if len(sys.argv) > 1 else "assets/images")
MIN_KB = 200      # smaller files are not worth converting
KEEP_RATIO = 0.8  # keep the webp only if it is at least 20% smaller

for src in sorted(p for p in root.iterdir() if p.suffix.lower() in (".png", ".jpg", ".jpeg")):
    size = src.stat().st_size
    out = src.with_suffix(".webp")
    if size < MIN_KB * 1024:
        continue
    if out.exists() and out.stat().st_mtime >= src.stat().st_mtime:
        continue
    r = subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", str(src), "-c:v", "libwebp", "-quality", "85", "-compression_level", "6", str(out)])
    if r.returncode or out.stat().st_size > size * KEEP_RATIO:
        out.unlink(missing_ok=True)
        print("skip", src.name)
        continue
    print(f"{src.name}: {size // 1024} KB -> {out.stat().st_size // 1024} KB")
