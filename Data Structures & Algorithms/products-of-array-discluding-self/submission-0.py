class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # Approach 1: do using division to get the result
        prod_array = 1
        for num in nums:
            prod_array *= num
        print(prod_array)

        res = []
        
        for ind_o in range(len(nums)):
            # print(ind_o)
            new_prod = 1
            for ind_i in range(len(nums)):
                if ind_i == ind_o:
                    continue
                new_prod *= nums[ind_i]
            res.append(new_prod)

        return res


        