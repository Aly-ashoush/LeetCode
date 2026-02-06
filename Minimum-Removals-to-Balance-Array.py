1class Solution(object):
2    def minRemoval(self, nums, k):
3        nums.sort()
4        n = len(nums)
5        minmum = 0
6        max_len = 1
7
8        for r in range(n):
9            while nums[r] > k * nums[minmum]:
10                minmum += 1
11            max_len = max(max_len, r - minmum + 1)
12
13        return n - max_len
14