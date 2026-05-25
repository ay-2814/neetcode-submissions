class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ''
        for s in strs:
            res += str(len(s)) + "#" + s
        print(res)
        return res
            

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            len_str = int(s[i:j]) 
            # str[i:j] captures the integer which represents the length of the upcoming string
            res.append(s[j+1 : j+ len_str+1])
            i = j + 1 + len_str
        
        return res
