class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ans = 0
        max_freq=0
        d = {}
        i = 0
        for j in range(len(s)):
            window_size = j-i + 1
            d[s[j]] = d.get(s[j], 0) + 1
            max_freq = max(max_freq, d[s[j]])
            if (window_size - max_freq) <= k:
                ans = max(ans, window_size)
            else:
                d[s[i]] = d[s[i]] - 1
                i+=1

        return ans;