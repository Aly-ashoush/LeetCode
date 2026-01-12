1class Solution(object):
2    def findLengthOfLCIS(self, nums):
3        counter=1
4        maximum=1
5        for i in range(len(nums)-1):
6
7            if  nums[i] < nums[i+1]:
8                counter+=1
9                maximum=max(maximum,counter)
10            else:
11                counter=1
12        return maximum    
13              
14        