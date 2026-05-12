#!/usr/bin/env python3
"""
Regenera las WebP de la landing Valero a partir de los PNG/JPG originales.
v2: encuadre correcto para retratos (caras arriba), calidad 88, sharpening sutil.
"""
import os, sys, shutil
from datetime import datetime
from PIL import Image, ImageOps, ImageFilter, ImageEnhance

ROOT = r"C:\Users\Administrator\Downloads\Valero y Asociados"
ORIG = ROOT
OUT = os.path.join(ROOT, "_Landing_Project", "landing", "img")
BACKUP = os.path.join(ROOT, "_Landing_Project",
                      f"img.backup-v2-{datetime.now():%Y%m%d-%H%M%S}")

# (archivo_origen, modo, focal_y) — focal_y es vertical centering 0..1, 0=top
# Para retratos editoriales, la cara está en el primer tercio vertical => focal_y bajo
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

SIZES = {
    "portrait":    [(1200, 1800), (700, 1050), (400, 600)],
    "portrait43":  [(1448, 1086), (900, 675),  (450, 338)],
    "landscape":   [(1800, 1013), (900, 506),  (450, 253)],
    "landscape32": [(1500, 1000), (900, 600),  (450, 300)],
    "landscape43": [(1400, 1050), (900, 675),  (450, 338)],
    "wide":        [(2000, 1125), (1200, 675), (600, 338)],
}

os.makedirs(OUT, exist_ok=True)
if not os.path.isdir(BACKUP):
    os.makedirs(BACKUP, exist_ok=True)
    for f in os.listdir(OUT):
        if f.lower().endswith(".webp"):
            shutil.copy2(os.path.join(OUT, f), os.path.join(BACKUP, f))
print(f"[backup] {BACKUP}")

def fit_cover(im, target_w, target_h, focal_y=0.4):
    """Resize+crop preservando aspect, centrando en (0.5, focal_y)."""
    return ImageOps.fit(im, (target_w, target_h), method=Image.LANCZOS, centering=(0.5, focal_y))

def enhance(im):
    """Sharpening sutil + color boost para fotos editoriales."""
    im = im.filter(ImageFilter.UnsharpMask(radius=1.2, percent=70, threshold=2))
    im = ImageEnhance.Color(im).enhance(1.05)
    im = ImageEnhance.Contrast(im).enhance(1.03)
    return im

def save_webp(im, path, quality=88):
    im.save(path, "WEBP", quality=quality, method=6)

stats = []
for dest, (src_name, mode, focal_y) in MAP.items():
    src_path = os.path.join(ORIG, src_name)
    if not os.path.isfile(src_path):
        print(f"[MISS] {dest} <- {src_name} (no existe)")
        continue
    sizes = SIZES.get(mode, SIZES["landscape"])
    with Image.open(src_path) as im:
        im = ImageOps.exif_transpose(im)
        if im.mode in ("RGBA", "P"):
            im = im.convert("RGB")
        for i, (tw, th) in enumerate(sizes):
            if i == 0:
                out_path = os.path.join(OUT, dest)
                q = 88
            else:
                base, ext = os.path.splitext(dest)
                suffix = "-md" if i == 1 else "-sm"
                out_path = os.path.join(OUT, f"{base}{suffix}{ext}")
                q = 84 if i == 1 else 80
            resized = fit_cover(im, tw, th, focal_y)
            resized = enhance(resized)
            save_webp(resized, out_path, quality=q)
            stats.append((os.path.basename(out_path), tw, th, os.path.getsize(out_path)//1024))
            print(f"[ok] {os.path.basename(out_path):28s} {tw:4d}x{th:<4d} q={q}  {os.path.getsize(out_path)//1024:>4d} KB")

total = sum(s[3] for s in stats)
print(f"\nTOTAL: {len(stats)} archivos, {total} KB ({total/1024:.1f} MB)")
print("DONE.")
