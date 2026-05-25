class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        # Create a set
        # see if the the length of set is different from the original list
        set_a = set(nums)
        # print(set_a)

        if(len(set_a) != len(nums)):
            return True
        
        return False
         