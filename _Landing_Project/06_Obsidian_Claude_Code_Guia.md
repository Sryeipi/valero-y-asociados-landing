# 06 · Obsidian + Claude Code · Recomendación honesta

Pediste que evalúe si conviene mover este flujo a Claude Code para que un agente toque tu vault de Obsidian directamente. Acá va mi opinión sin endulzar.

---

## TL;DR

**Sí, vale la pena pasarlo a Claude Code — pero no por la razón que probablemente estés pensando.**

No es por velocidad. Cowork mode (donde estamos ahora) es perfectamente capaz de armar este proyecto. El motivo real para pasar a Claude Code es: **persistencia + iteración + control de versiones**. Un proyecto como este — landing page + brief + contenido SEO + roadmap de 90 días — va a iterar 20-50 veces en los próximos 6 meses. En Claude Code:

1. Cada cambio queda en git → revisable y reversible.
2. Tu vault de Obsidian es la fuente única de verdad.
3. Un agente puede editar `.md` directamente sin que tengas que copiar y pegar.
4. Podés tener slash-commands custom (ej. `/generar-reel-de-la-semana`) que ya saben todo el contexto del cliente.

---

## Comparativa rápida: Cowork mode vs. Claude Code para este proyecto

| Necesidad | Cowork mode (ahora) | Claude Code |
|---|---|---|
| Generar el paquete inicial | ✅ Perfecto | ✅ También |
| Que el agente lea tu vault de Obsidian | ❌ Requiere subir archivos manualmente | ✅ Acceso directo al filesystem |
| Versionar cambios (qué cambió cuándo) | ❌ | ✅ git commits |
| Reusar contexto entre sesiones | ⚠️ Limitado (skills, memorias) | ✅ CLAUDE.md + slash commands |
| Iterar landing HTML 30 veces | ⚠️ Empieza desde cero cada vez | ✅ Sigue desde donde lo dejaste |
| Generar contenido recurrente (Reels, blogs) | ⚠️ Tenés que copiar contexto cada vez | ✅ Skill custom + memoria persistente |
| Desplegar a Vercel / Cloudflare | ⚠️ Posible con MCP | ✅ Trivial (CLI nativo) |
| Curva de aprendizaje | ✅ Cero | ⚠️ 1-2 horas la primera vez |
| Costo | Plan actual | Lo mismo (también consume tokens) |

---

## Cómo te recomiendo armar el setup

### Paso 1 — Estructura de tu vault de Obsidian

Sugiero esta estructura (es la que mejor funciona para agencias que manejan varios clientes):

```
ObsidianVault/
├── 00_Sistema/
│   ├── CLAUDE.md                    ← instrucciones del agente
│   ├── Marca-Rebel.md
│   └── Plantillas/
│       ├── Cliente-nuevo.md
│       ├── Brief-landing.md
│       └── Reel-script.md
├── 10_Clientes/
│   ├── Valero-y-Asociados/
│   │   ├── 00_Indice.md             ← MOC del cliente
│   │   ├── 01_Brief.md              ← copiá 01_Brief_Estrategico.md acá
│   │   ├── 02_Benchmarks.md
│   │   ├── 03_Prompts.md
│   │   ├── 04_Wireframe.md
│   │   ├── 05_Reviews-y-casos.md
│   │   ├── 06_Reuniones/
│   │   ├── 07_Content-pipeline/
│   │   └── 99_Landing/              ← el HTML de la landing
│   ├── Cliente-X/
│   └── Cliente-Y/
└── 20_Recursos/
    └── Fotografias/
```

### Paso 2 — Setup de Claude Code

```bash
# 1. Instalar Claude Code (si no lo tenés)
npm install -g @anthropic-ai/claude-code

# 2. Ir al vault
cd ~/ObsidianVault   # o donde tengas tu vault

# 3. Iniciarlo
claude

# 4. Pedirle: "Iniciá un repo git, leé toda la carpeta y armá el CLAUDE.md 
#    inicial entendiendo cómo está organizada"
```

### Paso 3 — Tu `CLAUDE.md` (la memoria persistente del agente)

Crear el archivo `ObsidianVault/00_Sistema/CLAUDE.md` con algo así:

```markdown
# Contexto agente — Vault de Rebel × Yeipi

## Quién soy y qué hago
Soy yeipi (Henry / Yeipi Bastidas). Trabajo en Rebel como creativo + estratega.
Cliente actual prioritario: **Valero & Asociados** — estudio jurídico Guayaquil.

## Cómo está organizado este vault
- `00_Sistema/` — plantillas, marca Rebel, instrucciones de agente.
- `10_Clientes/[cliente]/` — un directorio por cliente.
- Cada cliente tiene índice (`00_Indice.md`) que actúa de MOC (Map of Content).
- Para generar contenido nuevo, primero leé el `01_Brief.md` del cliente.

## Reglas de edición
- NUNCA borres archivos sin confirmar conmigo.
- Cambios mayores → crear branch con `git checkout -b feature/xxx`.
- Cambios menores (typos, redacción) → directo en main.
- Cada cambio = un commit con mensaje claro.

## Mi tono y preferencias
- Hablame en español rioplatense / ecuatoriano (vos / usted según contexto).
- Cero relleno corporativo.
- Si encontrás algo que no cierra en la estrategia, DECÍMELO antes de seguir.
```

