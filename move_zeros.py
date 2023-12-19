nums = [1,0,2,12]
slow = 0
for fast in range(len(nums)):
    if nums[fast] != 0:
        nums[slow],nums[fast] = nums[fast], nums[slow]
        slow += 1

