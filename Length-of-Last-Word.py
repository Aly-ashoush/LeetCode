class Solution(object):
    def lengthOfLastWord(self, s):
        ans=[]
        ans=s.split()
        return len(ans[-1])
        