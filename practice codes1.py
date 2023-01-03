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
# to concatenate strings, use the + operator eg:
print("I "+"love "+"Wisdom "+"the sun of my heart")
# to repeat strings use the * operator eg:
print(("I "+"love "+"Wisdom "+"the sun of my heart")*5)
# to print the entire list in upper and lowercase, use the upper() and lower() funtions eg:
string_var = "python variable"
print(string_var.upper())
#To print non-string characters as string characters, use the str() function eg: to print "My monthly income is 4500 euros"
my_income = 4500
print("My monthly income is " + str(my_income)+ " euros")
# If statements executes the body of the code if the condition is true. eg:
ax = 21
bx = 10
if ax > bx:
    print("na wa oh")
else:
        print("this life balance well")
# To test numerous conditions, we use the elif statement eg:
ax = 21
bx = 10
bz = 13
if ax > bx:
    print("ax is greater than bx")
elif ax < bz:
        print("ax is less than bz")
else:
    print("Abeg leave me alone")
# another example
number_of_girls = 50
number_of_boys = 55
if number_of_girls > number_of_boys:
    print("wahala dey")
elif number_of_girls < number_of_boys:
    print("God of the booless epp their life")
else:
    print("las las everybody go chop breakfast")





