class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashS = set()
        for i in nums: 
            if i in hashS: 
                return True 
            hashS.add(i)
        return False