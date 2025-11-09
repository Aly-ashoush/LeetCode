class Solution(object):
    def thirdMax(self, nums):
        unique_nums=set(nums)
        unique_nums=sorted(unique_nums,reverse=True)
        if len(unique_nums) < 3:
            return unique_nums[0]
        else:
            return unique_nums[2]    
        
        