i = 0
x, y = 0, 1
evensum = 0

while x < 4000000:
    x, y = y, x + y
    if x % 2 == 0 and x < 4000000:
        evensum += x
    print x

print evensum
