k = 0
longest = 5
for n in range (999999, 1, -1):
    i = n
    while i != 1: #
        if i % 2 != 0: #
            i = i*3+1 #
        else: #
            i = i / 2#
        k += 1#
    if k > longest:
        longest = k
        print n
    k = 0
