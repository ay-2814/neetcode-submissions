class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        # trying after looking at solution video walkthrough, no code reference tho
        res = [1] * len(nums)
        prefix = 1

        # print(prefix, postfix)

        # Calculating prefix for each number and storing it in res
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
            # print(f"res in prefix calc when i = {i} just finished: {res}")

        postfix = 1
        for i in range(len(nums) -1, -1, -1):
            res[i]*= postfix
            postfix *= nums[i]
        
        return res