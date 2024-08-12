nums = list(map(int,input("Enter the length of the sides of triangle : ").split()))

nums.sort()

if nums[2]**2 == nums[1]**2 + nums[0] ** 2:
    print("It is a right angled triangle")
else:
    print("It is not a right angled triangle")