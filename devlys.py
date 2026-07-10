from typing import List

DEVLYS_TO_UNICODE_SOURCE: List[str] = [
    "ñ","Q+Z","sas","aa",")Z","ZZ","‘","’","“","”",
    "å","ƒ","„","…","†","‡","ˆ","‰","Š","‹",
    "¶+","d+","[+k","[+","x+","T+","t+","M+","<+","Q+",";+","j+","u+",
    "Ùk","Ù","ä","–","—","é","™","=kk","f=k",
    "à","á","â","ã","ºz","º","í","{k","{","=","«",
    "Nî","Vî","Bî","Mî","<î","|","K","}",
    "J","Vª","Mª","<ªª","Nª","Ø","Ý","nzZ","æ","ç","Á","xz","#",":",
    "v‚","vks","vkS","vk","v","b±","Ã","bZ","b","m","Å",",s",",","_",
    "ô","d","Dk","D","£","[k","[","x","Xk","X","Ä","?k","?","³",
    "p","Pk","P","N","t","Tk","T",">","÷","¥",
    "ê","ë","V","B","ì","ï","M+","<+","M","<",".k",".",
    "r","Rk","R","Fk","F",")","n","/k","èk","/","Ë","è","u","Uk","U",
    "i","Ik","I","Q","¶","c","Ck","C","Hk","H","e","Ek","E",
    ";","¸","j","y","Yk","Y","G","o","Ok","O",
    "'k","'","\"k","\"","l","Lk","L","g",
    "È","z",
    "Ì","Í","Î","Ï","Ñ","Ò","Ó","Ô","Ö","Ø","Ù","Ük","Ü",
    "‚","¨","ks","©","kS","k","h","q","w","`","s","¢","S",
    "a","¡","%","W","•","·","∙","·","~j","~","\\","+"," ः",
    "^","*","Þ","ß","(","¼","½","¿","À","¾","A","-","&","&","Œ","]","~ ","@",
    "ाे","ाॅ","ंै","े्र","अौ","अो","आॅ"
]

DEVLYS_TO_UNICODE_TARGET: List[str] = [
    "॰","QZ+","sa","a","र्द्ध","Z","\"","\"","'","'",
    "०","१","२","३","४","५","६","७","८","९",
    "फ़्","क़","ख़","ख़्","ग़","ज़्","ज़","ड़","ढ़","फ़","य़","ऱ","ऩ",
    "त्त","त्त्","क्त","दृ","कृ","न्न","न्न्","=k","f=",
    "ह्न","ह्य","हृ","ह्म","ह्र","ह्","द्द","क्ष","क्ष्","त्र","त्र्",
    "छ्य","ट्य","ठ्य","ड्य","ढ्य","द्य","ज्ञ","द्व",
    "श्र","ट्र","ड्र","ढ्र","छ्र","क्र","फ्र","र्द्र","द्र","प्र","प्र","ग्र","रु","रू",
    "ऑ","ओ","औ","आ","अ","ईं","ई","ई","इ","उ","ऊ","ऐ","ए","ऋ",
    "क्क","क","क","क्","ख","ख","ख्","ग","ग","ग्","घ","घ","घ्","ङ",
    "च","च","च्","छ","ज","ज","ज्","झ","झ्","ञ",
    "ट्ट","ट्ठ","ट","ठ","ड्ड","ड्ढ","ड़","ढ़","ड","ढ","ण","ण्",
    "त","त","त्","थ","थ्","द्ध","द","ध","ध","ध्","ध्","ध्","न","न","न्",
    "प","प","प्","फ","फ्","ब","ब","ब्","भ","भ्","म","म","म्",
    "य","य्","र","ल","ल","ल्","ळ","व","व","व्",
    "श","श्","ष","ष्","स","स","स्","ह",
    "ीं","्र",
    "द्द","ट्ट","ट्ठ","ड्ड","कृ","भ","्य","ड्ढ","झ्","क्र","त्त्","श","श्",
    "ॉ","ो","ो","ौ","ौ","ा","ी","ु","ू","ृ","े","े","ै",
    "ं","ँ","ः","ॅ","ऽ","ऽ","ऽ","ऽ","्र","्","?","़",":",
    "‘","’","“","”",";","(",")","{","}","=","।",".","-","µ","॰",",","् ","/",
    "ो","ॉ","ैं","्रे","औ","ओ","ऑ"
]

