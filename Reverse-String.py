class Solution(object):
    def reverseString(self, s):
        ans=[]
        for i in range(len(s)-1,-1,-1):
            ans.append(s[i])
        s[:]=ans

        