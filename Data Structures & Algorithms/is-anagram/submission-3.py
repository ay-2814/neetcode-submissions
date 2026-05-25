class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # Optimized HashTable

        # Check length mismatch first
        if len(s) != len(t):
            return False
        
        # creating an array to store all 26 lowercase alphabets' count
        count_char = [0] * 26
        print(count_char)

        for i in range(len(s)):
            count_char[ord(s[i]) - ord('a')] += 1
            count_char[ord(t[i]) - ord('a')] -= 1
        
        for val in count_char:
            if val!=0:
                return False
        
        return True
        