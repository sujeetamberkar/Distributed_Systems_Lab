x = 10
count = 0

while count < x:
    print(count)
    count = count + 1
else:
    print("Loop Esceuted without any break statement")



print("#######################################")
# If you want to execute, execute completely or dont 
while count < x:
    print(count)
    if count == 4:
        break
    count = count + 1

else:
    print("The loop was terminted by a break statement")