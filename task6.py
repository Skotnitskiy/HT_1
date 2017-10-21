"""Write a script to check whether a specified value is contained in a group
      of values.
        Test Data :
        3 -> [1, 5, 8, 3] : True
        -1 -> (1, 5, 8, 3) : False"""

numbers_list = [1, 5, 8, 3]
numbers_tuple = (1, 5, 8, 3)
print(3 in numbers_list)
print(-1 in numbers_tuple)
