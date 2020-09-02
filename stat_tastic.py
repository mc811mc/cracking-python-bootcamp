#import data
data = 'sample_dataset'
with open(data) as file:
    for line in file:
        pass
    
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

#mean (average)
def mean():
    sum = 0
    for x in data:
        sum += x
        x += 1
    average = sum / len(data)
    return average

#standard deviation
def std():
    sum = 0
    for x in data:
        sum += x
        x += 1
    average = sum / len(data)
    for x in data:
        diff = x - average
        sqt  = diff ** 2
        std += sqt / len(data)
    return std


