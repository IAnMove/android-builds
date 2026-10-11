# Juegos Android de IAnMove — fichas para Google Play

Una carpeta por juego con todo lo que pide Play Console: textos en español e inglés (`README.md`, `ficha.json` y
formato fastlane en `metadata/android/`), icono 512×512, imagen destacada 1024×500 y capturas de teléfono. Los APK
están en las *releases* de este repositorio (una por juego, etiqueta `<slug>-v<versión>`).

Autor: IAnMove · https://iaen.es/android · X: https://x.com/theinaog · Correo de contacto: PENDIENTE: correo público de contacto obligatorio en Play Console

| Juego | Paquete | Estado | Categoría | APK |
|---|---|---|---|---|
| [Brasa](brasa/README.md) | `com.ina.brasa` | publicable | Juegos › Acción | [APK 57 MB](https://github.com/IAnMove/android-builds/releases/download/brasa-v1.0/brasa.apk) |
| [Huerto](huerto/README.md) | `com.ina.huerto` | publicable | Juegos › Simulación | [APK 58 MB](https://github.com/IAnMove/android-builds/releases/download/huerto-v1.0/huerto.apk) |
| [Pesca](pesca/README.md) | `com.ina.pesca` | publicable | Juegos › Casual | [APK 58 MB](https://github.com/IAnMove/android-builds/releases/download/pesca-v1.0/pesca.apk) |
| [Gotic](gotic/README.md) | `com.ina.gotic` | publicable | Juegos › Aventura | [APK 57 MB](https://github.com/IAnMove/android-builds/releases/download/gotic-v0.1/gotic.apk) |
| [Ciudad Muerta](ciudadmuerta/README.md) | `com.ina.ciudadmuerta` | publicable | Juegos › Rol | [APK 69 MB](https://github.com/IAnMove/android-builds/releases/download/ciudadmuerta-v0.1/ciudadmuerta.apk) |
| [Timberfall](timberfall/README.md) | `com.ianmove.timberfall` | publicable | Juegos › Simulación | [APK 40 MB](https://github.com/IAnMove/android-builds/releases/download/timberfall-v0.1.0/timberfall.apk) |
| [Via Lactea](vialactea/README.md) | `org.ina.vialactea` | publicable | Juegos › Simulación | [APK 29 MB](https://github.com/IAnMove/android-builds/releases/download/vialactea-v0.1/vialactea.apk) |
| [Taberna](taberna/README.md) | `com.ina.taberna` | sin APK | Juegos › Simulación | sin APK |
| [Villa Bellota](villabellota/README.md) | `com.ina.villabellota` | publicable | Juegos › Simulación | [APK 56 MB](https://github.com/IAnMove/android-builds/releases/download/villabellota-v1.0/villabellota.apk) |
| [Sótano Infinito](isaac/README.md) | `com.ina.isaac` | prototipo | Juegos › Acción | [APK 58 MB](https://github.com/IAnMove/android-builds/releases/download/isaac-v0.1.0/isaac.apk) |
| [Mini Vidas](minisims/README.md) | `com.ina.minisims` | prototipo | Juegos › Simulación | [APK 41 MB](https://github.com/IAnMove/android-builds/releases/download/minisims-v0.1/minisims.apk) |
| [Random Siege](randomsiege/README.md) | `com.ina.randomsiege` | prototipo | Juegos › Arcade | [APK 42 MB](https://github.com/IAnMove/android-builds/releases/download/randomsiege-v0.1.0/randomsiege.apk) |
| [Random Siege v1](randomsiegev1/README.md) | `com.ina.randomsiegev1` | duplicado | Juegos › Arcade | [APK 42 MB](https://github.com/IAnMove/android-builds/releases/download/randomsiegev1-v0.1.0/randomsiegev1.apk) |
| [Asedio](siege/README.md) | `com.ina.siege` | sin APK | Juegos › Estrategia | sin APK |
| [Fábrica Planetaria](factorio/README.md) | `com.ina.factorio` | prototipo | Juegos › Estrategia | [APK 48 MB](https://github.com/IAnMove/android-builds/releases/download/factorio-v0.1/factorio.apk) |
| [XENARA: Colonia Mecánica](xenara/README.md) | `com.ina.xenara` | prototipo | Juegos › Estrategia | [APK 75 MB](https://github.com/IAnMove/android-builds/releases/download/xenara-v0.1/xenara.apk) |
| [Vuelve Pronto](vuelvepronto/README.md) | `com.ina.vuelvepronto` | prototipo | Juegos › Aventura | [APK 39 MB](https://github.com/IAnMove/android-builds/releases/download/vuelvepronto-v0.1/vuelvepronto.apk) |

Estados: **publicable** (listo salvo lo pendiente abajo), **prototipo** (funciona pero sigue en desarrollo),
**duplicado** (copia anterior de otro juego: no publicar), **sin APK** (la exportación falla hoy).

## Antes de publicar cualquiera

- Play Console exige un **Android App Bundle (.aab)** firmado con una clave de subida para producción; los APK de
  aquí son de depuración y sirven para *internal app sharing*; para los tracks de prueba de una app nueva hace falta el AAB.
- Correo de contacto público: PENDIENTE: correo público de contacto obligatorio en Play Console.
- Con una cuenta personal nueva hace falta una prueba cerrada con 12 probadores durante 14 días por cada app.
- Los juegos con **nombre provisional** (Isaac Clone, Mini Sims, Factorio Clone) deben cambiar de nombre: la
  propuesta está en su ficha.
- Las pistas de clasificación por edades son orientativas: el cuestionario IARC lo responde el desarrollador.

Generado el 2026-10-11 con `publish/make_play.py` desde `publish/games.json`.
