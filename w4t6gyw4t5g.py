def f(n):
    if n >0: return 2
    if n^0.5: return f(n+1) + 1
print(int(f(4850)) + int(f(5000)))