UNICODE_TO_DEVLYS_SOURCE: List[str] = [
    "‘","’","“","”","(",")","{","}","=","।","?","-","µ","॰",",",".","् ",
    "०","१","२","३","४","५","६","७","८","९","x","+",";","_",
    "फ़्","क़","ख़","ग़","ज़्","ज़","ड़","ढ़","फ़","य़","ऱ","ऩ",
    "त्त्","त्त","क्त","दृ","कृ",
    "श्व","ह्न","ह्य","हृ","ह्म","ह्र","ह्","द्द","क्ष्","क्ष","त्र्","त्र","ज्ञ",
    "छ्य","ट्य","ठ्य","ड्य","ढ्य","द्य","द्व",
    "श्र","ट्र","ड्र","ढ्र","छ्र","क्र","फ्र","द्र","प्र","ग्र","रु","रू",
    "्र",
    "ओ","औ","आ","अ","ई","इ","उ","ऊ","ऐ","ए","ऋ",
    "क्","क","क्क","ख्","ख","ग्","ग","घ्","घ","ङ",
    "चै","च्","च","छ","ज्","ज","झ्","झ","ञ",
    "ट्ट","ट्ठ","ट","ठ","ड्ड","ड्ढ","ड","ढ","ण्","ण",
    "त्","त","थ्","थ","द्ध","द","ध्","ध","न्","न",
    "प्","प","फ्","फ","ब्","ब","भ्","भ","म्","म",
    "य्","य","र","ल्","ल","ळ","व्","व",
    "श्","श","ष्","ष","स्","स","ह",
    "ऑ","ॉ","ो","ौ","ा","ी","ु","ू","ृ","े","ै",
    "ं","ँ","ः","ॅ","ऽ","् ","्","़","/"
]

UNICODE_TO_DEVLYS_TARGET: List[str] = [
    "^","*","Þ","ß","¼","½","¿","À","¾","A","\\","&","&","Œ","]","-","~ ",
    "å","ƒ","„","…","†","‡","ˆ","‰","Š","‹","Û","$","(","&",
    "¶+","d+","[k+","x+","T+","t+","M+","<+","Q+",";+","j+","u+",
    "Ù","Ùk","ä","–","—",
    "Üo","à","á","â","ã","ºz","º","í","{","{k","«","=","K",
    "Nî","Vî","Bî","Mî","<î","|","}",
    "J","Vª","Mª","<ªª","Nª","Ø","Ý","æ","ç","xz","#",":",
    "z",
    "vks","vkS","vk","v","bZ","b","m","Å",",s",",","_",
    "D","d","ô","[","[k","X","x","?","?k","³",
    "pkS","P","p","N","T","t","÷",">","¥",
    "ê","ë","V","B","ì","ï","M","<",".",".k",
    "R","r","F","Fk",")","n","è","èk","U","u",
    "I","i","¶","Q","C","c","H","Hk","E","e",
    "¸",";","j","Y","y","G","O","o",
    "'","'k","\"","\"k","L","l","g",
    "v‚","‚","ks","kS","k","h","q","w","`","s","S",
    "a","¡","%","W","·","~ ","~","+","@"
]

DEVLYS_MATRAS = "अ आ इ ई उ ऊ ए ऐ ओ औ ा ि ी ु ू ृ े ै ो ौ ं : ँ ॅ"
UNICODE_MATRAS = "ािीुूृेैोौं:ँॅ"


def normalize_text(text: str) -> str:
    return text.replace("’", "'")


