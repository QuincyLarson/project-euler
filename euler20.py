def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

m = factorial(100)

m = map(int,str(m))
print m
h = sum(m)
print h


