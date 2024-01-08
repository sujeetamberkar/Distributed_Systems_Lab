total = 0
number = int(input('Enter a number: '))
# add numbers until number is zero
while number != 0:
    total += number # total = total + number
    # take integer input again
    number = int(input('Enter a number: '))
print('total =', total)
