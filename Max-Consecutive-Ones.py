1class Solution(object):
2    def findMaxConsecutiveOnes(self, nums):
3        counter=0
4        maximum=0
5        for i in range (len(nums)):
6            if nums[i]==1:
7                counter+=1
8                maximum=max(maximum,counter)
9            else:
10                counter=0
11        return maximum            
12
13            
14        