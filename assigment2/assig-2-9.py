nums = []

for i in range(3):
    num = int(input(f'Enter marks for test{i+1} : '))
    nums.append(num)

nums.sort()

print(f'Average of best two test marks out of three test\'s marks is {nums[2]/2+nums[1]/2}')
