class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        # In solution 1 : making a set and checking if the len of array and set are same, we still have to go through the whole array
        # Would be more efficient to find a way to stop as soon as there is a repitition

        hasSeen = set()

        for num in nums:
            if num in hasSeen:
                return True
            else:
                hasSeen.add(num)
        return False