def replace_all_pairs(text: str, source: List[str], target: List[str]) -> str:
    for old, new in zip(source, target):
        while old in text:
            text = text.replace(old, new)
    return text


def fix_devlys_i_matra(text: str) -> str:
    position = text.find("f")
    while position != -1 and position + 1 < len(text):
        next_char = text[position + 1]
        text = text.replace("f" + next_char, next_char + "ि", 1)
        position = text.find("f", position + 1)
    return text


def fix_devlys_im_matra(text: str) -> str:
    position = text.find("fa")
    while position != -1 and position + 2 < len(text):
        next_char = text[position + 2]
        text = text.replace("fa" + next_char, next_char + "िं", 1)
        position = text.find("fa", position + 2)
    return text


def fix_wrong_i_before_halant(text: str) -> str:
    position = text.find("ि्")
    while position != -1 and position + 2 < len(text):
        next_char = text[position + 2]
        text = text.replace("ि्" + next_char, "्" + next_char + "ि", 1)
        position = text.find("ि्", position + 2)
    return text


def move_reph_to_left(text: str) -> str:
    position = text.find("Z")
    while position > 0:
        target = position - 1

        while target >= 0 and text[target] in DEVLYS_MATRAS:
            target -= 1

        while target > 0 and text[target - 1] == "्":
            target -= 2

        chunk = text[target:position]
        text = text.replace(chunk + "Z", "र्" + chunk, 1)
        position = text.find("Z")

    return text


def devlys_to_unicode(text: str) -> str:
    text = normalize_text(text)
    text = replace_all_pairs(text, DEVLYS_TO_UNICODE_SOURCE, DEVLYS_TO_UNICODE_TARGET)

    text = text.replace("±", "Zं")
    text = text.replace("Æ", "र्f")
    text = fix_devlys_i_matra(text)

    text = text.replace("Ç", "fa")
    text = text.replace("É", "र्fa")
    text = fix_devlys_im_matra(text)

    text = text.replace("Ê", "ीZ")
    text = fix_wrong_i_before_halant(text)
    text = move_reph_to_left(text)

    return text


def move_i_matra_to_left(text: str) -> str:
    position = text.find("ि")
    while position != -1:
        left_char = text[position - 1]
        text = text.replace(left_char + "ि", "f" + left_char, 1)
        position -= 1

        while position > 0 and text[position - 1] == "्":
            cluster = text[position - 2:position]
            text = text.replace(cluster + "f", "f" + cluster, 1)
            position -= 2

        position = text.find("ि", position + 1)

    return text


def move_reph_to_right(text: str) -> str:
    text += "  "
    position = text.find("र्")

    while position > 0:
        target = position + 2

        while target < len(text) and text[target] in UNICODE_MATRAS:
            target += 1

        while target + 1 < len(text) and text[target + 1] == "्":
            target += 2

        chunk = text[position + 2:target + 1]
        text = text.replace("र्" + chunk, chunk + "Z", 1)
        position = text.find("र्")

    return text[:-2]


def unicode_to_devlys(text: str) -> str:
    nukta_normalization = {
        "त्र्य": "«य",
        "श्र्य": "Ü\u200d\u200dzय",
        "क़": "क़",
        "ख़‌": "ख़",
        "ग़": "ग़",
        "ज़": "ज़",
        "ड़": "ड़",
        "ढ़": "ढ़",
        "ऩ": "ऩ",
        "फ़": "फ़",
        "य़": "य़",
        "ऱ": "ऱ",
    }

    for old, new in nukta_normalization.items():
        text = text.replace(old, new)

    text = move_i_matra_to_left(text)
    text = move_reph_to_right(text)
    text = replace_all_pairs(text, UNICODE_TO_DEVLYS_SOURCE, UNICODE_TO_DEVLYS_TARGET)

    text = text.replace("Zksa", "ksZa")
    text = text.replace("~ Z", "Z~")
    text = text.replace("Zk", "kZ")
    text = text.replace("Zh", "Ê")

    return text