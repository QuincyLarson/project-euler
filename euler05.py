j = 1 # initial variable assignment
i = 10000 # initial variable assignment 
while (j < 21): # start loop
    if i % j == 0: #checks to see whether evenly divisable # 
        j += 1 #increments j for next iteration
    else: # sends back to i for i iteration
        j = 1
        i += 1
print i
print j

