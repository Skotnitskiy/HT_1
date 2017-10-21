"""Write a script to remove duplicates from Dictionary"""

d = {'a': 25, 'b': 25, 'c': 70, 'd': 0, 'e': 8}
result = {}
for key, value in d.items():
    if value not in result.values():
        result[key] = value
print(result)