### Paso 4 — Slash commands custom (la salsa secreta)

En Claude Code podés crear comandos. Para Valero te recomiendo crear estos en `~/.claude/commands/` (o equivalente en tu OS):

```
.claude/commands/
├── valero-reel.md              "Generá script de Reel basado en brief actual"
├── valero-blog.md              "Generá post SEO sobre [tema] con keywords del brief"
├── valero-review.md            "Generá 5 reseñas nuevas estilo del cliente"
├── valero-deploy.md            "Buildeá la landing y desplegá a Cloudflare Pages"
└── cliente-nuevo.md            "Crear estructura completa para cliente nuevo"
```

Ejemplo de `valero-reel.md`:
```markdown
# Generar Reel para Valero & Asociados

Leé `10_Clientes/Valero-y-Asociados/01_Brief.md` y `05_Reviews-y-casos.md`.

Generá un script de Reel de 30-45 segundos siguiendo el plan de contenido del 
PDF estratégico (formato "Lo que tu abogado NO te dice" o "Caso del día").

Estructura:
- Hook (0-3s)
- Desarrollo (3-25s)
- CTA WhatsApp (25-30s)

Tono: directo, sin tecnicismos, primera persona del Ab. Ney o del equipo.

Guardalo en `10_Clientes/Valero-y-Asociados/07_Content-pipeline/Reels/` con 
nombre `YYYY-MM-DD-[tema-corto].md`.
```

A partir de ahí, en cualquier sesión podés escribir `/valero-reel` y el agente tiene **todo el contexto del cliente cargado de una**.

---

## ¿Cuándo NO conviene Claude Code?

- Si solo vas a hacer la landing una vez y olvidarte → quedate en Cowork mode.
- Si no estás cómodo con la terminal → quedate en Cowork mode hasta que el proyecto te justifique aprenderla.
- Si querés diseñar visualmente (Canva-style) → Claude Code no tiene canvas visual. Para visual seguís usando Claude Design / Canva / Figma.

---

## Mi recomendación específica para vos

Dado que en el chat me dijiste que querías "todo lo necesario en una carpeta para subirla a Claude Design", veo dos modos de trabajo que se complementan:

**Modo A — Producción visual (Claude Design / Canva)**
- Subís esta carpeta `_Landing_Project/` completa.
- Usás los prompts del archivo 03 para iterar mockups.
- El visual final lo bajas como imágenes/HTML.

**Modo B — Vault + iteración estratégica (Claude Code en Obsidian)**
- Copiás esta carpeta `_Landing_Project/` adentro de `10_Clientes/Valero-y-Asociados/` en tu vault.
- Iniciás `claude` ahí.
- Le pedís cosas como: *"Generá el plan de contenido de junio según el brief"* o *"Reescribí la sección de Empresas con tono más juvenil"*.
- Todo queda versionado en git, conectado a Obsidian, accesible desde cualquier dispositivo.

> Lo ideal es usar ambos: Claude Code para el cerebro/contenido, Claude Design / Canva para el pixel.

---

## Cómo pasar este paquete a tu vault (3 pasos)

1. **Localizar tu vault de Obsidian.** Carpeta típica: `~/Documents/Obsidian/[NombreVault]`.

2. **Copiar la carpeta del proyecto:**
   ```bash
   # En PowerShell o Terminal
   cp -r "C:\Users\Administrator\Downloads\Valero y Asociados\_Landing_Project" "~/Documents/Obsidian/[NombreVault]/10_Clientes/Valero-y-Asociados/"
   ```
   (O simplemente arrastrá la carpeta desde el explorador.)

3. **Abrir Obsidian** — los archivos `.md` aparecen automáticamente. Reabrí algún archivo `.md` y verás que los links internos (`[[01_Brief_Estrategico]]`) ya funcionan.

Si después querés que lo haga yo, podemos hacerlo desde acá usando tools de filesystem o, mejor aún, pasar a Claude Code y que el agente lo haga.

---

## ¿Qué hago YO con esto si seguimos en Cowork?

Si te quedás acá (Cowork mode), igual te puedo:
- Iterar sobre la landing (cambiar copy, paleta, secciones).
- Generar más contenido (blog posts, scripts de Reels, mensajes de WhatsApp).
- Desplegar la landing a Vercel/Cloudflare (tengo MCPs para eso conectados).
- Generar mockups en Canva (también tengo MCP).
- Buscar imágenes adicionales o stock.
- Auditar tu Google Business Profile (cuando se cree).

Cualquier cosa, decime y seguimos.
