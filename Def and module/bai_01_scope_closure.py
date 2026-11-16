# BÀI 1: Scope sâu hơn (global, nonlocal) và Closure
# Em đã biết LEGB rồi. Bài này trả lời câu hỏi tiếp theo:
# "Vậy trong hàm, làm sao SỬA được biến ở bên ngoài?"

# ---------------------------------------------------------------
# 1. ĐỌC được biến ngoài, nhưng GÁN thì khác
# ---------------------------------------------------------------
counter = 0

def read_only():
    print(counter)            # OK: chỉ đọc, Python tìm theo LEGB và thấy global

def broken():
    try:
        counter += 1          # ❌ lỗi!
    except UnboundLocalError as e:
        print("Lỗi:", e)

read_only()
broken()

# 🧠 Logic note (chỗ nhiều bạn không hiểu, chị giải thích kỹ):
# Python quyết định biến là local hay không TRƯỚC KHI chạy hàm, bằng cách
# nhìn xem trong thân hàm có phép GÁN (=, +=, for x in ...) tới tên đó không.
# Có gán -> Python coi `counter` là biến LOCAL của hàm ngay từ dòng đầu.
# Mà lúc `counter += 1` chạy thì local counter chưa có giá trị -> UnboundLocalError.
# Nghĩa là: lỗi không nằm ở dòng bị báo, mà ở chỗ Python đã "chốt" counter là local.


# ---------------------------------------------------------------
# 2. global: nói với Python "tôi muốn sửa biến ở tầng module"
# ---------------------------------------------------------------
def increase():
    global counter
    counter += 1

increase()
increase()
print("counter =", counter)   # 2

# ⚠️ Lời khuyên của chị: ĐỪNG lạm dụng global. Hàm dùng global khó test,
# khó đọc, dễ gây lỗi khó tìm. Hàm tốt = nhận input qua tham số, trả output
# qua return. Hãy coi `global` là phương án cuối cùng.


# ---------------------------------------------------------------
# 3. nonlocal: sửa biến của hàm BAO BỌC (tầng E trong LEGB)
# ---------------------------------------------------------------
def outer():
    x = "enclosing"
    def inner():
        nonlocal x            # x này là x của outer, không phải tạo x mới
        x = "đã bị inner sửa"
    inner()
    print(x)                  # đã bị inner sửa

outer()


# ---------------------------------------------------------------
# 4. CLOSURE: hàm "nhớ" biến của nơi nó được tạo ra
# ---------------------------------------------------------------
def make_counter():
    count = 0                 # biến của make_counter
    def tick():
        nonlocal count
        count += 1
        return count
    return tick               # trả về HÀM tick, chưa gọi nó

c1 = make_counter()
c2 = make_counter()
print(c1(), c1(), c1())       # 1 2 3
print(c2())                   # 1  <- c2 có count riêng, độc lập với c1

# 🧠 Logic note:
# make_counter() chạy xong thì lẽ ra `count` biến mất. Nhưng tick vẫn dùng nó,
# nên Python giữ `count` sống cùng tick. Cặp (hàm + biến nó nhớ) = closure.
# Em xem được biến nó nhớ bằng:
print(c1.__closure__[0].cell_contents)   # 3
# Bài 2 (decorator) xây hoàn toàn trên closure, em hiểu chắc bài này nhé.


# ---------------------------------------------------------------
# 5. Bẫy kinh điển: closure trong vòng lặp
# ---------------------------------------------------------------
funcs = []
for i in range(3):
    funcs.append(lambda: i)
print([f() for f in funcs])   # [2, 2, 2]  ← em có thể mong [0, 1, 2]

# Vì sao? Các lambda đều nhớ BIẾN i (không phải GIÁ TRỊ của i lúc tạo).
# Đến lúc gọi thì vòng lặp đã xong, i = 2.
# Cách sửa: "chốt" giá trị lúc tạo bằng tham số mặc định
funcs = [lambda i=i: i for i in range(3)]
print([f() for f in funcs])   # [0, 1, 2]
