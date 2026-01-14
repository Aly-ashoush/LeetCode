1class Solution(object):
2    def checkPrimeFrequency(self, nums):
3        frequency={}
4        primes = {
5    2, 3, 5, 7,
6    11, 13, 17, 19,
7    23, 29, 31, 37,
8    41, 43, 47, 53,
9    59, 61, 67, 71,
10    73, 79, 83, 89,
11    97
12}
13        for i in nums:
14            if i  in frequency:
15                frequency[i]+=1
16            else:
17                frequency[i]=1
18        for j in frequency.values():
19            if  j in primes:
20                return True
21        return False    
22
23
24                
25
26                
27