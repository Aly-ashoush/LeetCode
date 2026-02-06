1class Solution(object):
2    def longestCommonPrefix(self, strs):
3        if not strs :
4            return ""
5        common = strs[0]
6        for i in strs[1:]:
7            while not i.startswith(common):
8                common=common[:-1]
9                if common =="":
10                    return ""
11        return common
12
13