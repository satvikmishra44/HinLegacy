import re


def krutidev_to_unicode(src: str) -> str:
    """
    Convert text in KrutiDev / Walkman Chanakya 905 legacy encoding to Unicode Devanagari.
    Ported from the public Walkman Chanakya905 converter.
    """
    if not src:
        return ""

    out = src

    array_one = [
        "ñ","Q+Z","sas","aa",")Z","ZZ","‘","’","“","”",
        "å",  "ƒ",  "„",   "…",   "†",   "‡",   "ˆ",   "‰",   "Š",   "‹",
        "¶+",   "d+", "[+k","[+", "x+",  "T+",  "t+", "M+", "<+", "Q+", ";+", "j+", "u+",
        "Ùk", "Ù", "Dr", "–", "—","é","™","=kk","f=k",
        "à",   "á",    "â",   "ã",   "ºz",  "º",   "í", "{k", "{", "=",  "«",
        "Nî",   "Vî",    "Bî",   "Mî",   "<î", "|", "K", "}",
        "J",   "Vª",   "Mª",  "<ªª",  "Nª",   "Ø",  "Ý", "nzZ",  "æ", "ç", "Á", "xz", "#", ":",
        "v‚","vks",  "vkS",  "vk",    "v",  "b±", "Ã",  "bZ",  "b",  "m",  "Å",  ",s",  ",",   "_",
        "ô",  "d", "Dk", "D", "[k", "[", "x","Xk", "X", "Ä", "?k", "?",   "³",
        "pkS",  "p", "Pk", "P",  "N",  "t", "Tk", "T",  ">", "÷", "¥",
        "ê",  "ë",   "V",  "B",   "ì",   "ï", "M+", "<+", "M",  "<", ".k", ".",
        "r",  "Rk", "R",   "Fk", "F",  ")", "n", "/k", "èk",  "/", "Ë", "è", "u", "Uk", "U",
        "i",  "Ik", "I",   "Q",    "¶",  "c", "Ck",  "C",  "Hk",  "H", "e", "Ek",  "E",
        ";",  "¸",   "j",    "y", "Yk",  "Y",  "G",  "o", "Ok", "O",
        "'k", "'",   "\"k",  "\"",  "l", "Lk",  "L",   "g",
        "È", "z",
        "Ì", "Í", "Î",  "Ï",  "Ñ",  "Ò",  "Ó",  "Ô",   "Ö",  "Ø",  "Ù","Ük", "Ü",
        "‚",    "ks",   "kS",   "k",  "h",    "q",   "w",   "`",    "s",    "S",
        "a",    "¡",    "%",     "W",  "•", "·", "∙", "·", "~j",  "~", "\\","+"," ः",
        "^", "*",  "Þ", "ß", "(", "¼", "½", "¿", "À", "¾", "A", "-", "&", "&", "Œ", "]","~ ","@"
    ]

    array_two = [
        "॰","QZ+","sa","a","र्द्ध","Z","\"","\"","'","'",
        "०",  "१",  "२",  "३",     "४",   "५",  "६",   "७",   "८",   "९",
        "फ़्",  "क़",  "ख़", "ख़्",  "ग़", "ज़्", "ज़",  "ड़",  "ढ़",   "फ़",  "य़",  "ऱ",  "ऩ",
        "त्त", "त्त्", "क्त",  "दृ",  "कृ","nn","nnd","=k","f=",
        "ह्न",  "ह्य",  "हृ",  "ह्म",  "ह्र",  "ह्",   "द्द",  "क्ष", "क्ष्", "त्र", "त्र्",
        "छ्य",  "ट्य",  "ठ्य",  "ड्य",  "ढ्य", "द्य", "ज्ञ", "द्व",
        "श्र",  "ट्र",    "ड्र",    "ढ्र",    "छ्र",   "क्र",  "फ्र", "र्द्र",  "द्र",   "प्र", "प्र",  "ग्र", "रु",  "रू",
        "ऑ",   "ओ",  "औ",  "आ",   "अ", "ईं", "ई",  "ई",   "इ",  "उ",   "ऊ",  "ऐ",  "ए", "ऋ",
        "क्क", "क", "क", "क्", "ख", "ख्", "ग", "ग", "ग्", "घ", "घ", "घ्", "ङ",
        "चै",  "च", "च", "च्", "छ", "ज", "ज", "ज्",  "झ",  "झ्", "ञ",
        "ट्ट",   "ट्ठ",   "ट",   "ठ",   "ड्ड",   "ड्ढ",  "ड़", "ढ़", "ड",   "ढ", "ण", "ण्",
        "त", "त", "त्", "थ", "थ्",  "द्ध",  "द", "ध", "ध", "ध्", "ध्", "ध्", "न", "न", "न्",
        "प", "प", "प्",  "फ", "फ्",  "ब", "ब", "ब्",  "भ", "भ्",  "म",  "म", "म्",
        "य", "य्",  "र", "ल", "ल", "ल्",  "ळ",  "व", "व", "व्",
        "श", "श्",  "ष", "ष्", "स", "स", "स्", "ह",
        "ीं", "्र",
        "द्द", "ट्ट","ट्ठ","ड्ड","कृ","भ","्य","ड्ढ","झ्","क्र","त्त्","श","श्",
        "ॉ",  "ो",   "ौ",   "ा",   "ी",   "ु",   "ू",   "ृ",   "े",   "ै",
        "ं",   "ँ",   "ः",   "ॅ",  "ऽ", "ऽ", "ऽ", "ऽ", "्र",  "्", "?", "़",":",
        "‘",   "’",   "“",   "”",  ";",  "(",    ")",   "{",    "}",   "=", "।", ".", "-",  "µ", "॰", ",","् ","/"
    ]

    # Move 'f' (short-i placeholder) to correct position, then convert to 'ि'
    out = "  " + out + "  "
    position_of_f = out.rfind("f")
    while position_of_f != -1:
        # swap 'f' with the char to its right
        out = (
            out[:position_of_f]
            + out[position_of_f + 1]
            + "f"
            + out[position_of_f + 2:]
        )
        position_of_f = out.rfind("f", 0, position_of_f)

    out = out.replace("f", "ि")
    out = out.strip()

    # Move half-R ('Z') correctly relative to matras
    out = "  " + out + "  "
    position_of_r = out.find("Z")
    set_of_matras = [
        "‚", "ks", "kS", "k", "h", "q", "w", "`", "s", "S",
        "a", "¡", "%", "W", "·", "∙", "·", "~j", "~", "\\", "+", " ः"
    ]

    while position_of_r != -1:
        # remove the Z
        out = out.replace("Z", "", 1)
        # check preceding chars for matras
        prev_char = out[position_of_r - 1]
        if prev_char and prev_char in set_of_matras:
            # insert reph before the matra cluster
            out = out[:position_of_r - 2] + "र्" + "~" + out[position_of_r - 2:]
        else:
            out = out[:position_of_r - 1] + "र्" + "~" + out[position_of_r - 1:]
        position_of_r = out.find("Z")

    out = out.strip()

    # ASCII -> Unicode replacements
    for i in range(len(array_one)):
        key = array_one[i]
        if not key:
            continue
        # escape regex specials if any, but we're doing simple .replace, so no regex
        out = out.replace(key, array_two[i])

    # Final cleanups for 'nn'/'nnd'
    out = out.replace("nn", "न्न")
    out = out.replace("nnd", "न्न्")

    return out


