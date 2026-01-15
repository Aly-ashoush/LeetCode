1class Solution(object):
2    def removeElement(self, nums, val):
3        counter=0
4        for i in range(len (nums)):
5            if nums[i] != val:  
6                nums[counter]=nums[i]
7                counter+=1
8        return   counter
9        