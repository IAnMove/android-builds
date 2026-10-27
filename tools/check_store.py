#!/usr/bin/env python3
"""Valida una ficha de Google Play en formato fastlane supply según FICHA.md.

Uso:  tools/check_store.py <carpeta metadata/android> [--todos | --es-en]
      --todos  (por defecto en las apps) exige los 87 idiomas de Google Play
      --es-en  (los juegos, de momento) exige solo en-US y es-ES
Sale con código 1 si hay algún problema y acaba con «N problemas».

Comprueba, por idioma: title.txt (≤30), short_description.txt (≤80), full_description.txt (≤4000), que no estén
vacíos ni sean el texto en inglés sin traducir (salvo las variantes que se copian a propósito), palabras que Play
prohíbe en el título y la descripción breve, emojis y mayúsculas sostenidas; las capturas de
images/phoneScreenshots/ (2 a 8, PNG o JPEG, lados de 320 a 3840 px, proporción ≤2:1); y, en en-US,
images/icon.png (512×512) e images/featureGraphic.png (1024×500).
"""
import re
import struct
import sys
from pathlib import Path

# Idiomas de la ficha de Google Play con su código de fastlane supply.
# Las variantes marcadas con su origen son copia exacta de ese idioma (Play las indexa aparte, el texto es el mismo).
LANGS = {
    "af": "Afrikaans", "am": "Amharic", "ar": "Arabic", "az-AZ": "Azerbaijani", "be": "Belarusian",
    "bg": "Bulgarian", "bn-BD": "Bengali", "ca": "Catalan", "cs-CZ": "Czech", "da-DK": "Danish",
    "de-DE": "German", "el-GR": "Greek", "en-US": "English (US)", "es-ES": "Spanish (Spain)",
    "es-419": "Spanish (Latin America)", "et": "Estonian", "eu-ES": "Basque", "fa": "Persian",
    "fi-FI": "Finnish", "fil": "Filipino", "fr-FR": "French", "gl-ES": "Galician", "gu": "Gujarati",
    "hi-IN": "Hindi", "hr": "Croatian", "hu-HU": "Hungarian", "hy-AM": "Armenian", "id": "Indonesian",
    "is-IS": "Icelandic", "it-IT": "Italian", "iw-IL": "Hebrew", "ja-JP": "Japanese", "ka-GE": "Georgian",
    "kk": "Kazakh", "km-KH": "Khmer", "kn-IN": "Kannada", "ko-KR": "Korean", "ky-KG": "Kyrgyz", "lo-LA": "Lao",
    "lt": "Lithuanian", "lv": "Latvian", "mk-MK": "Macedonian", "ml-IN": "Malayalam", "mn-MN": "Mongolian",
    "mr-IN": "Marathi", "ms": "Malay", "my-MM": "Burmese", "ne-NP": "Nepali", "nl-NL": "Dutch",
    "no-NO": "Norwegian", "pa": "Punjabi", "pl-PL": "Polish", "pt-BR": "Portuguese (Brazil)",
    "pt-PT": "Portuguese (Portugal)", "rm": "Romansh", "ro": "Romanian", "ru-RU": "Russian",
    "si-LK": "Sinhala", "sk": "Slovak", "sl": "Slovenian", "sq": "Albanian", "sr": "Serbian",
    "sv-SE": "Swedish", "sw": "Swahili", "ta-IN": "Tamil", "te-IN": "Telugu", "th": "Thai", "tr-TR": "Turkish",
    "uk": "Ukrainian", "ur": "Urdu", "vi": "Vietnamese", "zh-CN": "Chinese (Simplified)",
    "zh-TW": "Chinese (Traditional)", "zu": "Zulu",
}
COPIES = {
    "en-AU": "en-US", "en-CA": "en-US", "en-GB": "en-US", "en-IN": "en-US", "en-SG": "en-US", "en-ZA": "en-US",
    "es-US": "es-419", "fr-CA": "fr-FR", "zh-HK": "zh-TW", "fa-AE": "fa", "fa-AF": "fa", "fa-IR": "fa",
    "ms-MY": "ms",
}
ALL = {**LANGS, **{k: f"copia de {v}" for k, v in COPIES.items()}}
DEFAULT = "en-US"
LIMITS = {"title.txt": 30, "short_description.txt": 80, "full_description.txt": 4000}
GRAPHICS = {"icon.png": (512, 512), "featureGraphic.png": (1024, 500)}
# Política de metadatos de Play: nada de precio, rango ni llamadas a la acción en el título ni en la breve.
BANNED = re.compile(r"(?i)(?<!\w)(free|gratis|gratuit[ao]s?|best|mejor|#1|top|nº ?1|no\. ?1|new|nuev[ao]|"
                    r"download|descarga|install|instala|sale|oferta|discount|descuento|hot)(?!\w)")
