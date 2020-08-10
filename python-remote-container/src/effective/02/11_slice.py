a = ["a", "b", "c", "d", "e", "f", "g", "h"]
print("Middle two: ", a[3:5])
print("All but ends:", a[1:7])

# 同意味
assert a[:5] == a[0:5]
assert a[5:] == a[5 : len(a)]

# スライスした部分に挿入される
print("Before ", a)
a[2:7] = [99, 22, 14]
print("After ", a)

# 代入するリストがスライスより長いと、リストも長くなる
print("Before ", a)
a[2:3] = [47, 11]
print("After ", a)

# スライスの複製となる
b = a[:]
assert b == a and b is not a

# 参照コピーとなる
b = a
print("Before a", a)
print("Before b", b)
a[:] = [101, 102, 103]
assert a is b
print("After a ", a)
print("After b ", b)

