import numpy as np 
import random

print(random.choice([1,2,3,4,10,20]))  # Pick any random number from the list 
print(random.choice('Python')) # A random char from the given string 


print(random.randrange(25,30)) # A random number between the lower and upper limit 
print(random.randrange(25,50,2)) # A random number between the lower and upper limit  with step 2 

print(random.random()) # Random number between 0 and 1 
print(random.uniform(5,10)) # A random floating point number between the upper limit and lower limit 

a = [1,2,3,4,5]
random.shuffle(a)#, will shuffle the list elements
print(a)



# Seed a random Number 
random.seed(10)
number1 = random.random()
print(number1)
number1 = random.random()
print(number1)