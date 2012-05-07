sumofsqrs = 0
sumofnums = 0

def sumsqrs(sumofsqrs):
    for i in range (1, 101):
        sumofsqrs += (i * i)
    return sumofsqrs

def sumnums(sumofnums):
    for i in range (1, 101):
        sumofnums += i
    return sumofnums

sumofsqrs = sumsqrs(sumofsqrs)
print sumofsqrs

sumofnums = sumnums(sumofnums)
print sumofnums

sumofnums = sumofnums * sumofnums
print sumofnums

difofsums = sumofsqrs - sumofnums
print difofsums
