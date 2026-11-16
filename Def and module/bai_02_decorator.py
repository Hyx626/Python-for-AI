# BÀI 2: Decorator
# Điều kiện cần: hiểu bài 1 (closure) và "Functions are objects".
# Decorator = hàm nhận vào một hàm, trả về một hàm mới (đã được "bọc thêm").

import functools
import time

# ---------------------------------------------------------------
# 1. Viết decorator "bằng tay" để thấy nó không có phép màu
# ---------------------------------------------------------------
def shout(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)     # gọi hàm gốc
        return result.upper()              # bọc thêm: viết hoa kết quả
    return wrapper

def hello(name):
    return f"hello {name}"

hello = shout(hello)          # thay tên `hello` bằng phiên bản đã bọc
print(hello("linh"))          # HELLO LINH

# Cú pháp @ chỉ là cách viết gọn của đúng dòng `hello = shout(hello)`:
@shout
def bye(name):
    return f"bye {name}"

print(bye("an"))              # BYE AN

# 🧠 Logic note: vì sao wrapper dùng (*args, **kwargs)?
# Vì wrapper không biết trước hàm gốc nhận mấy tham số. Dấu * và ** (em đã học)
# giúp wrapper nhận tất cả rồi chuyển nguyên xi cho hàm gốc.


# ---------------------------------------------------------------
# 2. functools.wraps: giữ lại "danh tính" của hàm gốc
# ---------------------------------------------------------------
def timer(func):
    @functools.wraps(func)    # nếu thiếu dòng này, tên hàm sẽ thành "wrapper"
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        print(f"[timer] {func.__name__} chạy {elapsed:.6f}s")
        return result
    return wrapper

@timer
def slow_sum(n):
    """Tính tổng 0..n-1."""
    return sum(range(n))

print(slow_sum(1_000_000))
print(slow_sum.__name__)      # slow_sum (nhờ wraps; không có thì in "wrapper")


# ---------------------------------------------------------------
# 3. Decorator có tham số: thêm MỘT tầng hàm nữa
# ---------------------------------------------------------------
def repeat(times):                    # tầng 1: nhận tham số của decorator
    def decorator(func):              # tầng 2: nhận hàm
        @functools.wraps(func)
        def wrapper(*args, **kwargs): # tầng 3: chạy thật
            for _ in range(times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(3)                            # = repeat(3)(say_hi)
def say_hi():
    print("hi!")

say_hi()                              # in 3 lần

# 🧠 Logic note: @repeat(3) trước hết GỌI repeat(3) để lấy ra `decorator`,
# rồi mới áp `decorator` lên hàm. Vì vậy cần 3 tầng. Nếu em thấy rối, hãy
# viết lại thành dạng không có @ để nhìn từng bước.


# ---------------------------------------------------------------
# 4. Decorator có sẵn rất hay dùng: functools.cache
# ---------------------------------------------------------------
@functools.cache                      # nhớ kết quả những lần đã tính
def fib(n):
    return n if n < 2 else fib(n - 1) + fib(n - 2)

print(fib(80))                        # tức thì. Thử bỏ @cache với fib(35) để thấy chậm
