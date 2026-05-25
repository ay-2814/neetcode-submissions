class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # list(s).sort()
        # list(t).sort()
        # # print(s,t)
        if(sorted(s) == sorted(t)):
            return True
        return False
