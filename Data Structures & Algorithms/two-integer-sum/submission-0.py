class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # sum = 0
        # ind1 = ind2 = 0
        # for num1 in nums:
        #     ind1 = nums.index(num1)
        #     sum = num1
        #     for num2 in nums[ind1:]:
        #         if num2 + num1 == target:
        #             ind2 = nums.index(num2)
        #     break
        # return [ind1, ind2]
        # The above is O(n^2) complexity

        # Other approach is using HashMap and one pass of the array
        numSoFar = {} # val : index
        for i, n in enumerate(nums):
            # print(n,i)
            diff = target - n
            if diff in numSoFar:
                return[numSoFar[diff], i]
            # Update HashMap
            numSoFar[n] = i


