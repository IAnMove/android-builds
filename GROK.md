# Prompt para Grok (o cualquier agente): publicar en Google Play las apps y juegos de IAnMove

Responde en español. Trabajas en el ordenador de ina (Linux), con el CLI `grok` y aprobación automática: por eso
las reglas de abajo no son opcionales. Este archivo dice **dónde está todo** y **qué hacer**. Los estándares son
[`FICHA.md`](FICHA.md) (cómo tiene que quedar cada ficha de Play) y [`WEB.md`](WEB.md) (la página de cada app y juego
en iaen.es). Qué falta en cada una: [`ESTADO.md`](ESTADO.md). Al acabar cualquier tarea, actualiza `ESTADO.md`.

Cómo lanzarlo: `grok --cwd ~/customprograms/android-builds "Lee GROK.md y haz <tarea> de <app o juego>"`.

## 1. Dónde está todo
| Qué | Dónde |
|---|---|
| Este repo (fichas de los juegos, estándares, estado, validador) | `~/customprograms/android-builds` → github.com/IAnMove/android-builds (**público**: nada secreto aquí) |
| AAB de los juegos para subir a Play | releases de este repo (`<slug>-v<versión>`); copia local en `~/games/publish/play/<slug>/<slug>.aab` |
| Apps (código, ficha, privacidad, guía de Play Console) | `~/customprograms/android-apps/<carpeta>` → IAnMove/android-apps (privado). Ficha en `store/metadata/android/`, `PRIVACY.md`, `store/PLAY_CONSOLE.md`, AAB en `store/release/` |
| Ejemplo de app terminada | `~/customprograms/android-apps/lupa` (y `~/customprograms/capturecam-android`, ya en Play) |
| Juegos (código Godot) | `~/games/<carpeta>` y `~/games/newgames/games/<carpeta>`; tabla slug → carpeta en `~/games/publish/README.md` |
| Cadena de publicación de los juegos | `~/games/publish/` (**no está en git**): `games.json` (textos de las fichas), `about_info.gd` (copia maestra del «Acerca de») + `sync_about.sh`, `prepare_android.py`, `build_aab.sh`, `make_play.py`, `sync_builds_repo.sh` |
| Preparar una app con Grok (lanzador y encargo) | `~/games/publish/apps/run_grok.sh` y `~/games/publish/apps/BRIEF_TEMPLATE.md` |
| Estándar general de preparación | `~/games/PLAY_PUBLISH_PROMPT.md` |
| Web iaen.es | `~/customprograms/iaen-home` → IAnMove/home (privado; `main` se despliega solo) |
| Claves de subida (una por app o juego) | `~/almacen/android-keys/<slug>/` — **secreto**: de `upload.properties` solo puedes leer la línea `sha256=` |
| Clave de la API de Play (cuenta de servicio) | `~/almacen/play-api/service-account.json` (cuando ina la cree) — secreto |
| Godot y Android SDK | `~/games/Godot_v4.7.2-stable_linux.x86_64`, `~/Android/Sdk` (AVD `Medium_Phone_API_37.0`), Java en `~/.local/share/mise/installs/java/temurin-17` |

Correo público de contacto de todas las fichas: **contacto@iaen.es**. Autor IAnMove, X **@theinaog**, web
**https://iaen.es/android**. Paquetes `es.iaen.<slug>`, targetSdk 36.

## 2. Tareas
### A. Preparar una app (ficha, capturas, AAB, web)
`~/games/publish/apps/run_grok.sh "<slug>|<carpeta>|<Nombre>"` (sin argumentos, todas las pendientes, una tras otra).
Escribe `keystore.properties` sin enseñarte las contraseñas y te pasa el encargo `BRIEF_TEMPLATE.md`. Resultado:
interfaz en 20 idiomas, ficha según `FICHA.md` con `tools/check_store.py` en 0 problemas, capturas del emulador,
AAB firmado, página web en una rama de `iaen-home`, y un commit local en `android-apps`.

### B. Preparar un juego (AAB y ficha)
Desde `~/games`: `publish/sync_about.sh` (si cambió `about_info.gd`), `publish/build_aab.sh <slug> <carpeta>`,
`python3 publish/make_play.py` (debe decir «0 problemas») y `publish/sync_builds_repo.sh` (copia las fichas a este
repo; con `ONLY="<slug>" publish/sync_builds_repo.sh --release` sube el AAB a la release, solo si ina lo pide).
Comprueba la firma: `keytool -printcert -jarfile <aab>` = la línea `sha256=` de su `upload.properties`.
**Gotic** lo mantiene otro agente: no lo toques salvo que ina te lo diga.

