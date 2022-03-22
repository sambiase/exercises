'''
    List Comprehension with If statement
    Only prints numbers greater than 6 in a range of 10 elements
'''

res = [int(i) for i in range(10) if i > 6 ]
print(res)