#!/usr/bin/env python3
"""
v4 — Calidad maxima 95 + UnsharpMask balanceado (radius 1.0 percent 60).
Tamanos full max-up to original. Backup automatico.
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
                      f"img.backup-v4-{datetime.now():%Y%m%d-%H%M%S}")

# Tamano max-up generoso: si la original es grande, generar version casi full
# Esto da version retina nitida en displays grandes
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

# Maximo tamano por aspect - generoso para retina
SIZES = {
    "portrait":    [(1800, 2700), (1100, 1650), (550, 825)],
    "portrait43":  [(2000, 1500), (1200, 900),  (600, 450)],
    "landscape":   [(2400, 1350), (1300, 731),  (650, 366)],
    "landscape32": [(2000, 1333), (1200, 800),  (600, 400)],
    "landscape43": [(1900, 1425), (1200, 900),  (600, 450)],
    "wide":        [(2600, 1463), (1500, 844),  (750, 422)],
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
    # No upscale: si el original es mas chico, recortar pero no escalar para arriba
    if im.width < target_w * 1.05 or im.height < target_h * 1.05:
        # Original demasiado chico, ajustar target a su tamano max
        scale = min(im.width / target_w, im.height / target_h)
        target_w = int(target_w * scale)
        target_h = int(target_h * scale)
    return ImageOps.fit(im, (target_w, target_h), method=Image.LANCZOS, centering=(0.5, focal_y))

def enhance(im):
    """UnsharpMask BALANCEADO (mas sutil para no artefactar) + leve color/contrast."""
    im = im.filter(ImageFilter.UnsharpMask(radius=1.0, percent=60, threshold=3))
    im = ImageEnhance.Color(im).enhance(1.05)
    im = ImageEnhance.Contrast(im).enhance(1.04)
    return im

def save_webp(im, path, quality=95):
    # Method 6 (slowest, best compression). Lossless not used (file size).
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
        orig_size = im.size
        for i, (tw, th) in enumerate(sizes):
            if i == 0:
                out_path = os.path.join(OUT, dest)
                q = 95
            else:
                base, ext = os.path.splitext(dest)
                suffix = "-md" if i == 1 else "-sm"
                out_path = os.path.join(OUT, f"{base}{suffix}{ext}")
                q = 90 if i == 1 else 85
            resized = fit_cover(im, tw, th, focal_y)
            resized = enhance(resized)
            save_webp(resized, out_path, quality=q)
            real_w, real_h = resized.size
            stats.append((os.path.basename(out_path), real_w, real_h, os.path.getsize(out_path)//1024))
            print(f"[ok] {os.path.basename(out_path):28s} {real_w:4d}x{real_h:<4d} q={q}  {os.path.getsize(out_path)//1024:>5d} KB  (orig {orig_size[0]}x{orig_size[1]})")

total = sum(s[3] for s in stats)
print(f"\nTOTAL: {len(stats)} archivos, {total} KB ({total/1024:.1f} MB)")
if missing:
    print(f"\n[!] MISSING: {missing}")
print("DONE.")
