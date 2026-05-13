#!/usr/bin/env python3
"""
v3 — Calidad 92 con sharpening fuerte + tamanos mas grandes para mejor render desktop.
Busca originales en multiples locations. Backup automatico.
"""
import os, shutil
from datetime import datetime
from PIL import Image, ImageOps, ImageFilter, ImageEnhance

ROOT = r"C:\Users\Administrator\Documents\Obsidian Vault\03_CLIENTES\Valero y Asociados"
ORIG_LOCS = [
    ROOT,
    r"C:\Users\Administrator\Documents\Codex\2026-05-11\files-mentioned-by-the-user-valero\zip-inspect-valero-1\uploads",
    r"C:\Users\Administrator\Documents\Codex\2026-05-11\files-mentioned-by-the-user-valero\zip-inspect-valero-1",
]
OUT = os.path.join(ROOT, "_Landing_Project", "landing", "img")
BACKUP = os.path.join(ROOT, "_Landing_Project",
                      f"img.backup-v3-{datetime.now():%Y%m%d-%H%M%S}")

MAP = {
    "ney.webp":         ("ney.jpg",                                           "portrait",    0.22),
    "hero-main.webp":   ("MAIN image.png",                                    "wide",        0.35),
    "adrian.webp":      ("adrian.PNG",                                        "portrait43",  0.20),
    "daniel.webp":      ("daniel.PNG",                                        "portrait43",  0.20),
    "patricia.webp":    ("patricia.PNG",                                      "landscape32", 0.30),
    "scene-01.webp":    ("ChatGPT Image Apr 22, 2026, 08_47_26 PM.PNG",       "portrait",    0.22),
    "scene-02.webp":    ("ChatGPT Image Apr 22, 2026, 08_47_33 PM.PNG",       "portrait",    0.22),
    "scene-03.webp":    ("ChatGPT Image Apr 22, 2026, 08_49_17 PM.PNG",       "landscape",   0.40),
    "scene-04.webp":    ("ChatGPT Image Apr 22, 2026, 09_10_33 PM.PNG",       "landscape",   0.35),
    "scene-05.webp":    ("ChatGPT Image Apr 22, 2026, 09_27_01 PM.PNG",       "portrait43",  0.22),
    "scene-06.webp":    ("ChatGPT Image Apr 22, 2026, 09_27_01 PM.PNG",       "portrait43",  0.22),
    "scene-07.webp":    ("ChatGPT Image Apr 22, 2026, 09_27_33 PM.PNG",       "landscape",   0.40),
    "scene-08.webp":    ("ChatGPT Image Apr 22, 2026, 09_10_33 PM.PNG",       "landscape",   0.35),
    "editorial-01.webp":("67FAB200-1413-4958-9B90-6EA439B8B90F.PNG",          "landscape43", 0.30),
    "editorial-02.webp":("ChatGPT Image Apr 22, 2026, 08_47_33 PM.PNG",       "portrait",    0.22),
    "editorial-03.webp":("MAIN image.png",                                    "wide",        0.35),
    "ney-alt.webp":     ("ney.jpg",                                           "portrait",    0.22),
}

# Tamanos mas grandes para retina DPR2 + sharpening fuerte
SIZES = {
    "portrait":    [(1600, 2400), (900, 1350), (500, 750)],
    "portrait43":  [(1800, 1350), (1100, 825), (550, 413)],
    "landscape":   [(2200, 1238), (1100, 619), (550, 310)],
    "landscape32": [(1800, 1200), (1100, 733), (550, 367)],
    "landscape43": [(1700, 1275), (1100, 825), (550, 413)],
    "wide":        [(2400, 1350), (1400, 788), (700, 394)],
}

os.makedirs(OUT, exist_ok=True)
if not os.path.isdir(BACKUP):
    os.makedirs(BACKUP, exist_ok=True)
    for f in os.listdir(OUT):
        if f.lower().endswith(".webp"):
            shutil.copy2(os.path.join(OUT, f), os.path.join(BACKUP, f))
print(f"[backup] {BACKUP}")

def find_src(name):
    for loc in ORIG_LOCS:
        p = os.path.join(loc, name)
        if os.path.isfile(p):
            return p
    return None

def fit_cover(im, target_w, target_h, focal_y=0.4):
    return ImageOps.fit(im, (target_w, target_h), method=Image.LANCZOS, centering=(0.5, focal_y))

def enhance(im):
    """Sharpening fuerte + color/contrast boost editorial."""
    im = im.filter(ImageFilter.UnsharpMask(radius=1.8, percent=120, threshold=2))
    im = ImageEnhance.Color(im).enhance(1.08)
    im = ImageEnhance.Contrast(im).enhance(1.06)
    im = ImageEnhance.Brightness(im).enhance(1.02)
    return im

def save_webp(im, path, quality=92):
    im.save(path, "WEBP", quality=quality, method=6)

stats = []
missing = []
for dest, (src_name, mode, focal_y) in MAP.items():
    src_path = find_src(src_name)
    if not src_path:
        print(f"[MISS] {dest} <- {src_name}")
        missing.append(src_name)
        continue
    sizes = SIZES.get(mode, SIZES["landscape"])
    with Image.open(src_path) as im:
        im = ImageOps.exif_transpose(im)
        if im.mode in ("RGBA", "P"):
            im = im.convert("RGB")
        for i, (tw, th) in enumerate(sizes):
            if i == 0:
                out_path = os.path.join(OUT, dest)
                q = 92
            else:
                base, ext = os.path.splitext(dest)
                suffix = "-md" if i == 1 else "-sm"
                out_path = os.path.join(OUT, f"{base}{suffix}{ext}")
                q = 88 if i == 1 else 84
            resized = fit_cover(im, tw, th, focal_y)
            resized = enhance(resized)
            save_webp(resized, out_path, quality=q)
            stats.append((os.path.basename(out_path), tw, th, os.path.getsize(out_path)//1024))
            print(f"[ok] {os.path.basename(out_path):28s} {tw:4d}x{th:<4d} q={q}  {os.path.getsize(out_path)//1024:>4d} KB")

total = sum(s[3] for s in stats)
print(f"\nTOTAL: {len(stats)} archivos, {total} KB ({total/1024:.1f} MB)")
if missing:
    print(f"\n[!] MISSING ORIGINALS: {missing}")
print("DONE.")
