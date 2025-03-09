class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        check = {}
        max = 0
        left = 0
        for i in range(len(s)):
            if s[i] in check:
                oldleft = left
                left = check[s[i]] + 1
                for n in range(oldleft, left):
                    check.pop(s[n])
            check[s[i]] = i
            if max < (i+1) - left:
                max = (i+1) - left
        return max

            
            
