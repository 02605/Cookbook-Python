a = [0, 1, 2, ['a', 'b']]
# 浅拷贝
b = a[:]
a.append(3)
a[3].append('c')
a[0] = -1
print(a)
print(b)