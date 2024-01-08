x = [11,-21,0,45,66,-93]
positiveCount = 0
negativeCount = 0
ZeroCount = 0

for temp in x:
    if temp > 0:
        positiveCount = positiveCount + 1
    elif temp < 0 :
        negativeCount = negativeCount + 1
    else :
        ZeroCount = ZeroCount + 1
print(x)
print("Number of Positive NO is ", positiveCount)
print("Number of Negative NO is ", negativeCount)
print("Number of 0s ", positiveCount)
