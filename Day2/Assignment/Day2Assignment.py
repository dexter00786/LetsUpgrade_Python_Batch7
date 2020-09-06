# #list
my_list = ["Sachin","Nishant","Mukul","Abhay"] 
print(my_list)

#.append() --> To add an element at the last of the list.
my_list = ["Sachin","Nishant","Mukul","Abhay"]
my_list.append("keshav")
print(my_list)

# .insert() --> To insert an element at a specific position
# let supoose we wanna add Raghav after Nishant, then we have to give index number of position where we want to insert the element
my_list = ["Sachin","Nishant","Mukul","Abhay"]
my_list.insert(2,"Raghav")
print(my_list)

#.extend() --> use to add another list(or ant iterable object) at the end of the list
list1 = [1,2,3,4,5]
list2 = [6,7,8,9,10]
list1.extend(list2)
print(list1)

# length() --> To calculate the length of the list
my_list = ["Sachin","Nishant","Mukul","Abhay"]
res = len(my_list)
print(res)

# remove
my_list = ["Sachin","Nishant","Mukul","Abhay"]
my_list.remove("Abhay")
print(my_list)

# Dictionary
# Creating a dictionary
dist = {"Company":"Maruti suzuki",
		"Model":"WagonR",
		"Fuel":"Petrol"}
print(dist)

# pop() --> remove the item with specified key
dist = {"Company":"Maruti suzuki",
		"Model":"WagonR",
		"Fuel":"Petrol"}
dist.pop("Fuel")
print(dist)

# popitem --> Remove the last inserted key pair 
dist = {"Company":"Maruti suzuki",
		"Model":"WagonR",
		"Fuel":"Petrol"}
dist.popitem()
print(dist)
 
# setdefault --> Return the value of the item with specified key, if key is does not exist the insert the key with specified value
# case1
dist = {"Company":"Maruti suzuki",
		"Model":"WagonR",
		"Fuel":"Petrol"}
dist.setdefault("Model","Baleno")
print(dist)

# Case2
dist = {"Company":"Maruti suzuki",
		"Model":"WagonR",
		"Fuel":"Petrol"}
dist.setdefault("Color","SilverGrey")
print(dist)

# Update() --> insert the specified item to the dictionary
dist = {"Company":"Maruti suzuki",
		"Model":"WagonR",
		"Fuel":"Petrol"}
dist.update({"Transmission":"Mannual"})
print(dist)

# Values --> Return all the values of the dictionary
dist = {"Company":"Maruti suzuki",
		"Model":"WagonR",
		"Fuel":"Petrol"}
x=dist.values()
print(x)

# sets
car = {"Baleno","Ciaz","Nano"}
print(car)

# add() --> to add an element in set
car = {"Baleno","Ciaz","Nano"}
car.add("WagonR")
print(car)

# union()
set1 = {1,2,3,5,6,4}
set2 = {4,8,7,6,9}
z= set1.union(set2)
print(z)

# intersection()
set2 = {4,8,7,6,9}
set1 = {1,2,3,5,6,4}
y = set1.intersection(set2)
print(y)

# issubset()
set2 = {4,8,7,6,9}
set1 = {1,2,3,5,6,4}
p = set1.issubset(set2)
print(p)

# pop()
set1 = {1,2,3,5,6,4}
set1.pop()
print(set1)

# tuples
this_tuple = ("bat", "ball", "cat")
print(this_tuple)

# accessing tuple 
this_tuple = ("bat", "ball", "cat")
print(this_tuple[1])

# nevigating index
this_tuple = ("bat", "ball", "cat")
print(this_tuple[-1])

# range of indexes
this_tuple = ("bat", "ball", "cat")
print(this_tuple[1:2])

# change tuple value
this_tuple = ("bat", "ball", "cat")
q = list(this_tuple)
q[1] = "roy"
this_tuple = tuple(q)
print(this_tuple)

# length
this_tuple = ("bat", "ball", "cat")
print(len(this_tuple))

# STRINGS 
# capitalize
txt = "hello, and welcome to my world."
a = txt.capitalize()
print (a)

# title
txt = "hello, and welcome to my world."
a = txt.title()
print (a)

# .lower()
txt = "hello, and welcome to my world."
a = txt.lower()
print (a)

# islower()
txt = "hello, and welcome to my world."
a = txt.islower()
print (a)

# isupper()
# islower()
txt = "hello, and welcome to my world."
a = txt.isupper()
print (a)
