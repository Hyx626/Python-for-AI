def square(n):
    return n * n

nums = [3, 1, 2]
print(list(map(square, nums))) # map áp dụng một hàm lên từng phần tử của một danh sách 
print(sorted(["bb", "a", "ccc"], key=len))      # ['a', 'bb', 'ccc']
print(list(filter(lambda n: n % 2 == 1, nums))) # [3, 1]

