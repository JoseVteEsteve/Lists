#Given a list of numbers, find and print all elements that are an even number.
#In this case use a for-loop that iterates over the list, and not over its indices! That is, don't use range() 

list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o"]
n = len(list)
for i in list:
        if list.index(i) % 2== 0:
            print(i)