x = [1,2,3,4,5,6,7,8,9,10]
for temp in x:
    if temp % 2 == 0:
        x.remove(temp)

print(x)