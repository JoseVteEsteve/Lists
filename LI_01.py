#Given a list of numbers, find and print all the list elements with an even index number.

list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o"]
n = len(list)
for x in range(0,n + 1):
    if x % 2 == 0:
        print(list[x])