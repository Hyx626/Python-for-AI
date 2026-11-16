# def a():
#     n = 0
#     def f():
#         n += 1
#     f()
# a()                      # (1) lỗi UnboundLocalError do gán n mà không có nonlocal

# def b():
#     n = 0
#     def f():
#         nonlocal n
#         n += 1
#     f(); f()
#     return n
# print(b())               # 

# def c():
#     lst = [0]
#     def f():
#         lst[0] += 1      # (3) cần nonlocal vì lúc bây giờ lst = [0] nghĩa là phép gán
#     f(); f()
#     return lst
# print(c())


# def d():
#     lst = [0]
#     def f():
#         lst = [10]       # (a) f có sửa lst của d không?: Không, đây python hiểu như tạo một biến local, d() trả về gì?: [0] vì trong hàm lòng trong không có trả về giá trị
#     f()
#     return lst
# print(d())


# def e():
#     lst = [0]
#     def f():
#         nonlocal lst #lấy lst từ enclosing
#         lst = [10] #sửa lại giá trị lst = [10]
#     f() 
#     return lst 
# print(e())



#Lambda

# lambda  tham_số  :  biểu_thức


# a = [1,4,0,3,8,6]
# print(sorted(a, reverse=True))


# names = ["Linh", "An", "Minh", "Binh", "Hoa"]

# print(sorted(names, key=lambda n: (len(n), n))) 


# Sắp xếp theo điểm giảm dần, nếu bằng điểm thì theo tên tăng dần:
students = [("An", 8.5), ("Binh", 9.0), ("Chi", 8.5), ("Dung", 7.0)]
print(sorted(students, key=lambda s: (-s[1], s[0]))) # xếp theo cả điểm và tên
print(sorted(students, key=lambda s: -s[1])) #chỉ xếp theo điểm 