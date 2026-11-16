# BÀI 5: Module và Package
# Chạy bằng:  python main.py   (đứng trong thư mục bai_05_module_demo)

# --- 4 cách import, em nên biết khi nào dùng cái nào ---
import math                              # 1. import cả module -> math.sqrt(...)
from math import sqrt                    # 2. lấy đúng thứ cần  -> sqrt(...)
import datetime as dt                    # 3. đặt tên ngắn      -> dt.date.today()
from shop_utils import format_vnd, apply_discount, slugify   # 4. từ package của mình

print(math.sqrt(16), sqrt(25), dt.date.today().year)

price = apply_discount(200_000, 15)
print(format_vnd(price))                 # 170.000đ
print(slugify("Áo Thun Nam Đẹp!"))       # ao-thun-nam-dep

# Không nên: from module import *   (không biết tên nào đến từ đâu, dễ ghi đè nhau)

# 🧠 Logic note: Python tìm module ở đâu?
# Theo thứ tự trong sys.path: thư mục của file đang chạy -> thư viện chuẩn -> site-packages (pip).
import sys
print(sys.path[0])                       # thư mục chứa main.py
# Vì thế file em đặt tên trùng thư viện (vd random.py, math.py) sẽ che mất
# thư viện thật và gây lỗi lạ. Đừng đặt tên như vậy!

# 🧠 Logic note: import chỉ chạy file MỘT lần, lần sau lấy từ cache sys.modules.
print("shop_utils.money" in sys.modules)  # True

# pip và môi trường ảo (làm trong terminal, không phải trong file .py):
#   python -m venv .venv
#   .venv\Scripts\activate        (Windows)
#   pip install requests
#   pip freeze > requirements.txt
# Mỗi project nên có .venv riêng để thư viện không lẫn lộn. KHÔNG commit .venv lên git.
