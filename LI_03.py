#given a list of numbers, find and print all the elements that are greater than the previous element.

list = [1,3,7,9,2,4,11,10,8,5,14,16]
n = len(list)
max = 0
for i in range(n):
    if list[i] > list[i - 1]:
        print(str(list[i]) + " is greater than " + str(list[i - 1]))
        
