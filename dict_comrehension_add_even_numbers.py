#Adding the square of even numbers to a dictionary
numbers=range(10)
new_dict={}
#dict comprehension
new_dict= {i:i**2 for i in numbers if i % 2 == 0}
print(new_dict)
