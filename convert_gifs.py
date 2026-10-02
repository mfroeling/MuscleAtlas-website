"""Convert every GIF under a folder to .webm and .mp4 next to it.
Originals are kept. Outputs newer than the GIF are skipped, so it is safe to re-run.
Usage: python convert_gifs.py [folder]   (default: assets/images; needs ffmpeg on PATH)
"""
import subprocess, sys
from pathlib import Path

root = Path(sys.argv[1] if len(sys.argv) > 1 else "assets/images")
# yuv420p needs even dimensions
scale = "scale=trunc(iw/2)*2:trunc(ih/2)*2"
codecs = {
    ".webm": ["-c:v", "libvpx-vp9", "-crf", "36", "-b:v", "0", "-pix_fmt", "yuv420p"],
    ".mp4": ["-c:v", "libx264", "-crf", "26", "-preset", "slow", "-pix_fmt", "yuv420p", "-movflags", "+faststart"],
}

gifs = sorted(root.rglob("*.gif"))
for i, gif in enumerate(gifs, 1):
    for ext, args in codecs.items():
        out = gif.with_suffix(ext)
        if out.exists() and out.stat().st_mtime >= gif.stat().st_mtime:
            continue
        r = subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", str(gif), "-vf", scale, "-an", *args, str(out)])
        if r.returncode:
            print("FAILED", out)
    kb = lambda e: gif.with_suffix(e).stat().st_size // 1024 if gif.with_suffix(e).exists() else "-"
    print(f"[{i}/{len(gifs)}] {gif.name}: gif {gif.stat().st_size // 1024} KB, webm {kb('.webm')} KB, mp4 {kb('.mp4')} KB", flush=True)
