class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        # Convert array to hashSet (Set is not ordered)
        numSet = set(nums)
        print(f"numSet = {numSet}")
        longestSeq = 0

        for num in numSet:
            Seq = []
            if (num-1) not in numSet:
                print(f"Found candidate for beginning of Seq: {num}")
                Seq.append(num)
                print(f"length of current Seq: {len(Seq)}")
                while (num+len(Seq)) in numSet:
                    print(f"Checked if {num+len(Seq)} is in input and yes it is!")
                    print(f"Appending {num+len(Seq)} to the sequence")
                    Seq.append(num+len(Seq))
                    print(f"Sequence now is: {Seq} and its length is: {len(Seq)}")
            if len(Seq) > longestSeq:
                longestSeq = len(Seq)
        return longestSeq

                
            
