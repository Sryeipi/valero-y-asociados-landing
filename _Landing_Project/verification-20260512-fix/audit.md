# Verification v5 — fix coherencia visual (2026-05-12)

Branch: `fix/landing-coherencia-visual`
Commits: f594388 → 7ae62f0 → f90bffc → 64c480e → 967e452

## Resultados Playwright

### Desktop @ 1440×900
- ✅ Hero v5 renderiza: `.hero` exists, `.hero-cinema` removed.
- ✅ Foto hero: `ney.webp` carga (cargó `ney-md.webp` 700w en DPR1 — en DPR2 cargará 1200w).
- ✅ H1 "Protegemos lo que más le importa." con gold sweep.
- ✅ Hero quote del fundador absorbida con `cite`.
- ✅ 4 secciones eliminadas confirmadas (`.hero-cinema`, `.method-scroll`, `.atmosphere`, `#fundador` = false).
- ✅ DocHeight: 10432px (vs 15163 v4 = -31%).
- ✅ 0 errores de consola.

### Proceso v5
- ✅ 3 `.step-card` en grid 3-col.
- ✅ Iconos SVG line 32px stroke 1.5 en circulo dorado 56px.
- ✅ Eyebrow "PASO 01 · CONVERSACIÓN" mono con línea dorada.
- ✅ Old `.step:not(.step-card)` ocultos.

### Equipo v5
- ✅ 3 miembros (Adrián, Patricia, Daniel) — Ney removido del grid.
- ✅ Grid template: `386.656px 386.672px 386.656px` (3-col).
- ✅ Aspect ratio 4/3 horizontal aplicado (387×290 cada foto).
- ✅ Object-position por persona: center 30% / 35% / 25%.

### Mobile @ 390×844 (iPhone 14 Pro)
- ✅ scrollWidth: 390 = viewport → **sin overflow horizontal**.
- ✅ DocHeight: 10887px (vs 15333 v4 = -29%).
- ✅ Solo 2 elementos "overflow" detectados: `marquee-track` (4949px, scrollea horizontal por diseño) y `cases` (406px, scroll horizontal por diseño). Ambos esperados.
- ✅ 0 errores de consola.

## Imágenes en producción

Quedan en `landing/img/` solo las 6 personas reales:
- adrian, daniel, hero-main, ney, ney-alt, patricia (× 3 variantes -sm/-md/full)

Backups separados:
- `_Landing_Project/img.backup-scenes-20260512/` — 24 archivos scene-*.webp
- `_Landing_Project/img.backup-editorials-20260512/` — 9 archivos editorial-*.webp
- `_Landing_Project/img.backup-v2-20260512-002912/` — variantes anteriores
- `_Landing_Project/img.backup-webp-broken-20260512-001931/` — WebP rotas v1
- `_Landing_Project/landing.backup-20260511-204625/` — HTML pre-v2

## Secciones finales (7 + cierre, vs 12 en v4)

1. Hero (con quote del fundador absorbida)
2. Marquee credenciales
3. 02 — Áreas de práctica (3 cards)
4. 03 — Cómo trabajamos (3 step-cards editorial)
5. 04 — Casos resueltos (KPIs + 6 casos scroll horizontal)
6. 05 — Equipo (3 miembros, sin Ney duplicado)
7. 06 — Confianza (6 pilares anti-reseñas-falsas)
8. 07 — Preguntas frecuentes (6 FAQs)
9. Cierre + Footer + WhatsApp flotante + Sticky CTA

## Pendiente

- Limpieza JS de listeners para componentes eliminados (sin impacto funcional, solo housekeeping).
- Limpieza CSS de selectores muertos (`.hero-cinema`, `.method-*`, `.tile`, `.mosaic`, etc.) — son código muerto, no afectan render.
- Dirección oficina real en FAQ + footer.
- Cuando llegue WhatsApp comercial real: reemplazar `593959080607` (4+ ubicaciones).

## Decisión de merge

**NO mergeado a `main` por instrucción explícita del cowork.** Branch lista para review del usuario.

Para mergear cuando esté aprobado:
```bash
cd "/c/Users/Administrator/Downloads/Valero y Asociados"
git checkout main
git merge fix/landing-coherencia-visual
```
