#Obviously, we could do this with a bunch of nested loops. This would take forever. I remember seeing an exhibit at the MIT museum showing how, in a series of twelve gears, it was possible for the outmost gear to be spinning blurringly fast while the inmost gear took a century to turn one rotation. Don't feel like killing my computer, or growing a beard, while trying to solve this one.

#Let's consider other possible methods. With a 3D list, we could have it walk through the list using a loop that 


num_array = [[75, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
             [95, 64, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
             [17, 47, 82, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
             [18, 35, 87, 10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
             [20, 4, 82, 47, 65, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
             [19, 1, 23, 75, 03, 34, 0, 0, 0, 0, 0, 0, 0, 0, 0]
             [88, 2, 77, 73, 07, 63, 67, 0, 0, 0, 0, 0, 0, 0, 0]
             [99, 65, 4, 28, 6, 16, 70, 92, 0, 0, 0, 0, 0, 0, 0]
             [41, 41, 26, 56, 83, 40, 80, 70, 33, 0, 0, 0, 0, 0, 0]
             [41, 48, 72, 33, 47, 32, 37, 16, 94, 29, 0, 0, 0, 0, 0]
             [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14, 0, 0, 0, 0]
             [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57, 0, 0, 0]
             [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48, 0, 0]
             [63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31, 0]
             [4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23]]

result_list = []
for y in xrange (1, 15):
    for x in xrange (1, 15):
        for x2 in xrange (x-1, x+1):
        run_sum += num_array[y][x]
result_list.append(run_sum)
run_sum = 0

print max(result_list[0])

#Endgame is to append all the resultant values to a list, run the max method on the list, then print the max.
