class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic = {}
        dic2 = {}
        for i in s:
            dic[i] = dic.get(i,0) + 1

        for i in t:
            dic2[i] = dic2.get(i,0) + 1

        return dic==dic2

        