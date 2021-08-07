#Print function(comments)
print("Hello, World!")

#variables
a = 5
b = "try"
c = 2.0
print(a)

#assingment of multiple values
x, y, z = "1", "2", "3"
print(x)
print(y)
print(z)

#text combine
x = "python"
print("Zen of " + x)

#global variable
x = "python"

def func():
  print("Zen of " + x)

func()

#knowing the data types
print(type(a))   #int
print(type(c))   #float

#casting
p = float(3)    #p will be 3.0
q = int(7.77)   #q will be 7

#strings
a = "Zen, of, python"
print(type(a))

txt = "We are the so-called \"Vikings\" from the north."
print(txt)                                  #To insert characters that are illegal in a string, use an escape character.

a = "Hlo"
b = "Sir"
c = a + b
print(c)                                    #To concatenate two strings you can use the + operator.

age = 36
txt = "My name is Jarvis, and I am {}"
print(txt.format(age))                      #Use the format() method to insert numbers into strings:

#Boolean
a = 2
b = 1

if a > b:
  print("a is greater than b")
else:
  print("a is not greater than b")

#operators
print(10 + 5)                       #addition

print(10 - 5)                       #Subtraction

print(10 * 5)                       #Multiplication

print(10 / 5)                       #Division

print(10 % 5)                       #Modulus

print(10**5)                       #Exponentiation

print(10 // 5)                       #Floor division

#list
list = ["abc", 34, True, 40, "male"]
print(type(list))
print(list[1])                #List items are indexed and you can access them by referring to the index number

print(list[2:5])              #You can specify a range of indexes by specifying where to start and where to end the range.

list.append("orange")
print(list)                   #Using the append() method to append an item

list.insert(2, "new")
print(list)                   #Insert an item as the third position

top = ["19", "pineapple", "10"]
list.extend(top)
print(list)                   #Add the element top to list

list.remove("10")
print(list)                   #The remove() method removes the specified item

list.pop(1)
print(list)                   #The pop() method removes the specified index.


#Create a Tuple
tuple = ("apple", "banana", "cherry")
print(tuple)

#Dictionary
#Dictionaries are used to store data values in key:value pairs.

dict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(dict)