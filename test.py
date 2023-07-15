# a = 1
# b = a
# print("a=", a, "b=", b)

# a += 1
# b -= 1
# print("a=", a, "b=", b)

# a = [1,2,3]
# b = a

# a[0] = 100 # [100,2,3]
# b[1] = 200 # [100,200,3]

def test(a):
    print("before: a = ", a)
    a += 100
    print("after: a=", a)

k = 10
print("before: k = ", k)
test(k)

print("after: k=", k)