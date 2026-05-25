class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # Step 1, make a dict/HashMap of all the numbers and their frequency -> number : frequency
        count_num = {}
        for num in nums:
            count_num[num] = 1 + count_num.get(num, 0)
        # Check print
        # print(count_num)

        # Step 2, make a dict/HashMap of the freq where index is freq and val is a list of all the numbers with that frequency
        freq = [[] for i in range(len(nums) + 1)]
        # print(len(freq), len(freq[0]))
        for num, cnt in count_num.items():
            # print(num, cnt)
            freq[cnt].append(num)
        
        print("len freq:",len(freq))
        # Step 3, traverse that list in step 2 backward till k values
        res = []
        for i in range(len(freq) - 1,0, -1):
            # print(i)
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res

       