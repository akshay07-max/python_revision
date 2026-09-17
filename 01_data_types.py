# 1] int, float, complex = immutable 
# eg 5, 5.5, 2+4j

a = 10 
print(a)
print(type(a))

b = 2.32
print(b)
print(type(b))


c = 33+33j
print(c)
print(type(c))

# 2] str = immutable. eg. "Hello"
d = "Good Boy"
print(d)
print(type(d))

# 3] bool = Immutable. eg. True, False
f = True
print(f)
print(type(f))


# 4] list = Mutable eg. [1,2,3,4]
g = [12, 32, 34, 55]
print(g)
print(type(g))

# 5] Tuple = Immutable eg. (12, 44, 45)
h = (12, 42, 55)
print(h)
print(type(h))

# 6] set = Mutable eg. {1,2,4,5}
i = {1, 3, 5, 7}
print(i)
print(type(i))

# 7] frozenset = Immutable eg. frozenset({1,2})
j = frozenset({1,2})
print(j)
print(type(j))

# 8] dict = Mutable eg. {"a": 1, "b":2}
k = {"a": 1, "b":2}
print(k)
print(type(k))

# 9] NoneType = Immutable eg. None
l = None
print(l)
print(type(l))
