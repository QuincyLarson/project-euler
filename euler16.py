a = 2**1000

def sumdigits(n):
    numList = list(str(n))
    total = sum(int(c) for c in numList)
    print total

sumdigits(a)

#credit to bartonc for elegant function http://bytes.com/topic/python/answers/728511-getting-sum-digits-number
