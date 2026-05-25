class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        print(f"the string: {s}")

        # Brute force
        s_stripped = ""
        for c in s:
            if c.isalnum():
                s_stripped += c.lower()
        
        reversed_s = s_stripped[::-1]
        print(f"reversed_s {reversed_s}")
        return (s_stripped == reversed_s)