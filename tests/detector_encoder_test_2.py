from hinlegacy.decoder import encode_text
from hinlegacy.detector import detect_font


SAMPLES = [
    "भारत एक सुंदर देश है",
    "कृपया यहाँ अपना नाम लिखिए",
    "विद्यालय में हिंदी पढ़ाई जाती है",
    "प्रशासनिक व्यवस्था मजबूत होनी चाहिए",
    "संविधान सभी नागरिकों को अधिकार देता है",
]


def test_detector_roundtrip_krutidev():
    for sample in SAMPLES:
        encoded = encode_text(sample, "krutidev_010")
        result = detect_font(encoded)

        assert result.font_slug == "krutidev_010", (
            f"Expected 'krutidev_010' but detected '{result.font_slug}' "
            f"for sample: {sample!r}\n"
            f"Encoded text: {encoded!r}"
        )


def test_detector_roundtrip_devlys():
    for sample in SAMPLES:
        encoded = encode_text(sample, "devlys_010")
        result = detect_font(encoded)

        assert result.font_slug == "devlys_010", (
            f"Expected 'devlys_010' but detected '{result.font_slug}' "
            f"for sample: {sample!r}\n"
            f"Encoded text: {encoded!r}"
        )


def test_detector_roundtrip_walkman_chanakya():
    for sample in SAMPLES:
        encoded = encode_text(sample, "walkman_chanakya_905")
        result = detect_font(encoded)

        assert result.font_slug == "walkman_chanakya_905", (
            f"Expected 'walkman_chanakya_905' but detected '{result.font_slug}' "
            f"for sample: {sample!r}\n"
            f"Encoded text: {encoded!r}"
        )