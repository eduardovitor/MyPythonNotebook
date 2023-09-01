

def twoSum(nums, target):
    sum_nums = 0
    for i in range(0,len(nums)-1):
        for j in range(i+1, len(nums)):
            if nums[i]+nums[j]==target:
                return [i,j]
