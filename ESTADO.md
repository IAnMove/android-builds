# Estado de las apps y juegos Android para Google Play

Al día a 2026-10-28. Quien publique algo (ina o Grok) actualiza este archivo y el **Registro** del final.
Guía: [`GROK.md`](GROK.md) · ficha: [`FICHA.md`](FICHA.md) · web: [`WEB.md`](WEB.md).

Ya en Google Play: **CaptureCam** (`es.iaen.capturecam`) y **Pesca** (`es.iaen.pesca`).
Correo público de contacto: **contacto@iaen.es**.

## Pendiente para todas
1. **Crear cada app en Play Console y su primera subida**, a mano (la API no lo permite). Luego Grok puede subir
   fichas y versiones a las pistas de prueba (`GROK.md`, tarea D) cuando exista la cuenta de servicio.
2. **Prueba cerrada**: 12 testers apuntados 14 días seguidos por cada app nueva (cuenta personal). El mismo Grupo
   de Google de testers en todas = los 14 días corren a la vez.
3. **Web** (`IAnMove/home`, se publica al fusionar en `main`): ramas sin fusionar, hechas y subidas:
   - `android-anclas`: anclas `#apps` y `#juegos` del concentrador, a las que enlazan todos los «Acerca de».
   - `android-contacto`: `contacto@iaen.es` en las 36 políticas de privacidad (17 juegos, CaptureCam y Lupa).
   Las apps que no son Lupa ni CaptureCam aún no tienen página ni política publicada: Play exige la política
   antes de enviar (lo hace el paso A de `GROK.md`).
4. **Código fuente**: los «Acerca de» y las fichas dicen «software libre, Apache 2.0», pero ningún repo de apps o
   juegos es público. Decidir si se publican los repos (y rellenar `url_source`) o quitar esa frase.

## Apps (`~/customprograms/android-apps/<carpeta>`)
Hecho en las 9: «Acerca de» con «Más apps de @theinaog» → `iaen.es/android/#apps`, X, privacidad y licencia;
paquete `es.iaen.<slug>`; targetSdk 36; `LICENSE` + `NOTICE`; compilan y `lintDebug` sin errores; **ficha con
ASO en los 87 idiomas de Play** (`store/metadata/android/`, validada con `tools/check_store.py`), `PRIVACY.md` y
`store/PLAY_CONSOLE.md`. Nada probado aún en un móvil. Traducciones de un modelo, sin revisar por nativos.

Falta en todas menos Lupa (paso A de `GROK.md`, `run_grok.sh`): interfaz en 20 idiomas (hoy solo español, o
español e inglés; las fichas lo dicen, y hay que quitar esa frase cuando se traduzca), icono e imagen destacada,
capturas del emulador, AAB firmado y página web.

Diferencias entre fichas que hay que igualar al traducir las interfaces: las de Sonómetro, Duermevela, FotoFácil,
StikerMaker, Corregir y Explora dicen en los idiomas extranjeros que la app está en español (o español e inglés);
la de Gifea no lo dice; Lupa dice que la interfaz está en 20 idiomas. Gifea y Aligera no llevan la frase
«Apache 2.0» (las demás sí: ver el punto 4 de arriba).

| App | Carpeta | Paquete | Estado | Ojo con |
|---|---|---|---|---|
| Lupa | lupa | es.iaen.lupa | **lista para subir** | permiso de cámara |
| Gifea | gifcreator | es.iaen.gifea | ficha hecha | — |
| Aligera | image-video-compresor | es.iaen.aligera | ficha hecha | — |
| FotoFácil | photo-editor | es.iaen.fotofacil | ficha hecha | — |
| Sonómetro | medidordesonido | es.iaen.sonometro | ficha hecha | micrófono (no graba ni guarda audio) |
| StikerMaker | stickermaker | es.iaen.stikermaker | ficha hecha | probar en un móvil que WhatsApp acepta los packs (authority nueva); «WhatsApp» solo en la descripción |
| Duermevela | despertador | es.iaen.duermevela | ficha hecha | `USE_EXACT_ALARM` puede rechazarse (plan B en su `PLAY_CONSOLE.md`); vídeo del servicio en primer plano; `allowBackup=true` |
| Corregir | wordfixer | es.iaen.corregir | ficha hecha | usa internet (IA que elige el usuario); Play puede pedir un botón para denunciar contenido de IA y un aviso de consentimiento, que la app no tiene; el revisor necesitará una clave de API de prueba |
| Explora | android-explorer | es.iaen.explora | ficha hecha | permisos restringidos: acceso a todos los archivos e instalar paquetes (declaración tras la primera subida; puede pedir vídeo) |

Orden recomendado: Lupa → Gifea, Aligera, FotoFácil, Sonómetro, StikerMaker → Duermevela → Explora y Corregir.

## Juegos (`~/games`, fichas en este repo)
«Acerca de» común (copia maestra `~/games/publish/about_info.gd`): «Más juegos» → `iaen.es/android/#juegos`,
@theinaog, ficha, privacidad y catálogo de los demás juegos (Pesca con su botón de Google Play); al día en todos
menos Gotic y Taberna. Fichas ES/EN. AAB de los candidatos reexportados el 2026-10-27 (firma comprobada) en las
releases de este repo. Páginas web de los 17 ya publicadas en iaen.es.

| Juego | Slug | Estado | Ojo con |
|---|---|---|---|
| Pesca | pesca | **publicado** | próxima versión: subir versionCode |
| Brasa | brasa | listo | — |
| Huertecito | huerto | listo | — |
| Villa Bellota | villabellota | listo | — |
| Ciudad Muerta | ciudadmuerta | listo | — |
| Timberfall | timberfall | listo | — |
| Vía Láctea | vialactea | listo | solo 2 capturas (mejor 4–6) |
| XENARA | xenara | listo (0.2) | subir el tráiler a YouTube (no listado) y poner el enlace en `video.txt` |
| Gotic | gotic | listo, AAB por rehacer | lo mantiene otro agente; su `core/about_info.gd` es el viejo y el AAB del 27-oct también: actualizar, pasar `tests/run.sh` y reexportar antes de subir |

**No lanzar por ahora:** Random Siege y Random Siege v1 (calidad / duplicado), Siege y Taberna (la exportación
Android falla; Taberna en desarrollo en la rama `android-port`), Sótano Infinito (isaac), Mini Vidas (minisims;
muebles lowpoly ya en `main`), Fábrica Planetaria (factorio) y Vuelve Pronto: prototipos.

## Registro
| Fecha | Slug | Pista | versionCode | Nota |
|---|---|---|---|---|
