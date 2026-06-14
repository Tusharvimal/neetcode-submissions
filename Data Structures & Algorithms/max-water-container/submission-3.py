class Solution:
    def maxArea(self, heights: List[int]) -> int:
        ans = 0

        temp = 0
        i = 0
        j = len(heights) - 1
        while i < j:
            temp = min(heights[i], heights[j]) * (j - i)
            ans = max(ans, temp)

            if(heights[i]< heights[j]):
                i+=1
            else:
                j-=1
        return ans 
        