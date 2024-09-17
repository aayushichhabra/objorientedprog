def slicer(a, b, x):
    s = ""
    for i in range(a, b):
        s += x[i]
    return s

x = "hello world"
print(slicer(2, 9, x))
