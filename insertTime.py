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
        while j >= 0 and cur > numArr[j]:
            # shift item to make room for cur
            numArr[j+1] = numArr[j]
            j -= 1
        # found correct index, now store in array
        numArr[j+1] = cur

# size of tests
nums = [1000, 2000, 3000, 4000, 5000, 6000, 7000]
for n in nums:
    # fill array with zeroes
    numArr = [0] * n
    totalTime = 0
    # take the average of 100 trials for each number
    for i in range(100):
        # fill array with random nums between 0 - 10,000
        for i in range(n):
            numArr[i] = randrange(10000)
        # start timer
        start = time()
        # sort array using insert sort
        insertSort(numArr)
        # stop timer
        end = time()
        totalTime += (end - start)
    # print timer
    print('Numbers sorted: ' + str(n))
    print('Time taken: ' + str(totalTime/100))
