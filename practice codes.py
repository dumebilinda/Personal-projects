text1= "Zero is equal to "
# the str function converts an integer to string
text2 = str(0)
print(text1 + text2)
print("Welcome to my interactive tutorial")
name = input("please enter your name")
# in the next line i have to specify the kind of input i am expecting from the age variable
age = int(input("please enter your age"))
city = input("please enter your city")
email = input("enter your email address")
print(f"Thank you very much {name}, you will be contacted at {email} stay blessed! ")
# some codes on lists
a = [22, 50, 30, 60, 90]
a = [22, 50, 30, 60, 90]
# show the value in index 0 for list a
print(a[0])
b = [56, 87,40, 33, 78]
# create a new list c which is the sum of a and b
c = a + b
# display the new list c
print(c)
# show the value in index 0 for list c
print(c[4])
# Also, lists are mutable, meaning that the elements of a list can be changed using the index. for instance
# the first element of the list b is changed from 56 to 9
b = [56, 87,40, 33, 78]
b[0] = 9
print(b)
# find out the number of elements in the list, the len function is used ie:
print(len(b))
# to slice a list:
print(a[0:2])
# arithmetic operations
result = (5%2)
print(result)
# example a program that calculates simple interest
P=100
N=2
R=3
SI=(P*N*R)/100
print(SI)
# to access the character in a string and display an index:
string_var = "python variable"
print(string_var[3])
# to get the size of the variable 'string_var' we use the len function:
print(len(string_var))
# the last character in the string can be accessed by subtracting 1 from the output of the len function:
print(string_var[len(string_var)-1])
# To access the range of characters in a string or create substrings, use the range slice [:] operator:
print(string_var[2:5])


