1class Solution(object):
2    def convertToTitle(self, columnNumber):
3        letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m',
4           'n','o','p','q','r','s','t','u','v','w','x','y','z']
5        result=""
6        if columnNumber < 27:
7            return str(letters[columnNumber-1]).upper()
8        else:
9            while columnNumber > 0:
10                columnNumber-=1
11                rem=columnNumber%26
12                result = letters[rem] + result
13                columnNumber //= 26
14        return result.upper()
15
16                    
17        