def unicode_to_krutidev(src: str) -> str:
    """
    Convert Unicode Devanagari text to KrutiDev / Walkman Chanakya 905 legacy encoding.
    Ported from the same converter. [web:5]
    """
    if not src:
        return ""

    out = src

    # Normalize two-byte nuqta forms to single-byte variants
    out = out.replace("क़", "क़")
    out = out.replace("ख़", "ख़")
    out = out.replace("ग़", "ग़")
    out = out.replace("ज़", "ज़")
    out = out.replace("ड़", "ड़")
    out = out.replace("ढ़", "ढ़")
    out = out.replace("n़", "ऩ")
    out = out.replace("फ़", "फ़")
    out = out.replace("य़", "य़")
    out = out.replace("ऱ", "ऱ")

    # Rearrange post-consonant short-i matra: move 'ि' before cluster
    # /(([क-हक़-य़]़?्)*[क-हक़-य़]़?)ि/ → 'ि$1'
    pattern_i = re.compile(r'((?:[क-हक़-य़]़?्)*[क-हक़-य़]़?)ि')
    out = pattern_i.sub(r'ि\1', out)

    # Rearrange reph 'र्' → push to end of cluster + matras, then mark with Z
    # /र्(([क-हक़-य़]़?्)*[क-हक़-य़]़?)([ाीेैोौूंँःॅ]*)/ → '$1$3Z'
    pattern_reph = re.compile(
        r'र्((?:[क-हक़-य़]़?्)*[क-हक़-य़]़?)([ाीेैोौूंँःॅ]*)'
    )
    out = pattern_reph.sub(r'\1\2Z', out)

    # Short-i placeholder
    out = out.replace("ि", "f")

    array_one = [
        "‘",   "’",   "“",   "”",   "(",    ")",   "{",    "}",   "=", "।",  "?",  "-",  "µ", "॰", ",", ".", "् ",
        "०",  "१",  "२",  "३",     "४",   "५",  "६",   "७",   "८",   "९", "x",
        "फ़्",  "क़",  "ख़",  "ग़", "ज़्", "ज़",  "ड़",  "ढ़",   "फ़",  "य़",  "ऱ",  "ऩ",
        "त्त्",   "त्त",     "क्त",  "दृ",  "कृ",
        "ह्न",  "ह्य",  "हृ",  "ह्म",  "ह्र",  "ह्",   "द्द",  "क्ष्", "क्ष", "त्र्", "त्र","ज्ञ",
        "छ्य",  "ट्य",  "ठ्य",  "ड्य",  "ढ्य", "द्य","द्व",
        "श्र",  "ट्र",    "ड्र",    "ढ्र",    "छ्र",   "क्र",  "फ्र",  "द्र",   "प्र",   "ग्र", "रु",  "रू",
        "्र",
        "ओ",  "औ",  "आ",   "अ",   "ई",   "इ",  "उ",   "ऊ",  "ऐ",  "ए", "ऋ",
        "क्",  "क",  "क्क",  "ख्",   "ख",    "ग्",   "ग",  "घ्",  "घ",    "ङ",
        "चै",   "च्",   "च",   "छ",  "ज्", "ज",   "झ्",  "झ",   "ञ",
        "ट्ट",   "ट्ठ",   "ट",   "ठ",   "ड्ड",   "ड्ढ",  "ड",   "ढ",  "ण्", "ण",
        "त्",  "त",  "थ्", "थ",  "द्ध",  "द", "ध्", "ध",  "न्",  "न",
        "प्",  "प",  "फ्", "फ",  "ब्",  "ब", "भ्",  "भ",  "म्",  "म",
        "य्",  "य",  "र",  "ल्", "ल",  "ळ",  "व्",  "व",
        "श्", "श",  "ष्", "ष",  "स्",   "स",   "ह",
        "ऑ",   "ॉ",  "ो",   "ौ",   "ा",   "ी",   "ु",   "ू",   "ृ",   "े",   "ै",
        "ं",   "ँ",   "ः",   "ॅ",    "ऽ",  "् ", "्"
    ]

    array_two = [
        "^", "*",  "Þ", "ß", "¼", "½", "¿", "À", "¾", "A", "\\", "&", "&", "Œ", "]","-","~ ",
        "å",  "ƒ",  "„",   "…",   "†",   "‡",   "ˆ",   "‰",   "Š",   "‹","Û",
        "¶",   "d",    "[k",  "x",  "T",  "t",   "M+", "<+", "Q",  ";",    "j",   "u",
        "Ù",   "Ùk",   "Dr",    "–",   "—",
        "à",   "á",    "â",   "ã",   "ºz",  "º",   "í", "{", "{k",  "«", "=","K",
        "Nî",   "Vî",    "Bî",   "Mî",   "<î", "|","}",
        "J",   "Vª",   "Mª",  "<ªª",  "Nª",   "Ø",  "Ý",   "æ", "ç", "xz", "#", ":",
        "z",
        "vks",  "vkS",  "vk",    "v",   "bZ",  "b",  "m",  "Å",  ",s",  ",",   "_",
        "D",  "d",    "ô",     "[",     "[k",    "X",   "x",  "?",    "?k",   "³",
        "pkS",  "P",    "p",  "N",   "T",    "t",   "÷",  ">",   "¥",
        "ê",      "ë",      "V",  "B",   "ì",       "ï",     "M",  "<",  ".", ".k",
        "R",  "r",   "F", "Fk",  ")",    "n", "/",  "/k",  "U", "u",
        "I",  "i",   "¶", "Q",   "C",  "c",  "H",  "Hk", "E",   "e",
        "¸",   ";",    "j",  "Y",   "y",  "G",  "O",  "o",
        "'", "'k",  "\"", "\"k", "L",   "l",   "g",
        "v‚",    "‚",    "ks",   "kS",   "k",     "h",    "q",   "w",   "`",    "s",    "S",
        "a",    "¡",    "%",     "W",   "·",   "~ ", "~"
    ]

    # Replace Unicode with ASCII using mapping arrays
    for i in range(len(array_one)):
        key = array_one[i]
        val = array_two[i]
        if not key:
            continue
        # simple global replacement
        out = out.replace(key, val)

    # Reph + Anusvara combined replacement
    out = out.replace("Zं", "±")
    out = out.replace("ंZ", "±")

    return out


