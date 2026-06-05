class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = []
        dic = {}
        for i in range(len(strs)):
            s = strs[i]
            freq = [0] * 26
            for j in s:
                freq[ord(j) - ord('a')] +=1
            key = tuple(freq)
            if key in dic:
                dic[key].append(s)
            else:
                dic[key] = [s]
        return list(dic.values())
            
        