class Solution:

    def encode(self, strs: List[str]) -> str:
        enc = ""
        for i in strs:
            enc += i + '\n'
        return enc

    def decode(self, s: str) -> List[str]:
        ans = s.split("\n")[:-1]
        return ans 
