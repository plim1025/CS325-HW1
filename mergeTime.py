from random import randrange
from time import time

# mergeSort subroutine - given two sorted subarrays, merge them into one sorted array
# input: nums: List[] - array of numbers, low: int - starting index of first subarray, mid: int - ending index of first subarray, high: int - ending index of second subarray
def merge(nums, low, mid, high):
    # calculate lengths of both subarrays
    n1 = mid-low+1
    n2 = high-mid
    # fill subarrays with zeroes
    leftArr = [0] * n1
    rightArr = [0] * n2
    # fill left subarray
    for i in range(n1):
        leftArr[i] = nums[low+i]
    # fill right subarray
    for i in range(n2):
        rightArr[i] = nums[mid+1+i]
    # initialize counter variables - i for left, j for right, k for overall
    i, j, k = 0, 0, low
    # keep merging until one array runs out
    while i < n1 and j < n2:
        # if left array value is less than right, place it in main array
        if leftArr[i] >= rightArr[j]:
            nums[k] = leftArr[i]
            i += 1
        # if right array value is less than left, place it in main array
        else:
            nums[k] = rightArr[j]
            j += 1
        k += 1
    # fill leftovers of right and left subarray
    while i < n1:
        nums[k] = leftArr[i]
        i += 1
        k += 1
    while j < n2:
        nums[k] = rightArr[j]
        j += 1
        k += 1

# sorts array of numbers in place
# input: nums: List[] - array of numbers
# output: None
def mergeSort(nums, low, high):
    # base case
    if low < high:
        # calculate mid of array to use as reference
        mid = (low+high)//2
        # merge both left and right of array
        mergeSort(nums, low, mid)
        mergeSort(nums, mid+1, high)
        # then merge the two subarrays
        merge(nums, low, mid, high)

# size of tests
nums = [1000, 2000, 3000, 4000, 5000, 6000, 7000]
for n in nums:
    # fill array with zeroes
    numArr = [0] * n
    totalTime = 0
    # take the average of 30 trials for each number
    for i in range(100):
        # fill array with random nums between 0 - 10,000
        for i in range(n):
            numArr[i] = randrange(10000)
        # start timer
        start = time()
        # sort array using insert sort
        mergeSort(numArr, 0, n-1)
        # stop timer
        end = time()
        totalTime += (end - start)
    # print timer
    print('Numbers: ' + str(n))
    print('Time taken: ' + str(totalTime/100))