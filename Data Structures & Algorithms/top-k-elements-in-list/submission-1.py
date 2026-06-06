class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        for i in nums:
            dic[i] = dic.get(i, 0) + 1

        freq = [[] for _ in range(len(nums) + 1)]
        for key, val in dic.items():
            freq[val].append(key)

        res = []
        for i in range(len(freq) -1, 0, -1):
            for j in freq[i]:
                res.append(j)
                if len(res) == k:
                    return res