# BÀI 3: Thiết kế hàm cho tốt
# return nhiều giá trị, type hint, docstring, tham số đặc biệt, đệ quy.

# ---------------------------------------------------------------
# 1. "Trả về nhiều giá trị" thực ra là trả về MỘT tuple
# ---------------------------------------------------------------
def min_max(numbers):
    return min(numbers), max(numbers)    # tuple (min, max)

result = min_max([4, 9, 1])
print(result)                            # (1, 9)
lo, hi = min_max([4, 9, 1])              # unpacking: tách tuple ra 2 biến
print(lo, hi)

# Unpacking với dấu *
first, *rest = [10, 20, 30, 40]
print(first, rest)                       # 10 [20, 30, 40]


# ---------------------------------------------------------------
# 2. Docstring + Type hint: để người khác (và em sau 1 tháng) hiểu hàm
# ---------------------------------------------------------------
def average(numbers: list[float], round_to: int = 2) -> float:
    """Tính trung bình cộng.

    Args:
        numbers: danh sách số, không được rỗng.
        round_to: làm tròn bao nhiêu chữ số thập phân.

    Returns:
        Giá trị trung bình.

    Raises:
        ValueError: nếu danh sách rỗng.
    """
    if not numbers:
        raise ValueError("numbers không được rỗng")
    return round(sum(numbers) / len(numbers), round_to)

print(average([1, 2, 4]))
help(average)                            # xem docstring

# 🧠 Logic note: type hint KHÔNG ép kiểu lúc chạy. average("abc") vẫn chạy
# và nổ lỗi ở chỗ khác. Nó là "lời chú thích có cấu trúc" để editor và công
# cụ như mypy phát hiện lỗi sớm. Em cứ viết thói quen này từ giờ.


# ---------------------------------------------------------------
# 3. Tham số đặc biệt: / và *
# ---------------------------------------------------------------
def make_user(name, /, age, *, is_admin=False):
    # trước dấu /  : CHỈ truyền theo vị trí  (positional-only)
    # sau dấu *    : BẮT BUỘC ghi tên         (keyword-only)
    return {"name": name, "age": age, "is_admin": is_admin}

print(make_user("An", 20, is_admin=True))
print(make_user("Binh", age=25))
# make_user("An", 20, True)        # ❌ TypeError: is_admin phải ghi tên
# Dùng keyword-only cho tham số kiểu cờ True/False để chỗ gọi hàm tự giải thích.


# ---------------------------------------------------------------
# 4. Đệ quy (recursion): hàm tự gọi chính nó
# ---------------------------------------------------------------
def factorial(n: int) -> int:
    if n <= 1:                           # BASE CASE: điều kiện dừng, bắt buộc có
        return 1
    return n * factorial(n - 1)          # bài toán nhỏ hơn

print(factorial(5))                      # 120

# 🧠 Logic note: cách nghĩ đệ quy gồm 2 câu hỏi:
#   (a) Trường hợp nhỏ nhất, trả lời được ngay là gì?  -> base case
#   (b) Nếu đã có đáp án cho bài nhỏ hơn một bậc, tôi suy ra đáp án bài này thế nào?
# Em đừng cố "chạy trong đầu" hết mọi tầng. Hãy tin vào (a) và (b).
# Quên base case -> gọi mãi -> RecursionError (giới hạn mặc định ~1000 tầng).

def flatten(items):
    """Làm phẳng list lồng nhau: [1,[2,[3]]] -> [1,2,3]. Đệ quy rất hợp ở đây."""
    out = []
    for item in items:
        if isinstance(item, list):
            out.extend(flatten(item))
        else:
            out.append(item)
    return out

print(flatten([1, [2, [3, 4]], 5]))
