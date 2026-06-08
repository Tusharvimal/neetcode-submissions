class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [1] * len(nums)
        n = len(nums)

        running = 1
        for i in range(n):
            ans[i] *= running
            running *= nums[i]

        running = 1
        for i in range(n-1, -1, -1):
            ans[i] *= running
            running*=nums[i]

        return ans

        