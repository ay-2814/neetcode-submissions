class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # print(f"nums array: {nums}")

        # Solution 1: Create a set and see if sets length is same as nums array
        distinctNums = set(nums)
        # print(f"distinctNums, {distinctNums}")
        if len(distinctNums) == len(nums):
            return False
        return True