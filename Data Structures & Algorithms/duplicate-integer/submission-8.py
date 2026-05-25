class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # print("abhiraj")
        seen_nums = set()
        for num in nums:
            # print(num)
            if num in seen_nums:
                return True
            else:
                seen_nums.add(num)
                print(f"current num is {num} and seen_nums is {seen_nums}")
        return False
