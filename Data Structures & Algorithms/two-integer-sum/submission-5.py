class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        prevSeen = {}

        for i, num in enumerate(nums):
            diff = target - num
            if diff in prevSeen:
                return [prevSeen[diff], i]
            prevSeen[num] = i # Append if the pair not found yet
