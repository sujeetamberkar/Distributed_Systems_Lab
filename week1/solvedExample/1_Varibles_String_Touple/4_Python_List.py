list = [ 'abcd', 786 , 2.23, 'john', 70.2 ]
tinylist = [123, 'john']
print (list) # Prints complete list
print (list[0]) # Prints first element of the list
print (list[1:3]) # Prints elements starting from 2nd till 3rd
print (list[2:]) # Prints elements starting from 3rd element
print (tinylist * 2) # Prints list two times
print (list + tinylist) # Prints concatenated lists

# Functions & Methods in LIST
list = ['physics', 'chemistry', 1997, 2000]
list.append("maths")
print(list)
del(list[2])
print(list)

print("physics" in list)
print("Length of the list is ", len(list))
print("No of times the word 'physics' " , list.count('physics'))
list.pop()
print(list)

list = ['physics', 'chemistry', 1997, 2000]
list.insert (2, 'maths')

list = ['physics', 'chemistry', 1997, 2000]
list.remove("chemistry")
print(list)

list.reverse()
print(list)
