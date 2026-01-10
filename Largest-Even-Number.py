1class Solution(object):
2    def largestEven(self, s):
3        x=s.rfind("2")
4        if x==-1:
5            return ""
6        else:
7            return s[:x+1]        
8
9        