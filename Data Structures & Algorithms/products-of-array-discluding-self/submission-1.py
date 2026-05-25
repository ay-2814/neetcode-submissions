class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # Approach 1: do using division to get the result
        # prod_array = 1
        # for num in nums:
        #     prod_array *= num
        # print(prod_array)

        # res = []
        
        # for ind_o in range(len(nums)):
        #     # print(ind_o)
        #     new_prod = 1
        #     for ind_i in range(len(nums)):
        #         if ind_i == ind_o:
        #             continue
        #         new_prod *= nums[ind_i]
        #     res.append(new_prod)

        # return res

        # Approach 2, 2 linear passes while storing pre and post fix in the result array itself

        res = [1] * len(nums)
        print(res)

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        
        postfix = 1
        # reverse transversing the array
        for i in range(len(nums)-1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]

        return res

        