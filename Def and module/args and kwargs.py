# def total(*args):            # gom các positional argument thành tuple
#     return sum(args)

# def show(**kwargs):          # gom keyword argument thành dict
#     for key, value in kwargs.items():
#         print(key, "=", value)

# total(1, 2, 3)               # 6
# show(name="An", age=18)     # An = 18

# # Dấu * nghĩa là “gom lại thành tuple”, dấu ** nghĩa là “gom lại thành dict”.
# # args và kwargs chỉ là tên quy ước, quan trọng là dấu sao.


# def add_item(item, box=[]):      # ❌ BAD
#     box.append(item)
#     return box

# print(add_item(1))   # [1]
# print(add_item(2))   # [1, 2]  ← em mong là [2]!



# def add_item(item, box=None):    # ✅ GOOD
#     if box is None:
#         box = []
#     box.append(item)
#     return box


def shipping_label(*args, **kwargs):
    for arg in args:
        print(arg, end = " ")
    print(f"{kwargs.get('name')}")
    print(f"{kwargs.get('age')}")

shipping_label("ngo", "Gia", "Gia",
               name = "Huy", age = 19)