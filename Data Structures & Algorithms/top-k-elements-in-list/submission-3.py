class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_count = {}
        freq = [[] for i in range(len(nums)+1)]

        for num in nums:
            num_count[num] = 1 + num_count.get(num, 0)
        
        for n, c in num_count.items():
            freq[c].append(n)
        
        res = []

        for i in range(len(freq)-1,0,-1):
            #  print(f"i: {i}")
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res

        
        