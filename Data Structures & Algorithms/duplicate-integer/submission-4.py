class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        n = set()
        for i in nums:
            n.add(i)
        if len(nums) == len(n):
            return False
        return True