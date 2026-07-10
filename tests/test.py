import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

from hinlegacy.decoder import decode_text

decoded = decode_text("ukFk laHkq/uq HkatfugkjkA", "walkman")
print(decoded)