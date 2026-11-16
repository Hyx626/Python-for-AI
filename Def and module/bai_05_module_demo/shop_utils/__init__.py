# Có file __init__.py thì thư mục shop_utils là một PACKAGE.
# Code trong file này chạy 1 lần khi package được import lần đầu.

from .money import format_vnd, apply_discount   # dấu . = "cùng package với file này"
from .text import slugify

__all__ = ["format_vnd", "apply_discount", "slugify"]
# __all__ quy định những tên nào được lấy khi viết: from shop_utils import *