### C. Página web
Según `WEB.md`, en una rama `android-<slug>` de `iaen-home`. Nunca en `main`.

### D. Subir a Google Play (pistas de prueba)
Solo para apps o juegos que ina te diga que ya ha creado en Play Console (ver sección 3).
Requisitos: `fastlane --version` (si falta, `gem install --user-install fastlane`) y la clave de la cuenta de
servicio (`fastlane run validate_play_store_json_key json_key:~/almacen/play-api/service-account.json`).
1. Firma del AAB comprobada (como en B).
2. `versionCode` mayor que el de Play:
   `fastlane run google_play_track_version_codes package_name:es.iaen.<slug> track:alpha json_key:...`.
   Si no lo es, súbelo en el proyecto (preset de Godot `version/code` o `versionCode` de Gradle), recompila y
   commitea ese cambio en su repo (sin push).
3. Subida a la **prueba cerrada**:
   ```
   fastlane supply --json_key ~/almacen/play-api/service-account.json --package_name es.iaen.<slug> \
     --aab <aab> --track alpha --release_status completed \
     --metadata_path <carpeta metadata/android> --skip_upload_changelogs true
   ```
   Apps: `metadata_path` = `~/customprograms/android-apps/<carpeta>/store/metadata/android`.
   Juegos: `metadata_path` = `~/customprograms/android-builds/<slug>/metadata/android`.
   Si Play rechaza un texto o una imagen, arregla la ficha (y vuelve a pasar `tools/check_store.py`), no el código.
4. Apunta en `ESTADO.md` (Registro) fecha, slug, pista y versionCode, y commitea en este repo (sin push).
5. Cuando ina diga que una ya está en producción: su URL de Play en `play` de `~/games/publish/about_info.gd`
   (juegos, y luego `publish/sync_about.sh`) o en su página y `links.xml` (apps), en `play_url` de `games.json`, en su
   página web (rama de `iaen-home`) y en `ESTADO.md`.

## 3. Lo que hace ina a mano en https://play.google.com/console
La API de Play no permite crear apps ni rellenar las declaraciones, y la primera subida tiene que ser a mano:
1. Crear la app (nombre, idioma por defecto inglés, App o Juego, Gratis, aceptar las declaraciones).
2. Subir el primer AAB en Pruebas → Prueba interna (activa la firma de apps de Play).
3. Contenido de la app: política de privacidad, acceso, anuncios, clasificación IARC, público objetivo, seguridad
   de los datos, permisos restringidos. Las respuestas: `store/PLAY_CONSOLE.md` (apps) o `<slug>/README.md` (juegos).
4. Prueba cerrada con el grupo de testers (12 o más, 14 días seguidos; el mismo grupo en todas las apps hace que
   los 14 días corran a la vez) y, al acabar, «Solicitar acceso a producción».

Preparación única de la API (si falta, explícasela a ina): Google Cloud Console → proyecto → activar «Google Play
Android Developer API» → cuenta de servicio → clave JSON en `~/almacen/play-api/service-account.json` (`chmod 600`,
con copia de seguridad) → en Play Console, Usuarios y permisos → invitar a la cuenta de servicio con «Publicar en
pistas de prueba» y «Gestionar presencia en Play Store», **sin** «Publicar en producción».

## 4. Prohibido
- Subir a **producción** o enviar a revisión de producción. Solo `internal` y `alpha`.
- `git push`, crear repos, tocar `main` de `iaen-home`.
- Mostrar, copiar o commitear contraseñas, la clave JSON, `keystore.properties`, `.jks` o `.keystore`. Este repo es
  público: antes de cada commit, `git diff --cached` y busca secretos y rutas con datos personales.
- Tocar el móvil físico de ina (ADB inalámbrico). Si hace falta un dispositivo, el emulador `emulator-5554`.
- Añadir anuncios, analíticas, compras o permisos nuevos, o cambiar lo que hace una app o un juego.
- Publicar lo que `ESTADO.md` marca como «no lanzar» aunque tenga AAB.
- Inventar: si algo no se puede saber del código o de estos archivos, pregúntaselo a ina en una sola tanda.

## 5. Al acabar
Resumen corto: qué hiciste, rutas, hashes de commit, lo que no pudiste verificar, y los pasos que le tocan a ina.
