def foo(a, b):
    c = 0
    while(a < 0):
        if (b < 0):
            b = b + 2
        a = a + 1
    c = a + b
    return c