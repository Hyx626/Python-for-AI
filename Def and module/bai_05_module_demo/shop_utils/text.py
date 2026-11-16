import re
import unicodedata


def slugify(title: str) -> str:
    """'Áo Thun Nam!' -> 'ao-thun-nam'"""
    title = title.replace("đ", "d").replace("Đ", "D")
    title = unicodedata.normalize("NFKD", title)
    title = "".join(ch for ch in title if not unicodedata.combining(ch))
    title = re.sub(r"[^a-zA-Z0-9]+", "-", title).strip("-")
    return title.lower()
