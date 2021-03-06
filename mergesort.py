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

# Sets file path
filepath = 'data.txt'

newFileStr = ''
# opens file and stores in fp
with open(filepath) as fp:
    # reads first line of file
    line = fp.readline()
    # while there are still existing lines
    while line:
        # parse line to strip of \n's an store in array
        nums = [int(x) for x in line.strip('\n').split(' ')]
        # get length of nums
        numslen = nums.pop(0)
        # perform insertion sort on array of nums
        mergeSort(nums, 0, numslen-1)
        # for each num in num array, write to output file
        for num in nums:
            newFileStr += str(num) + ' '
        newFileStr += '\n'
        # read next line
        line = fp.readline()

# write string to output file
with open('merge.out', 'w') as output:
    output.write(newFileStr)