
# We know it takes 20 steps south and 20 steps east to get from the northwest corner to the southwest corner. Each step is binary - it is one or the other. First let's attempt to use combinatrics to determine how many steps total - !40 / (20! * 20!) - note I didn't fully understand the math behind this problem, so I read up on it here: http://mathforum.org/library/drmath/view/70459.html

def factorial (n):
    if n == 0: return 1#base case
    return n * factorial(n-1)

print factorial(40)/ (factorial(20) * factorial(20))
