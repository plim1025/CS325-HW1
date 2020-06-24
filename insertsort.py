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

# Sets file path
filepath = 'data.txt'
# String to write to output file
newFileStr = ''
# opens file and stores in fp
with open(filepath) as fp:
    # reads first line of file
    line = fp.readline()
    # while there are still existing lines
    while line:
        # parse line to strip of \n's an store in array
        nums = [int(x) for x in line.strip('\n').split(' ')]
        # perform insertion sort on array of nums
        insertSort(nums)
        # for each num in num array, write to output file
        for num in nums:
           newFileStr += str(num) + ' '
        newFileStr += '\n'
        # read next line
        line = fp.readline()

# write string to output file
with open('insert.out', 'w') as output:
    output.write(newFileStr)