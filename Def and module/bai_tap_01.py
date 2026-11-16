# BÀI TẬP SAU BÀI 1-4
# Cách làm: tự viết thân hàm thay cho `pass`, rồi chạy `python bai_tap_01.py`.
# Mỗi bài có test ở cuối; bài nào đúng sẽ hiện ✅. KHÔNG xem đáp án trước khi tự thử 20 phút.
# Bí quá thì viết ra giấy "đầu vào -> đầu ra" của ví dụ nhỏ nhất rồi mới code.

import functools


# Bài 1 (closure): make_multiplier(3) trả về một hàm nhân đối số với 3.
def make_multiplier(factor):
    pass


# Bài 2 (nonlocal): make_accumulator() trả về hàm; mỗi lần gọi acc(x) cộng x
# vào tổng đang nhớ và trả về tổng mới. Không dùng global.
def make_accumulator():
    pass


# Bài 3 (decorator): count_calls đếm số lần hàm bị gọi, lưu ở wrapper.calls
def count_calls(func):
    pass


# Bài 4 (decorator có tham số): only_positive(func) -> nếu bất kỳ argument
# vị trí nào <= 0 thì raise ValueError("phải dương"), ngược lại gọi hàm gốc.
def only_positive(func):
    pass


# Bài 5 (return nhiều giá trị + type hint): stats(numbers) -> (min, max, mean)
def stats(numbers: list[float]) -> tuple[float, float, float]:
    pass


# Bài 6 (đệ quy): sum_digits(1234) -> 10, không dùng str() hay vòng lặp.
def sum_digits(n: int) -> int:
    pass


# Bài 7 (generator): evens(limit) yield lần lượt các số chẵn từ 0 tới < limit.
def evens(limit):
    pass


# Bài 8 (generator + thực tế): chunks([1,2,3,4,5], 2) yield [1,2], [3,4], [5]
def chunks(items, size):
    pass


# Bài 9 (suy luận, KHÔNG chạy trước): viết dự đoán output rồi mới chạy để kiểm tra.
#   def f(x, acc=[]):
#       acc.append(x)
#       return acc
#   print(f(1), f(2), f(3, []), f(4))
# Dự đoán của em: ...... (ghi vào đây dạng comment, rồi giải thích TẠI SAO)


# ====================== PHẦN TEST (đừng sửa) ======================
def check(name, fn):
    try:
        fn()
        print(f"✅ {name}")
    except Exception as e:
        print(f"❌ {name}: {type(e).__name__} {e}")

def t1():
    assert make_multiplier(3)(5) == 15

def t2():
    acc = make_accumulator()
    assert (acc(5), acc(10), acc(-3)) == (5, 15, 12)
    assert make_accumulator()(1) == 1          # bộ nhớ độc lập

def t3():
    @count_calls
    def hi(): return "hi"
    hi(); hi(); hi()
    assert hi.calls == 3 and hi() == "hi"

def t4():
    @only_positive
    def add(a, b): return a + b
    assert add(1, 2) == 3
    try:
        add(1, -2)
    except ValueError:
        return
    raise AssertionError("phải raise ValueError")

def t5():
    assert stats([1, 2, 6]) == (1, 6, 3)

def t6():
    assert sum_digits(1234) == 10 and sum_digits(0) == 0

def t7():
    assert list(evens(7)) == [0, 2, 4, 6]

def t8():
    assert list(chunks([1, 2, 3, 4, 5], 2)) == [[1, 2], [3, 4], [5]]

if __name__ == "__main__":
    for i, t in enumerate([t1, t2, t3, t4, t5, t6, t7, t8], start=1):
        check(f"Bài {i}", t)
