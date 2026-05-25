class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_visited = {} # To store index:value

        for ind, num in enumerate(nums):
            # Calc diff and check if diff is already in the hashmap
            diff = target - num
            if diff in nums_visited:
                return [nums_visited[diff],ind]
            # Else, add the number to the hashmap
            nums_visited[num] = ind
        