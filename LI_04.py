#Given a list of numbers, find and print the first adjacent elements which have the same sign. If there is no such pair, leave the output blank.

list = [1,-3,7,9,-2,-4,11,10,-8,5,-14,16]
n = len(list)
for i in range(n):
    if (list[i]>0 and list[i - 1] >0 ) or (list[i] < 0 and list[i-1]<0):
        print("The first adjacent elements with the same sign are: " + str(list[i]) + " and " + str(list[i - 1]))
        break
        

