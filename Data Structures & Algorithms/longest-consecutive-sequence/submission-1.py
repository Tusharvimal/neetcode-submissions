class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set()
        for i in nums:
            seen.add(i)

        ans = 0
        for i in nums:
            temp = 0
            if i-1 not in seen:
                j = i
                while j in seen:
                    temp+=1
                    j = j+1
                ans = max(ans, temp)
        return ans 
        