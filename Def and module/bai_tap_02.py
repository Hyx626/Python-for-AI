# BÀI TẬP 02: củng cố scope, nonlocal, lambda, sorted, closure, decorator
# Làm lần lượt từ phần A đến D. Chạy:  python -X utf8 bai_tap_02.py
# Quy tắc: tự thử 20 phút, KHÔNG nhìn đáp án; mọi dự đoán phải ghi LÝ DO.

# ============ PHẦN A: DỰ ĐOÁN OUTPUT (không chạy trước!) ============
# Với mỗi đoạn, ghi dự đoán + lý do vào comment, rồi mới bỏ comment ra chạy.

# A1
# x = 5
# def f():
#     print(x)
#     x = 10
# f()
# Dự đoán + lý do: ......

# A2
# def make():
#     total = 0
#     def add(n):
#         total += n
#         return total
#     return add
# a = make()
# print(a(1))
# Dự đoán + lý do: ......  (sửa thế nào cho chạy đúng?)

# A3
# def make():
#     data = []
#     def add(n):
#         data.append(n)
#         return data
#     return add
# a = make(); b = make()
# a(1); a(2)
# print(b(3), a(4))
# Dự đoán + lý do: ......

# A4
# fs = [lambda: i for i in range(3)]
# print([f() for f in fs])
# Dự đoán + lý do: ......  (sửa để ra [0, 1, 2])

# A5
# def g(x, box=[]):
#     box.append(x)
#     return len(box)
# print(g(1), g(2), g(3, []), g(4))
# Dự đoán + lý do: ......


# ============ PHẦN B: LAMBDA + SORTED ============
students = [("An", 8.5), ("Binh", 9.0), ("Chi", 8.5), ("Dung", 7.0)]

# B1: điểm giảm dần, bằng điểm thì tên tăng dần
def rank_1(items):
    pass

# B2: điểm giảm dần, bằng điểm thì tên GIẢM dần (gợi ý: sắp 2 lần, nhờ sorted là stable)
def rank_2(items):
    pass

# B3: trả về người có tên dài nhất (dùng max + key); nếu hòa lấy người đứng đầu danh sách
def longest_name(items):
    pass

# B4: gom tên theo điểm, trả về dict {điểm: [tên, ...]} (tên trong list xếp tăng dần)
#     {9.0: ["Binh"], 8.5: ["An", "Chi"], 7.0: ["Dung"]}  (dict theo điểm giảm dần)
def group_by_score(items):
    pass


# ============ PHẦN C: CLOSURE + NONLOCAL ============
# C1: make_toggle() -> hàm; mỗi lần gọi đổi qua lại True/False, lần đầu trả True
def make_toggle():
    pass

# C2: make_bank(balance) -> (deposit, withdraw)  hai hàm cùng dùng chung số dư.
#     withdraw quá số dư thì raise ValueError("không đủ tiền").  Cả hai trả về số dư mới.
def make_bank(balance):
    pass

# C3: make_history() -> add(x) trả về list tất cả giá trị đã add, KHÔNG dùng nonlocal
def make_history():
    pass


# ============ PHẦN D: DECORATOR ============
import functools

# D1: log_calls: mỗi lần gọi hàm, ghi vào list global CALL_LOG dòng "tên_hàm(args)".
#     Phải giữ nguyên __name__ của hàm gốc (functools.wraps).
CALL_LOG = []
def log_calls(func):
    pass

# D2: retry(times): nếu hàm raise Exception thì thử lại, tối đa `times` lần tổng cộng;
#     hết lần mà vẫn lỗi thì ném lại lỗi cuối cùng.
def retry(times):
    pass

# D3: type_check(*types): kiểm tra từng argument vị trí đúng kiểu; sai thì raise TypeError.
#     @type_check(int, int) def add(a, b)
def type_check(*types):
    pass


# ====================== TEST (đừng sửa) ======================
def check(name, fn):
    try:
        fn(); print(f"✅ {name}")
    except Exception as e:
        print(f"❌ {name}: {type(e).__name__} {e}")

def b1(): assert rank_1(students) == [("Binh", 9.0), ("An", 8.5), ("Chi", 8.5), ("Dung", 7.0)]
def b1_rev():  # dữ liệu "xấu": đảo thứ tự đầu vào
    assert rank_1(students[::-1]) == [("Binh", 9.0), ("An", 8.5), ("Chi", 8.5), ("Dung", 7.0)]
def b2(): assert rank_2(students) == [("Binh", 9.0), ("Chi", 8.5), ("An", 8.5), ("Dung", 7.0)]
def b2_rev(): assert rank_2(students[::-1]) == [("Binh", 9.0), ("Chi", 8.5), ("An", 8.5), ("Dung", 7.0)]
def b3(): assert longest_name(students) == ("Binh", 9.0) and longest_name([("Hoa", 1), ("Lan", 2)]) == ("Hoa", 1)
def b4():
    r = group_by_score(students)
    assert r == {9.0: ["Binh"], 8.5: ["An", "Chi"], 7.0: ["Dung"]} and list(r) == [9.0, 8.5, 7.0]
    assert group_by_score([]) == {}

def c1():
    t = make_toggle(); assert (t(), t(), t()) == (True, False, True)
    assert make_toggle()() is True
def c2():
    dep, wd = make_bank(100)
    assert dep(50) == 150 and wd(30) == 120
    try: wd(500)
    except ValueError: pass
    else: raise AssertionError("phải raise ValueError")
    assert make_bank(0)[0](1) == 1
def c3():
    h = make_history(); h(1); assert h(2) == [1, 2]
    assert make_history()(9) == [9]

def d1():
    CALL_LOG.clear()
    @log_calls
    def add(a, b): return a + b
    assert add(1, 2) == 3 and add.__name__ == "add" and CALL_LOG == ["add(1, 2)"]
def d2():
    state = {"n": 0}
    @retry(3)
    def flaky():
        state["n"] += 1
        if state["n"] < 3: raise RuntimeError("lỗi")
        return "ok"
    assert flaky() == "ok" and state["n"] == 3
    @retry(2)
    def bad(): raise KeyError("x")
    try: bad()
    except KeyError: return
    raise AssertionError("hết lượt phải ném lại lỗi")
def d3():
    @type_check(int, int)
    def add(a, b): return a + b
    assert add(1, 2) == 3
    try: add(1, "2")
    except TypeError: return
    raise AssertionError("phải raise TypeError")

if __name__ == "__main__":
    tests = [("B1", b1), ("B1 đảo", b1_rev), ("B2", b2), ("B2 đảo", b2_rev), ("B3", b3), ("B4", b4),
             ("C1", c1), ("C2", c2), ("C3", c3), ("D1", d1), ("D2", d2), ("D3", d3)]
    for name, t in tests:
        check(name, t)
