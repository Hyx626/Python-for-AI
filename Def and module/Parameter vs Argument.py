# Parameter vs Argument
# Parameter (tham số) là tên khai báo trong def.
# Argument (đối số) là giá trị thật em truyền vào khi gọi hàm.


def greet(name, greeting="Hello"):   # name, greeting = parameters
    return f"{greeting}, {name}!"

greet("Linh")                        # "Linh" = argument (positional)
greet("Linh", greeting="Hi")         # keyword argument

# Logic note: return khác print. print chỉ hiển thị ra màn hình, còn return 
# trả giá trị về để chương trình dùng tiếp. Hàm không có return sẽ trả về None