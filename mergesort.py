filepath = 'data.txt'
with open(filepath) as fp:
   line = fp.readline()
   while line:
       nums = line.strip('\n').split(' ')
       print(nums)
       line = fp.readline()