def walkman_chanakya905_to_unicode(src: str) -> str:
    """
    Walkman-Chanakya905Normal (Type1, WinAnsiEncoding) -> Unicode Devanagari.
    This matches the way the public Walkman Chanakya905 converter treats
    Chanakya/Walkman glyphs: first remap a few glyphs, then use KrutiDev mapping.
    """
    if not src:
        return ""

    out = src

    # Chanakya/Walkman-specific glyph substitutions before KrutiDev conversion
    out = out.replace("]", "न")
    out = out.replace("[", "क")
    out = out.replace("}", "द्व")
    out = out.replace("|", "द्य")
    out = out.replace("«", "त्र्")
    out = out.replace("=", "त्र")
    out = out.replace("J", "श्र")

    # Then run through KrutiDev -> Unicode mapping
    return krutidev_to_unicode(out)


def unicode_to_walkman_chanakya905(src: str) -> str:
    """
    Unicode Devanagari -> Walkman-Chanakya905Normal encoding.
    Uses Unicode->KrutiDev, then applies Chanakya/Walkman-specific glyph substitutions. [web:5]
    """
    if not src:
        return ""

    out = unicode_to_krutidev(src)

    # Map KrutiDev codes to Chanakya/Walkman glyphs
    out = out.replace("u", "]")
    out = out.replace("d", "[")
    out = out.replace("द्व", "}")
    out = out.replace("द्य", "|")

    return out

if __name__ == "__main__":
    text = input("Enter your text:")
    print(walkman_chanakya905_to_unicode(text))