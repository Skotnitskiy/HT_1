"""Write a script to remove an empty tuple(s) from a list of tuples
Sample data: [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
        Expected output: [('',), ('a', 'b'), ('a', 'b', 'c'), 'd']"""
lst = [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
lst = [k for k in lst if k != ()]
print(lst)
