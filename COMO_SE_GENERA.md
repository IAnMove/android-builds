# Publicación en Google Play: parte común de todos los juegos

Lo que comparten los juegos de `~/games` de cara a la tienda. Nada de aquí sale de esta máquina solo.

| Archivo | Qué es |
|---|---|
| `about_info.gd` | **Copia maestra** de la pantalla «Acerca de» (autor IAnMove, `@theinaog` en X, `iaen.es/android`, ficha y privacidad de cada juego, catálogo de los demás juegos). Es idéntico en todos los juegos. |
| `sync_about.sh` | Reparte `about_info.gd` a cada juego (ruta de cada copia dentro del script). |
| `games.json` | Datos de las fichas web: nombre, slug, paquete, textos ES/EN, capturas, icono, `play_url`, `source_url`. |
| `make_web.py` | Genera en `~/customprograms/iaen-home` las páginas `android/<slug>/`, `android/<slug>/privacy/`, sus imágenes y las tarjetas de `android/index.html` e `index.html`. Necesita ImageMagick (`magick`). |
| `make_play.py` | Genera `publish/play/<slug>/`: ficha de Google Play (README, `ficha.json`, formato fastlane en `metadata/android/`, icono 512, imagen destacada 1024×500, capturas de teléfono) y el índice `play/README.md` + `manifest.json`. Acaba con un validador («0 problemas» salvo los juegos sin APK). |
| `sync_builds_repo.sh` | Copia `publish/play` (sin APK) al repo público `~/customprograms/android-builds` → https://github.com/IAnMove/android-builds ; con `--release` sube cada APK como release `<slug>-v<versión>`. |
| `prepare_android.py` | Deja un proyecto listo para Play: instala la plantilla Gradle (`android/build`), pone el preset «Android» en Gradle + AAB, paquete `es.iaen.<slug>`, target SDK 36 y arm64, mueve la clave de subida a `export_credentials.cfg` y completa el `.gitignore`. |
| `build_aab.sh <slug> <dir> …` | Llama a `prepare_android.py` y exporta el AAB de release firmado a `play/<slug>/<slug>.aab` (log en `publish/.tmp/<slug>.aab.log`). |
| `play/<slug>/<slug>.aab` | Android App Bundle de release. No se commitea: va a las releases del repo público. |
| `~/almacen/android-keys/` | **Claves de subida** (una por juego) y contraseñas. Fuera de git siempre; ver su README para la copia de seguridad. |

## Juegos (17 proyectos, slug = carpeta en `publish/play/` y en la web)

brasa, huerto (`puzzle-android`), pesca, gotic, ciudadmuerta (`mundoabierto`), timberfall, vialactea (`space/game`),
taberna (`taberna/Taberna`), villabellota (`animalcrossing`) y los de `newgames/games/`: isaac, minisims (`puzzle`),
randomsiege (`randomsiege_reload`), randomsiegev1 (copia anterior, solo en `play/`, no en la web ni en el catálogo
del «Acerca de»), siege, factorio (`factorio/godot`), xenara (`warcraf2/godot`), vuelvepronto (`souls/vuelve-pronto`).
`huerto-rama` es una rama de trabajo de Huerto (mismo paquete) y no cuenta. `skell-android` es el esqueleto.

## Dónde está el «Acerca de» en cada juego

| Juego | Dónde | Copia de `about_info.gd` |
|---|---|---|
| Skell, Brasa, Gotic, Pesca | MENÚ → ACERCA DE (`core/menu.gd`, junto a CRÉDITOS) | `core/about_info.gd` |
| Ciudad Muerta | Menú inicial y menú de pausa → Acerca de / About (`ui/menus.gd`, clave `menu.about`) | `core/about_info.gd` |
| Huerto | MENÚ → ACERCA DE (`main.gd`, `_open_about`) | `about_info.gd` |
| Timberfall | Menú → Ajustes → tarjeta «Acerca de» (`scripts/ui/panels/panel_settings.gd`) | `scripts/about_info.gd` |
| Via Lactea | Título y pausa → ACERCA DE (`game/scripts/menu.gd`, página `ACERCA`; sin lista de otros juegos, no cabe) | `game/scripts/about_info.gd` |
| Taberna | Ajustes → sección «Acerca de» al final (`scenes/settings/SettingsMenu.gd`, sigue el idioma del juego) | `Taberna/resources/about_info.gd` |
| Villa Bellota | MENÚ → ACERCA DE (esqueleto skell) | `core/about_info.gd` |
| Isaac Clone | Menú → ACERCA DE (estado `ABOUT` en `main.gd`, sigue el idioma) | `about_info.gd` |
| Mini Sims | Menú de pausa → Acerca de (menú contextual, `scripts/hud.gd`) | `scripts/about_info.gd` |
| Random Siege (y v1) | Título → «ACERCA DE» abajo a la izquierda → escena `scenes/about.tscn` | `scripts/about_info.gd` |
| Siege | Barra superior → botón «Acerca de» (ventana emergente, `scripts/hud.gd`) | `scripts/about_info.gd` |
| Factorio Clone | Menú / pausa → Acerca de (`ui.gd`) | `about_info.gd` |
| XENARA | Menú principal y pausa → Acerca de (`scripts/menus.gd`) | `scripts/about_info.gd` |
| Vuelve Pronto | Pantalla de idioma → enlaces «@theinaog» y «más juegos» (`scripts/title_screen.gd`) | `scripts/about_info.gd` |

Los juegos bilingües (Brasa, Ciudad Muerta, Taberna) enseñan la pantalla en el idioma activo; el resto, en español.
Los enlaces se abren con `OS.shell_open` (no hace falta permiso de internet); si no hay navegador se enseña la dirección.

## Cuando un juego salga en Google Play

1. En `about_info.gd`, pon la URL en `"play"` de ese juego dentro de `GAMES` (y `"source"` si hay repo público).
2. `publish/sync_about.sh` y vuelve a exportar los juegos (el botón «Google Play» pasa de apagado a activo en todos).
3. En `games.json`, pon la misma URL en `play_url` y ejecuta `python3 publish/make_web.py` desde `~/games`;
   revisa el repo `iaen-home` y commitea en una rama (todo lo que llega a `main` se publica solo).

Los slugs salen del nombre del juego en `project.godot` en minúsculas y sin espacios (con la tabla `SLUG_ALIASES`
de `about_info.gd` para «Isaac Clone», «Siege - Prototipo», «Factorio Clone» y «XENARA»); tienen que coincidir en
`about_info.gd`, `games.json`, la web y `publish/play/`.

## Pendiente conocido

- **siege** y **taberna** no exportan APK: Godot falla al leer archivos importados de GLB (`fseeko ... get_length`),
  de forma determinista (24 y 9 archivos). Sin resolver.
- Antes de cada subida a Play hay que subir `version/code` en el preset del juego.
- Correo de contacto público: pendiente. Nombres provisionales con marca: Isaac Clone, Mini Sims, Factorio Clone.
