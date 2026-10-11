# Publicación en Google Play: parte común de todos los juegos

Lo que comparten los juegos de `~/games` de cara a la tienda. Nada de aquí sale de esta máquina solo.

| Archivo | Qué es |
|---|---|
| `about_info.gd` | **Copia maestra** de la pantalla «Acerca de» (autor IAnMove, `@theinaog` en X, `iaen.es/android`, ficha y privacidad de cada juego, catálogo de los demás juegos). Es idéntico en todos los juegos. |
| `sync_about.sh` | Reparte `about_info.gd` a cada juego (ruta de cada copia dentro del script). |
| `games.json` | Datos de las fichas web: nombre, slug, paquete, textos ES/EN, capturas, icono, `play_url`, `source_url`. |
| `make_web.py` | Genera en `~/customprograms/iaen-home` las páginas `android/<slug>/`, `android/<slug>/privacy/`, sus imágenes y las tarjetas de `android/index.html` e `index.html`. Necesita ImageMagick (`magick`). |

## Dónde está el «Acerca de» en cada juego

| Juego | Dónde | Copia de `about_info.gd` |
|---|---|---|
| Skell, Brasa, Gotic, Pesca | MENÚ → ACERCA DE (`core/menu.gd`, junto a CRÉDITOS) | `core/about_info.gd` |
| Ciudad Muerta | Menú inicial y menú de pausa → Acerca de / About (`ui/menus.gd`, clave `menu.about`) | `core/about_info.gd` |
| Huerto | MENÚ → ACERCA DE (`main.gd`, `_open_about`) | `about_info.gd` |
| Timberfall | Menú → Ajustes → tarjeta «Acerca de» (`scripts/ui/panels/panel_settings.gd`) | `scripts/about_info.gd` |
| Via Lactea | Título y pausa → ACERCA DE (`game/scripts/menu.gd`, página `ACERCA`; sin lista de otros juegos, no cabe) | `game/scripts/about_info.gd` |
| Taberna | Ajustes → sección «Acerca de» al final (`scenes/settings/SettingsMenu.gd`, sigue el idioma del juego) | `Taberna/resources/about_info.gd` |

Los juegos bilingües (Brasa, Ciudad Muerta, Taberna) enseñan la pantalla en el idioma activo; el resto, en español.
Los enlaces se abren con `OS.shell_open` (no hace falta permiso de internet); si no hay navegador se enseña la dirección.

## Cuando un juego salga en Google Play

1. En `about_info.gd`, pon la URL en `"play"` de ese juego dentro de `GAMES` (y `"source"` si hay repo público).
2. `publish/sync_about.sh` y vuelve a exportar los juegos (el botón «Google Play» pasa de apagado a activo en todos).
3. En `games.json`, pon la misma URL en `play_url` y ejecuta `python3 publish/make_web.py` desde `~/games`;
   revisa el repo `iaen-home` y commitea en una rama (todo lo que llega a `main` se publica solo).

Los slugs (`brasa huerto pesca gotic ciudadmuerta timberfall vialactea taberna`) salen del nombre del juego en
`project.godot` en minúsculas y sin espacios; tienen que coincidir en `about_info.gd`, `games.json` y la web.
