class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s_lower = "".join(filter(str.isalnum, s))
        i = 0
        j = len(s_lower) - 1

        while i<=j:
            print(s_lower[i], s_lower[j])
            if s_lower[i] != s_lower[j]:
                return False
            i+=1
            j-=1
        return True
        