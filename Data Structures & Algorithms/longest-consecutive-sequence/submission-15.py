class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        # Convert array to hashSet (Set is not ordered)
        numSet = set(nums)
        # print(f"numSet = {numSet}")
        longestSeq = 0

        for num in numSet:
            SeqLen = 0
            if (num-1) not in numSet:
                # print(f"Found candidate for beginning of Seq: {num}")
                SeqLen+=1
                # print(f"length of current Seq: {SeqLen}")
                while (num+SeqLen) in numSet:
                    # print(f"Checked if {num+SeqLen} is in input and yes it is!")
                    # print(f"Appending {num+SeqLen} to the le")
                    SeqLen+=1
                    # print(f"length is: {SeqLen}")
            if SeqLen > longestSeq:
                longestSeq = SeqLen
        return longestSeq

                
            
