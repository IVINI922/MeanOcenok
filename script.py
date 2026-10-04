nums = []
a = 5
mean = 0
while a>1 & a!='':
    b = input()
    try:
        a = int(b)
    except:
        break
    nums.append(a)
for n in nums:
    mean += n
mean /= len(nums)
print(nums)
print(mean)
while a>1 & a!='':
    b = input()
    try:
        a = int(b)
    except:
        break
    nums.append(a)
mean = 0
for n in nums:
    mean += n
mean /= len(nums)
print(nums)
print(mean)
input()