class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        # # Approach, similar to two sum, 
        # # loop through the number, check if num+1 exists in the set and if it does, extend the sequence
        # num_set = set(nums)
        # # print(num_set)
        # longest_seq = []

        # for i in num_set:
        #     if (i+1 in num_set) or (i-1 in num_set):
        #         # print("appending ", i, "into list because ", i-1 , "or", i+1, "is in the set")
        #         longest_seq.append(i)
        # # print(longest_seq)
        # return len(longest_seq)

        # Solving after watching the solution
        num_set = set(nums)
        longest = 0

        for i in num_set:
            print("current i:", i)
            if (i-1) not in num_set:
                print("Previous number ", i-1,"is not in set")
                current_num = i # Start of sequence
                current_streak = 1
                
                while (current_num + 1) in num_set:
                    current_num += 1
                    print("current_num updated to:", current_num)
                    current_streak +=1
                    print("curren")
                longest = max(longest, current_streak)
        return longest

            






            


        