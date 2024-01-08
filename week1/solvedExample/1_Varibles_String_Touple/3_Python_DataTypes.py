a = 5 # Python numbers
b = 4.56
print(5*a)
print(a/2)
print(a**2)
str = 'Hello World!' # Strings 
print(str)
print(str[0]) 
print(str[2:5])
print(str[2:])
print(str * 2)
var1 = 'Hello world!' # Updating a string
print("Updated string: ", var1[1:6]+'Python')

print( "My name is %s and weight is %d kg!" % ('Abay', 55)) 
# Built−in String methods
str = "this is string example wow!!!"
print (str.capitalize())
str = "this is string example ... wow!!!"  
print(str.count('s'))
print(str.find("example")) # will locate the position of searching ‘substring’, (index)
str = "THIS IS STRING EXAMPLE ... WOW!!!"
print (str.lower())
# returns a copy of the string in which all case−based characters have been
# lowercased.
str = "this is string example ... wow!!! this is really string"
print (str.replace("is", "was"))
str = "this is string example ... wow!!!"
print (str.swapcase())
str = "this is string example ... wow!!!"
print (str.title())