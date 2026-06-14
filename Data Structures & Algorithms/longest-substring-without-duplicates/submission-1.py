class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        st = ""
        ans = 0
        for i in range(len(s)):
            if s[i] in st:
                ind = st.find(s[i])
                st = st[ind + 1:]
                st+=s[i]
                continue
            st += s[i]
            ans = max(len(st), ans)
        return ans
        