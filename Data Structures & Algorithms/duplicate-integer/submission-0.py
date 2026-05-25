class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
         # print(nums)
         s = set(nums)
         if len(s)==len(nums):
            return False
         else:
            return True