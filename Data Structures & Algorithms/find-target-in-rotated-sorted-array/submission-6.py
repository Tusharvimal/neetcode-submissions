class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i = 0
        j = len(nums) - 1
        while (i < j):
            mid = (i + j) // 2
            if (nums[j] < nums[mid]):
                i = mid + 1
            else:
                j = mid
        pivot = i
        i = 0
        j = len(nums) - 1
        if (target >= nums[pivot] and nums[j] >= target):
            i = pivot
            j = len(nums) - 1
        else:
            j = pivot - 1

        while (i <= j):
            mid = (i + j) // 2
            if (nums[mid] == target):
                return mid
            if (nums[mid] < target):
                i = mid + 1
            else:
                j = mid -1
        return -1