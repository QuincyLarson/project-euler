#Update - apparently the caluclation needn't be done - divisor factors wikipedia article talks about this but the math was too complicated for me to follow. I'll tackle it later.

import math

def factorgen():



def divisorgen(n): # Greg Hewgill posted this on Stack overflow
    factors = (list(factorgen))
    nfactors = len(factors)
    f = [0] * nfactors
    while True:
        yield reduce(lambda x,y: x*y, factors[x][0]**f[x] for x in range(nfactors)], 1)
        i = 0
        while True:
            f[i] += 1
            if f[i] <= factors[i][1]:
                break
            f[i] = 0
            i += 1
            if f >= factors:
                return


    yield 1, n
    for i in xrange(2, math.floor(math.sqrt(n))):
        if n%i==0:
            yield i
        yield n/i
    return n

print divisors(21)
