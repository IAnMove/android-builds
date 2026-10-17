# Juegos Android de IAnMove — fichas para Google Play

Una carpeta por juego con todo lo que pide Play Console: textos en español e inglés (`README.md`, `ficha.json` y
formato fastlane en `metadata/android/`), icono 512×512, imagen destacada 1024×500 y capturas de teléfono. Los AAB
(Android App Bundle de release, listos para subir a Play Console) están en las *releases* de este repositorio (una por
juego, etiqueta `<slug>-v<versión>`).

Autor: IAnMove · https://iaen.es/android · X: https://x.com/theinaog · Correo de contacto: PENDIENTE: correo público de contacto obligatorio en Play Console

| Juego | Paquete | Estado | Categoría | AAB |
|---|---|---|---|---|
| [Brasa](brasa/README.md) | `es.iaen.brasa` | publicable | Juegos › Acción | [AAB 27 MB](https://github.com/IAnMove/android-builds/releases/download/brasa-v1.0/brasa.aab) |
| [Huerto](huerto/README.md) | `es.iaen.huerto` | publicable | Juegos › Simulación | [AAB 28 MB](https://github.com/IAnMove/android-builds/releases/download/huerto-v1.0/huerto.aab) |
| [Pesca](pesca/README.md) | `es.iaen.pesca` | publicable | Juegos › Casual | [AAB 28 MB](https://github.com/IAnMove/android-builds/releases/download/pesca-v1.0/pesca.aab) |
| [Gotic](gotic/README.md) | `es.iaen.gotic` | publicable | Juegos › Aventura | [AAB 27 MB](https://github.com/IAnMove/android-builds/releases/download/gotic-v0.1/gotic.aab) |
| [Ciudad Muerta](ciudadmuerta/README.md) | `es.iaen.ciudadmuerta` | publicable | Juegos › Rol | [AAB 40 MB](https://github.com/IAnMove/android-builds/releases/download/ciudadmuerta-v0.1/ciudadmuerta.aab) |
| [Timberfall](timberfall/README.md) | `es.iaen.timberfall` | publicable | Juegos › Simulación | [AAB 38 MB](https://github.com/IAnMove/android-builds/releases/download/timberfall-v0.1.0/timberfall.aab) |
| [Via Lactea](vialactea/README.md) | `es.iaen.vialactea` | publicable | Juegos › Simulación | [AAB 27 MB](https://github.com/IAnMove/android-builds/releases/download/vialactea-v0.1/vialactea.aab) |
| [Taberna](taberna/README.md) | `es.iaen.taberna` | sin APK | Juegos › Simulación | [AAB 878 MB](https://github.com/IAnMove/android-builds/releases/download/taberna-v0.1.0/taberna.aab) |
| [Villa Bellota](villabellota/README.md) | `es.iaen.villabellota` | publicable | Juegos › Simulación | [AAB 26 MB](https://github.com/IAnMove/android-builds/releases/download/villabellota-v1.0/villabellota.aab) |
| [Sótano Infinito](isaac/README.md) | `es.iaen.isaac` | prototipo | Juegos › Acción | [AAB 56 MB](https://github.com/IAnMove/android-builds/releases/download/isaac-v0.1.0/isaac.aab) |
| [Mini Vidas](minisims/README.md) | `es.iaen.minisims` | prototipo | Juegos › Simulación | [AAB 39 MB](https://github.com/IAnMove/android-builds/releases/download/minisims-v0.1/minisims.aab) |
| [Random Siege](randomsiege/README.md) | `es.iaen.randomsiege` | prototipo | Juegos › Arcade | [AAB 40 MB](https://github.com/IAnMove/android-builds/releases/download/randomsiege-v0.1.0/randomsiege.aab) |
| [Random Siege v1](randomsiegev1/README.md) | `es.iaen.randomsiegev1` | duplicado | Juegos › Arcade | [AAB 40 MB](https://github.com/IAnMove/android-builds/releases/download/randomsiegev1-v0.1.0/randomsiegev1.aab) |
| [Asedio](siege/README.md) | `es.iaen.siege` | sin APK | Juegos › Estrategia | [AAB 490 MB](https://github.com/IAnMove/android-builds/releases/download/siege-v0.1.0/siege.aab) |
| [Fábrica Planetaria](factorio/README.md) | `es.iaen.factorio` | prototipo | Juegos › Estrategia | [AAB 46 MB](https://github.com/IAnMove/android-builds/releases/download/factorio-v0.1/factorio.aab) |
| [XENARA: Colonia Mecánica](xenara/README.md) | `es.iaen.xenara` | prototipo | Juegos › Estrategia | [AAB 73 MB](https://github.com/IAnMove/android-builds/releases/download/xenara-v0.1/xenara.aab) |
| [Vuelve Pronto](vuelvepronto/README.md) | `es.iaen.vuelvepronto` | prototipo | Juegos › Aventura | [AAB 37 MB](https://github.com/IAnMove/android-builds/releases/download/vuelvepronto-v0.1/vuelvepronto.aab) |

Estados: **publicable** (listo salvo lo pendiente abajo), **prototipo** (funciona pero sigue en desarrollo),
**duplicado** (copia anterior de otro juego: no publicar), **sin AAB** (la exportación falla hoy).

## Antes de publicar cualquiera

- Cada AAB va firmado con la **clave de subida** propia del juego (una por paquete, guardada fuera de GitHub); al crear
  la app en Play Console hay que aceptar Play App Signing. Paquetes definitivos `es.iaen.<slug>`, target SDK 36 (configurado en el preset), versionCode el del preset de cada juego.
- Correo de contacto público: PENDIENTE: correo público de contacto obligatorio en Play Console.
- Con una cuenta personal nueva hace falta una prueba cerrada con 12 probadores durante 14 días por cada app.
- Los juegos con **nombre provisional** (Isaac Clone, Mini Sims, Factorio Clone) deben cambiar de nombre: la
  propuesta está en su ficha.
- Las pistas de clasificación por edades son orientativas: el cuestionario IARC lo responde el desarrollador.

Generado el 2026-10-17 con `publish/make_play.py` desde `publish/games.json`.