EMOJI = re.compile("[\U0001F300-\U0001FAFF☀-➿\U0001F000-\U0001F2FF]")


def png_jpeg_size(path):
    data = path.read_bytes()[:64 * 1024]
    if data[:8] == b"\x89PNG\r\n\x1a\n":
        return struct.unpack(">II", data[16:24])
    if data[:2] == b"\xff\xd8":
        i = 2
        while i < len(data) - 9:
            if data[i] != 0xFF:
                i += 1
                continue
            marker, length = data[i + 1], struct.unpack(">H", data[i + 2:i + 4])[0]
            if marker in (0xC0, 0xC1, 0xC2):
                h, w = struct.unpack(">HH", data[i + 5:i + 9])
                return w, h
            i += 2 + length
    return None


def check(root, required):
    problems = []
    def bad(lang, msg):
        problems.append(f"{lang}: {msg}")

    texts = {}
    for lang in sorted(required):
        d = root / lang
        if not d.is_dir():
            bad(lang, "falta la carpeta")
            continue
        texts[lang] = {}
        for name, limit in LIMITS.items():
            f = d / name
            if not f.is_file():
                bad(lang, f"falta {name}")
                continue
            t = f.read_text(encoding="utf-8").strip()
            texts[lang][name] = t
            if not t:
                bad(lang, f"{name} vacío")
            if len(t) > limit:
                bad(lang, f"{name} tiene {len(t)} caracteres (máx. {limit})")
            if name != "full_description.txt":
                if "\n" in t:
                    bad(lang, f"{name} tiene saltos de línea")
                m = BANNED.search(t)
                if m and lang.split("-")[0] in ("en", "es"):
                    bad(lang, f"{name} usa «{m.group(0)}» (política de metadatos de Play)")
            if EMOJI.search(t):
                bad(lang, f"{name} tiene emojis")
            if re.search(r"\b[A-ZÁÉÍÓÚÑ]{4,}(?:\s+[A-ZÁÉÍÓÚÑ]{4,}){3,}", t):
                bad(lang, f"{name} tiene frases enteras en MAYÚSCULAS")
        shots = sorted((d / "images" / "phoneScreenshots").glob("*")) if (d / "images" / "phoneScreenshots").is_dir() else []
        shots = [s for s in shots if s.suffix.lower() in (".png", ".jpg", ".jpeg")]
        if lang in (DEFAULT, "es-ES") and len(shots) < 2:
            bad(lang, f"{len(shots)} capturas (mín. 2 en en-US y es-ES)")
        if len(shots) > 8:
            bad(lang, f"{len(shots)} capturas (máx. 8)")
        for s in shots:
            size = png_jpeg_size(s)
            if not size:
                bad(lang, f"{s.name}: no es PNG ni JPEG")
                continue
            w, h = size
            if not (320 <= w <= 3840 and 320 <= h <= 3840) or max(w, h) > 2 * min(w, h):
                bad(lang, f"{s.name}: {w}×{h} fuera de lo que admite Play")
    for name, (w, h) in GRAPHICS.items():
        f = root / DEFAULT / "images" / name
        if not f.is_file():
            bad(DEFAULT, f"falta images/{name}")
        elif png_jpeg_size(f) != (w, h):
            bad(DEFAULT, f"images/{name} mide {png_jpeg_size(f)} (debe ser {w}×{h})")

    en = texts.get(DEFAULT, {})
    for lang, t in texts.items():
        src = COPIES.get(lang)
        if src:
            if src in texts and t != texts[src]:
                bad(lang, f"debe ser copia exacta de {src} (tools/check_store.py --copiar lo arregla)")
        elif lang != DEFAULT and en and t.get("full_description.txt") == en.get("full_description.txt"):
            bad(lang, "la descripción completa es la inglesa sin traducir")
    extra = [p.name for p in root.iterdir() if p.is_dir() and p.name not in ALL]
    for name in extra:
        bad(name, "carpeta con un código que Play no reconoce")
    return problems


def copy_variants(root):
    for dst, src in COPIES.items():
        s, d = root / src, root / dst
        if not s.is_dir():
            continue
        d.mkdir(exist_ok=True)
        for name in LIMITS:
            if (s / name).is_file():
                (d / name).write_text((s / name).read_text(encoding="utf-8"), encoding="utf-8")


def main(argv):
    args = [a for a in argv if not a.startswith("--")]
    if len(args) != 1:
        print(__doc__)
        return 2
    root = Path(args[0])
    if "--copiar" in argv:
        copy_variants(root)
    required = {DEFAULT, "es-ES"} if "--es-en" in argv else set(ALL)
    problems = check(root, required)
    for p in problems:
        print(p)
    print(f"{len(problems)} problemas ({len(required)} idiomas comprobados en {root})")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
