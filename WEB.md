# La página de cada app y cada juego en iaen.es

Cada app y cada juego tiene su página en `https://iaen.es/android/<slug>/` y su política de privacidad en
`https://iaen.es/android/<slug>/privacy/`. Google Play exige la política publicada antes de enviar, y los «Acerca
de» enlazan a las dos.

## El repo de la web
- `IAnMove/home` (privado), clonado en `~/customprograms/iaen-home`. **Todo lo que llega a `main` se despliega solo
  en iaen.es**: se trabaja siempre en una rama `android-<slug>` (mejor en un worktree aparte:
  `git -C ~/customprograms/iaen-home worktree add <carpeta> -b android-<slug> origin/main`) y la fusiona ina.
- Puede haber otras sesiones en ese repo: no toques sus ramas ni el árbol principal.

## Qué hay en la web
| Ruta | Qué es |
|---|---|
| `android/index.html` y `android/en/index.html` | Concentrador ES/EN, con las secciones `#apps` y `#juegos` (las anclas están en la rama `android-anclas`, sin fusionar) |
| `android/<slug>/index.html` y `android/<slug>/en/index.html` | Página de la app o el juego en español y en inglés, cada una con su URL (`hreflang` es/en/x-default) |
| `android/<slug>/privacy/index.html` y `android/<slug>/privacy/en/index.html` | Política de privacidad (ES y EN) |
| `android/img/` | `<slug>-icon.webp` (256 px), capturas `<slug>-<n>.webp` o `<slug>-<es|en>-<n>.webp`, imagen OG `og-<slug>.jpg` (1024×500) |
| `img/android-<slug>.webp` | Tarjeta 800×500 de la portada |
| `index.html` | Portada; sección «// Android» con una tarjeta por app y juego |
| `android/android.css` | Estilos comunes; no metas CSS suelto en las páginas |

## Cómo tiene que ser una página
- Cabecera común (iaen.es / android, GitHub, X, botón ES/EN), migas `iaen.es / android / <slug>`.
- Bloque principal: icono, género, nombre, frase, y botones **Google Play** (o «Google Play · próximamente» si aún
  no está), **Política de privacidad** y **Código fuente** solo si hay repo público.
- Capturas reales (las mismas de la ficha de Play), descripción, «Qué hace» / «Qué hay» con las funciones,
  «Bueno saber» (permisos, sin anuncios, sin internet si es verdad) y la línea del autor con @theinaog.
- «Otras apps» (en una app) u «Otros juegos» (en un juego), con enlace a `/android/#apps` o `/android/#juegos`.
- SEO: `<title>` «Nombre — frase · Android», `meta description` con la palabra clave principal en español,
  `canonical`, Open Graph con `og-<slug>.jpg`, JSON-LD `SoftwareApplication` (como `android/lupa/`), textos
  ES y EN completos (no traducción automática a medias) y, si hay, preguntas frecuentes reales.
- Privacidad: el texto de `PRIVACY.md` de la app (o el genérico de los juegos), con fecha y `contacto@iaen.es`.
- Tarjeta en `android/index.html` y `android/en/index.html`, en **Apps** o **Juegos** según sea, y en la sección
  «// Android» de `index.html`.

## Cómo se hacen
- **Juegos: ya hechas las 17.** Se generaron con `python3 publish/make_web.py` (desde `~/games`, a partir de
  `~/games/publish/games.json`), pero después se mejoraron a mano para SEO (versión EN con URL propia, JSON-LD,
  títulos ≤60, preguntas frecuentes en Pesca). **No vuelvas a ejecutar `make_web.py` sobre las existentes**: lo
  machacaría. Cambia las páginas a mano (ES y EN) y usa `make_web.py` solo como referencia para un juego nuevo.
  Las tarjetas de juegos van entre `<!-- juegos-android:inicio -->` y `<!-- juegos-android:fin -->`.
- **Apps: a mano, copiando `android/lupa/`** (página ES y EN, privacidad ES y EN, imágenes y tarjetas). Textos sacados de la ficha
  `en-US`/`es-ES` y de `PRIVACY.md` de la app. Ya están CaptureCam y Lupa.
- Comprobación local antes de commitear: `python3 -m http.server` en la raíz del repo y capturas con
  `chromium --headless --screenshot` en escritorio (1440 px) y móvil (390 px); mira cada captura.
- Cuando una app o juego salga en Play: su URL en `play_url` de `games.json` (juegos) o en su página (apps), y en
  el «Acerca de» (`~/games/publish/about_info.gd` → `publish/sync_about.sh`, o `links.xml` en las apps).
