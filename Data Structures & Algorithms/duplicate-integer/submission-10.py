class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # print(f"type of the input nums: {type(nums)}")
        hashSet = set()

        for num in nums:
            if num in hashSet:
                return True
            else:
                hashSet.add(num)
        return False
