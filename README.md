# Python for AI — nhật ký học của em

Repo này là nơi mình học Python từng bước, từ nền tảng đến lập trình hướng đối tượng (OOP) và AI.
Mỗi bài có code chạy được, ghi chú "Logic note" giải thích chỗ dễ hiểu sai, và bài tập tự kiểm tra.

## Lộ trình

| Giai đoạn | Nội dung | Trạng thái |
|---|---|---|
| 1. Hàm & Module | tham số, `*args/**kwargs`, LEGB, `global/nonlocal`, closure, decorator, type hint, đệ quy, generator, module, package | 🔄 đang học |
| 2. Cấu trúc dữ liệu & xử lý lỗi | list/dict/set/tuple sâu, `try/except`, `raise`, tự định nghĩa exception, `with` | ⏳ |
| 3. File & thư viện chuẩn | đọc ghi file, JSON/CSV, `pathlib`, `collections`, `itertools`, `datetime` | ⏳ |
| 4. **OOP** | `class`, `__init__`, `self`, thuộc tính/phương thức, đóng gói, kế thừa, đa hình, `@property`, `@classmethod`, `@staticmethod`, dunder (`__str__`, `__repr__`, `__eq__`), `dataclass`, composition vs inheritance | ⏳ |
| 5. Chất lượng code | `pytest`, `venv`, `pip`, `logging`, PEP8, type hint với `mypy` | ⏳ |
| 6. Dự án | 2-3 project nhỏ (quản lý chi tiêu, bot đọc file, mini game) làm bằng OOP | ⏳ |
| 7. Python for AI | `numpy`, `pandas`, `matplotlib`, rồi `scikit-learn` | ⏳ |

## Cách học (nhịp độ đều, không trễ nãi)

1. Mỗi ngày tối thiểu 60-90 phút: 20 phút đọc + gõ lại ví dụ (không copy-paste), 40 phút bài tập.
2. Gõ lại code, đổi giá trị, cố tình làm lỗi để xem Python báo gì.
3. Với mỗi dòng "Logic note": tự giải thích lại bằng lời của mình. Không giải thích được = chưa hiểu.
4. Cuối ngày: `git add . && git commit -m "bai 02: decorator"` — mỗi ngày ít nhất 1 commit. Lịch commit đều đặn là minh chứng tốt nhất.
5. Mỗi cuối tuần: làm lại bài tập khó nhất mà không nhìn đáp án.

## Cấu trúc thư mục

```
Def and module/
  bai_01_scope_closure.py
  bai_02_decorator.py
  bai_03_return_typehint_recursion.py
  bai_04_generator_comprehension.py
  bai_05_module_demo/        # chạy: python main.py
  bai_tap_01.py              # tự viết code, chạy để xem ✅/❌
```

## Lưu ý trên Windows

Nếu in tiếng Việt bị lỗi `UnicodeEncodeError`, chạy với chế độ UTF-8:

```
python -X utf8 ten_file.py
```
