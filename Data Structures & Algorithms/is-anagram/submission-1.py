class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Approach 1: checking if the sorted strings are same
        s = sorted(s)
        t = sorted(t)

        if (s==t):
            return True
        return False
        