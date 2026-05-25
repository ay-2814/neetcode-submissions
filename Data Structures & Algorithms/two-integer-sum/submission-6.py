class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # print(f"nums: {nums}");
        numsSeen = {} # num (key) : index (value)

        for ind, num in enumerate(nums):
            diff = target - num
            if diff in numsSeen:
                return ([numsSeen[diff], ind])
                # return ([ind, numsSeen[diff]])
            else:
                numsSeen[num] = ind

