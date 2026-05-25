class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freq_count = {} # dict with key as num and value as freq of the number
        
        count_freq = [ [] for _ in range(len(nums)+ 1) ] # List where index corresponds to the frequency and the value at the index correponds to a list of values with that frequenies

        # print(count_freq)
        res = []

        # Step 1, calculate the frequencies of each number
        for num in nums:
            freq_count[num] = 1+ freq_count.get(num, 0)
        print("freq_count",freq_count)

        # Step 2, create a list with key as freq and list of numbers with that freq as the value

        for num, cnt in freq_count.items():
            count_freq[cnt].append(num)
        print(count_freq)


        # Step 3, remove the elements from the array where index = k (given value)
        for i in range(len(count_freq)-1, 0, -1):
            print('value of i and count_freq[i]: ', i, count_freq[i])
            for num in count_freq[i]: # this only enters the loop if freq_count[i] is non-empty
                res.append(num)
                print("current res: ", res)
            if len(res) == k:
                return res

    
        