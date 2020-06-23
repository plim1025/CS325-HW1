from random import randrange
from time import time

# sorts array of numbers in place
# input: nums: List[] - array of numbers
# output: None
def insertSort(numArr):
    # starting at second element, traverse list
    for i in range(1, len(numArr)):
        # store current list's value
        cur = numArr[i]
        # store last index where list is sorted
        j = i-1
        # search for correct position for cur
        while j >= 0 and cur < numArr[j]:
            # shift item to make room for cur
            numArr[j+1] = numArr[j]
            j -= 1
        # found correct index, now store in array
        numArr[j+1] = cur

# start timer
start = time()
# size of test
n = 5000
# fill array with zeroes
numArr = [0] * n
# fill array with random nums between 0 - 10,000
for i in range(n):
    numArr[i] = randrange(10000)
# sort array using insert sort
insertSort(numArr)
# stop timer
end = time()
# print timer
print('Numbers: ' + str(n))
print('Timer: ' + str(end - start))