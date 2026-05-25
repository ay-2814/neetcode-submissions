class Solution:

    def encode(self, strs: List[str]) -> str:
        res_encode = ''
        for s in strs:
            res_encode += (str(len(s)) + "#" + s)
        # print(res_encode)
        return res_encode


    def decode(self, s: str) -> List[str]:
        res_decode = []
        i = 0
        # print("initial i:", i)
        while i < len(s):
            print("current i, i denotes first index pointer", i)
            j = i
            while s[j] != "#":
                j += 1
                print("j after # is found", j)
            len_str = int(s[i:j])
            print("len of next word is: ", len_str)
            res_decode.append(s[j+1 : j+1 + len_str])
            i = j + 1 + len_str
        return res_decode