class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        # Convert the list into a HashSet
        set_num = set(nums)
        
        # Check their lengths
        if len(set_num) != len(nums):
            return True
        
        return False
        