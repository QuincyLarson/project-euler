import math

def xdivs(n):
    a, b = 0, 0
    while True: # infinite loop to determine whether triangle num
        a += 1000000
        b += a
        p = []
        for j in xrange (1, b): 
            if (b // j) * j == b:
                    p.append(j)
                    print j
                    if len(p) == n: # exit when hit 500th entry
                        return b, p

def get_div(n):
    divisors = [1, n]
    for i in xrange(1, math.sqrt(n)):
        if n / i == :
            divisors.append(i)
                    
        return divisors

print xdivs(500)
