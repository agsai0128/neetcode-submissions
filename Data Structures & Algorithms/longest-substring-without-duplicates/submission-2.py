class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        
        res = 1
        maxLen = 1

        l, r = 0, 1

        while r < len(s):
            if s[r] not in s[l:r]:
                maxLen += 1

                res = max(res, maxLen)
            else:
                l += 1
                r = l
                maxLen = 1
            r += 1
        return res
