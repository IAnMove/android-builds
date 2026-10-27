# Cómo tiene que quedar cada ficha de Google Play

Estándar común para las apps y los juegos de IAnMove. Una ficha está bien cuando
`tools/check_store.py <carpeta metadata/android>` termina en **«0 problemas»**.

## Dónde vive
Formato [fastlane supply](https://docs.fastlane.tools/actions/supply/): `metadata/android/<idioma>/`.

| Qué | Carpeta de la ficha | Se genera con |
|---|---|---|
| Apps | `~/customprograms/android-apps/<carpeta>/store/metadata/android/` | a mano (agente), una por app |
| Juegos | `<slug>/metadata/android/` en este repo (copia de `~/games/publish/play/<slug>/`) | `python3 publish/make_play.py` desde `~/games`, con los textos de `~/games/publish/games.json` |

Cada idioma lleva `title.txt`, `short_description.txt` y `full_description.txt`. Solo en `en-US/images/`:
`icon.png` (512×512, PNG de 32 bits) y `featureGraphic.png` (1024×500). Capturas en
`<idioma>/images/phoneScreenshots/`: de 2 a 8, PNG o JPEG, lados de 320 a 3840 px, proporción ≤ 2:1, con prefijo
numérico (`1_main.png`…: el orden alfabético es el de Play). Obligatorias en `en-US` y `es-ES`; los demás idiomas
pueden no llevarlas (Play enseña las del idioma por defecto) o llevar las suyas si la interfaz está traducida.

## Idiomas
- **Apps: los 87 idiomas de Google Play.** 74 se traducen y 13 variantes son copia exacta de otro
  (`en-AU en-CA en-GB en-IN en-SG en-ZA` ← `en-US`, `es-US` ← `es-419`, `fr-CA` ← `fr-FR`, `zh-HK` ← `zh-TW`,
  `fa-AE fa-AF fa-IR` ← `fa`, `ms-MY` ← `ms`). Las copias las hace `tools/check_store.py <carpeta> --copiar`.
  La lista exacta de códigos está en `LANGS` y `COPIES` de `tools/check_store.py`.
- **Juegos: `en-US` y `es-ES`** por ahora (`check_store.py … --es-en`).
- Idioma por defecto de la ficha: `en-US`.
- `es-ES` en español de España («móvil»); `es-419` en español neutro de Latinoamérica («celular»); `pt-PT` en
  portugués de Portugal («telemóvel»), distinto de `pt-BR`.
- Las traducciones las escribe un modelo: hay que decirlo, no las ha revisado un nativo.

## Textos (ASO: lo que hace que te encuentren)
**Título (≤ 30):** `Nombre: palabra clave` en el idioma de la ficha, p. ej. `Gifea: creador de GIF`,
`Gifea: GIF Maker`, `Gifea: GIF 制作`. El nombre de la app, igual en todos los idiomas; la palabra clave, la que
la gente busca en ese idioma (no la traducción literal).

**Descripción breve (≤ 80):** qué hace y para quién, con la palabra clave principal y una secundaria. Sin punto
final de relleno.

**Descripción completa (≤ 4000, ideal 1500–2500):**
1. Primera frase (lo que se ve sin pulsar «más», ~170 caracteres): el beneficio principal con la palabra clave.
2. Bloques con título en una línea y viñetas `•`: cada función real, con las palabras que se buscan
   («comprimir vídeo», «reducir tamaño de foto», «GIF desde vídeo»…). Cada palabra clave importante, 2–4 veces
   en todo el texto, de forma natural.
3. Bloque de confianza con lo que sea verdad según el código: sin anuncios, sin cuentas, sin internet (solo si la
   app no tiene el permiso `INTERNET`), qué permisos pide y para qué, dónde se guardan los datos.
4. Pie: `Hecha por IAnMove · Más apps: https://iaen.es/android · X: @theinaog` (en juegos «Hecho» y
   «Más juegos»), traducido.

**Prohibido por la política de metadatos de Play** (el validador lo vigila en `en`/`es`; en el resto, cuidado
igual): precio o rango en el título y la breve (`gratis`, `free`, `mejor`, `best`, `#1`, `top`, `nuevo`,
`descarga`…), emojis, frases en MAYÚSCULAS, listas de palabras clave sueltas, testimonios inventados, nombres
de otras apps o marcas en el título y el icono. Una marca ajena solo en la descripción y solo para decir con qué
funciona (p. ej. «stickers para WhatsApp» en StikerMaker), nunca como si fuera suya. Nada que la app no haga.

## Imágenes
- `icon.png`: el icono de la app tal cual (primer plano + fondo del icono adaptativo), sin texto añadido.
- `featureGraphic.png`: fondo del color de la app, icono y nombre; sin texto pequeño, sin botones falsos, sin
  «descarga ya». Se genera con un script (en las apps, `tools/make_graphics.sh` como en Lupa).
- Capturas reales de la app en el emulador (ver `~/games/PLAY_PUBLISH_PROMPT.md`, sección 4): sin diálogos del
  sistema, sin barra de notificaciones con avisos, sin datos personales. Vertical 1080×1920 (horizontal
  1920×1080 si es un juego apaisado).
- Vídeo: solo como enlace de YouTube (`video.txt` en `en-US`), si hay.

## Lo que acompaña a la ficha (fuera de `metadata/`)
- **Apps:** `PRIVACY.md` (EN + ES, lo que de verdad hace el código) y `store/PLAY_CONSOLE.md` (tablas «campo →
  valor» para Play Console: categoría, correo `contacto@iaen.es`, web, privacidad, seguridad de los datos,
  clasificación, anuncios, público objetivo, permisos restringidos). Ejemplo terminado: `android-apps/lupa`.
- **Juegos:** `<slug>/README.md` y `<slug>/ficha.json` de este repo, generados.
- Política de privacidad publicada en `https://iaen.es/android/<slug>/privacy/` (ver `WEB.md`).
- Correo de contacto público de todas las fichas: **contacto@iaen.es**.
