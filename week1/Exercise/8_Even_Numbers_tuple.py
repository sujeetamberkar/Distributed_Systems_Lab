myTuple = (1,2,3,4,5,6,7,8,9)
temp =[]
for i in myTuple:
    if i % 2 ==0:
        temp.append(i)
temp = tuple(temp)
print(temp)
