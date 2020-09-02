from math import sqrt

data = [1,2,3]

#total 
def total():
    return (len(data))

#summation
def summation():
    sum = 0
    for x in data:
        sum += x
        x += 1
    return sum

#mean
def mean():
    sum = 0
    for x in data:
        sum += x
        x += 1
    average = sum / len(data)
    return average

#variance
def variance():
    for x in range(0, len(data)):
        sum = (data[x] - mean())**2
        sum += sum
        x += 1
    return sum / (total() - 1)

#standard deviation
def deviation():
    deviation = variance()
    return sqrt(deviation)

#median
def median():
    if len(data) % 2 == 0:
        placement = int(len(data) / 2)
        median = (data[placement] + data[placement - 1]) / 2
        return median 

    if len(data) % 2 == 1:
        placement = int((len(data) - 1) / 2)
        median = data[placement]
        return median

#minimum
def minimum():
    minimum = data[0]
    for x in range(0, len(data)):
        if data[x] < minimum:
            minimum = data[x]
            x += 1
    return minimum

#maximum
def maximum():
    maximum = data[0]
    for x in range(0, len(data)):
        if data[x] > maximum:
            maximum = data[x]
            x += 1
    return maximum

print("There are a total of", total(), "numbers")
print("The sum is",summation())
print("The average is", mean())
print("The variance is", variance())
print("The standard deviation is", deviation())
print("The median is", median())
print("The minimum value is", minimum())
print("The maximum value is", maximum())
    