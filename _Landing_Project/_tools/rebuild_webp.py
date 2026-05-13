#!/usr/bin/env python3
"""
v5 PIXEL-PERFECT: calidad 100, SIN sharpening, SIN color/contrast enhance.
Las WebP salen identicas visualmente a las originales. Sin perdida de calidad.
"""
import os, shutil
from datetime import datetime
from PIL import Image, ImageOps

ROOT = r"C:\Users\Administrator\Documents\Obsidian Vault\03_CLIENTES\Valero y Asociados"
ORIG_LOCS = [
    ROOT,
    r"C:\Users\Administrator\Documents\Codex\2026-05-11\files-mentioned-by-the-user-valero\zip-inspect-valero-1\uploads",
    r"C:\Users\Administrator\Documents\Codex\2026-05-11\files-mentioned-by-the-user-valero\zip-inspect-valero-1",
]
OUT = os.path.join(ROOT, "_Landing_Project", "landing", "img")
BACKUP = os.path.join(ROOT, "_Landing_Project",
                      f"img.backup-v5-{datetime.now():%Y%m%d-%H%M%S}")

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

# Tamano target: ajustado al original maximo, sin upscale
SIZES = {
    "portrait":    [(1290, 1935), (900, 1350), (550, 825)],   # respeta ney 1290x2033
    "portrait43":  [(1448, 1086), (1100, 825), (600, 450)],   # respeta adrian/daniel 1448x1086
    "landscape":   [(1672, 940),  (1100, 619), (650, 366)],   # respeta scenes 1672x941
    "landscape32": [(1500, 1000), (1100, 733), (600, 400)],   # respeta patricia 1537x1023
    "landscape43": [(1402, 1051), (1100, 825), (600, 450)],   # respeta 67FAB 1402x1122
    "wide":        [(2400, 1350), (1400, 788), (700, 394)],   # MAIN 5225x2941 escalado
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
    # NO upscale jamas
    if im.width < target_w or im.height < target_h:
        scale = min(im.width / target_w, im.height / target_h)
        target_w = max(1, int(target_w * scale))
        target_h = max(1, int(target_h * scale))
    return ImageOps.fit(im, (target_w, target_h), method=Image.LANCZOS, centering=(0.5, focal_y))

# NO enhance, NO sharpening - pixel-perfect

def save_webp(im, path, quality=100):
    # Quality 100 + method 6 (best compression)
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
                q = 100  # full size pixel-perfect
            else:
                base, ext = os.path.splitext(dest)
                suffix = "-md" if i == 1 else "-sm"
                out_path = os.path.join(OUT, f"{base}{suffix}{ext}")
                q = 95 if i == 1 else 90
            resized = fit_cover(im, tw, th, focal_y)
            # NO enhance aqui
            save_webp(resized, out_path, quality=q)
            real_w, real_h = resized.size
            stats.append((os.path.basename(out_path), real_w, real_h, os.path.getsize(out_path)//1024))
            print(f"[ok] {os.path.basename(out_path):28s} {real_w:4d}x{real_h:<4d} q={q}  {os.path.getsize(out_path)//1024:>5d} KB  (orig {orig_size[0]}x{orig_size[1]})")

total = sum(s[3] for s in stats)
print(f"\nTOTAL: {len(stats)} archivos, {total} KB ({total/1024:.1f} MB)")
if missing:
    print(f"\n[!] MISSING: {missing}")
print("DONE.")
