class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d = {}
        ans = 0
        left = 0
        for i in range(len(s)):
            if s[i] in d:
                left = max(left, d[s[i]] + 1)
            ans = max(ans, (i - left + 1))
            d[s[i]] = i

        return ans 
            