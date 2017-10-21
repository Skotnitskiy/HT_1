"""Write a script to replace last value of tuples in a list
        Sample list: [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
        Expected Output: [(10, 20, 100), (40, 50, 100), (70, 80, 100)]"""

lst = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
j = 0
for i in lst:
    sublist = list(i)
    sublist.pop()
    sublist.append(100)
    lst[j] = tuple(sublist)
    j = j + 1
print(lst)
