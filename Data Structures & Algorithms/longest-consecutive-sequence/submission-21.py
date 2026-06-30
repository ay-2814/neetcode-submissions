class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        longest_seq_len = 0

        for num in nums:
            print(f"num : {num}")
            seq_len = 0
            if (num-1) not in nums:
                # We can now  think of starting the sequence
                seq_len +=1
                while (num + seq_len) in nums:
                    print(f"{num + seq_len} is present")
                    seq_len+=1
                    print(f"new sequence length is: {seq_len} ")
                    print(f"now checking if {num+seq_len} is in the sequence")
                
                # if (num+seq_len) in nums:
                #     print(f"it is, extending the sequence length.")
                #     seq_len +=1
                #     print(f"new seq_len is : {seq_len}")
                
                # if (seq_len > longest_seq_len):
                #     print(f"new longest seq found!")
                #     print(f"it is {seq_len}")
                #     longest_seq_len = seq_len
                longest_seq_len = max(seq_len, longest_seq_len)
        
        return longest_seq_len
