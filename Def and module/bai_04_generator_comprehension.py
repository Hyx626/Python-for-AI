# BÀI 4: Comprehension và Generator (hàm "lười")

# ---------------------------------------------------------------
# 1. Comprehension: cách viết gọn thay cho map/filter em đã học
# ---------------------------------------------------------------
nums = [3, 1, 2, 5, 8]

squares = [n * n for n in nums]                  # thay map
odds    = [n for n in nums if n % 2 == 1]        # thay filter
labels  = ["chẵn" if n % 2 == 0 else "lẻ" for n in nums]
lookup  = {n: n * n for n in nums}               # dict comprehension
unique  = {n % 3 for n in nums}                  # set comprehension
print(squares, odds, labels, lookup, unique, sep="\n")

# Quy tắc chị: comprehension dài quá 1 dòng hoặc lồng 2 tầng for -> viết vòng for thường.
# Code dễ đọc quan trọng hơn code ngắn.


# ---------------------------------------------------------------
# 2. Generator: dùng yield thay vì return
# ---------------------------------------------------------------
def countdown(n):
    while n > 0:
        yield n               # "nhả" 1 giá trị rồi TẠM DỪNG tại đây
        n -= 1

gen = countdown(3)
print(next(gen))              # 3
print(next(gen))              # 2
print(list(gen))              # [1]  (lấy nốt phần còn lại)

# 🧠 Logic note: gọi countdown(3) KHÔNG chạy thân hàm, chỉ tạo ra generator.
# Mỗi lần next(), hàm chạy tiếp từ chỗ dừng lần trước tới yield kế.
# Hết yield -> StopIteration (vòng for tự bắt lỗi này nên em không thấy).
# Generator chỉ duyệt được MỘT lần: list(gen) lần 2 sẽ ra [].


# ---------------------------------------------------------------
# 3. Vì sao dùng generator? Tiết kiệm bộ nhớ
# ---------------------------------------------------------------
import sys

big_list = [i for i in range(1_000_000)]   # giữ cả triệu số trong RAM
big_gen  = (i for i in range(1_000_000))   # generator expression, dùng ngoặc ()
print(sys.getsizeof(big_list), "bytes")    # ~8 MB
print(sys.getsizeof(big_gen), "bytes")     # ~200 bytes
print(sum(big_gen))                        # vẫn tính được tổng

# Khi xử lý file lớn hoặc dữ liệu AI hàng triệu dòng, em sẽ dùng generator liên tục.
# Em nhớ lại: map() và filter() cũng trả về iterator "lười" kiểu này, đó là lý
# do trong file "Functions are objects" em phải bọc list(...) mới thấy kết quả.


def read_numbers(lines):
    """Ví dụ thực tế: lọc từng dòng, không cần nạp hết vào bộ nhớ."""
    for line in lines:
        line = line.strip()
        if line.isdigit():
            yield int(line)

print(list(read_numbers(["10", "abc", " 7 ", ""])))   # [10, 7]
