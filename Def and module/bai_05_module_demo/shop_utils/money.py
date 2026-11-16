def format_vnd(amount: int) -> str:
    """1500000 -> '1.500.000đ'"""
    return f"{amount:,}".replace(",", ".") + "đ"


def apply_discount(price: int, percent: float) -> int:
    if not 0 <= percent <= 100:
        raise ValueError("percent phải nằm trong [0, 100]")
    return round(price * (1 - percent / 100))


# 🧠 Logic note về if __name__ == "__main__":
# Mỗi file .py có biến __name__.
#  - Chạy trực tiếp `python money.py`      -> __name__ == "__main__"
#  - Được file khác import                 -> __name__ == "shop_utils.money"
# Nên khối dưới đây chỉ chạy khi em chạy thẳng file này (dùng để tự test nhanh),
# còn khi import thì KHÔNG chạy.
if __name__ == "__main__":
    print(format_vnd(1500000))
    print(apply_discount(200000, 15))
