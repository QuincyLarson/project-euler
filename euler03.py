m = 59569
n = 600851475143

for i in xrange (1, n, 2):
    if n % i == 0:
        print i
    if i > m:
        break


