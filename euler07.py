"""def prime(n):
    if n < 2: return []
    if n == 2: return [2]
    s = range(3, n, 2)
    mroot = n ** .5
    half = len(s)
    i = 0
    m = 3
    while m < mroot:
        if s[i]:
            j = (m * m - 3)//2
            s[j] = 0
            while j < half:
                s[j] = 0
                j += m
                
        i += 1
        m = 2 * i + 3
    return [2] + [x for x in s if x]

num = 10001
primeList = prime(num)
print "Here are the primes between 2 and %d:" % num
print primeList
"""

#Ok - our goal is to index the returns so we can call magic number 10001 and complete Euler 7.
#We have a way to make primes. Let's try to understand that then assign to index

from sys import prime

i = 3
while a.length <= 10001:
    i += 2
    if 


print a[10001]
