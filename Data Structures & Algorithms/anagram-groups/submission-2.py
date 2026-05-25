class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # str_by_len = {}
        # for i in range(len(strs)):
        #     # print(str)
        #     for j in range(i+1, len(strs)):
        #         if len(strs[i]) == len(strs[j]):
        #             str_by_len[len(strs[i])].add([strs[i], strs[j]])

        #             # print(f"{strs[i]} and {strs[j]} are the same length")
        # print(str_by_len) 
        res = defaultdict(list)

        for s in strs:
            # print(f"string being examined: {s}")
            
            char_count = [0] * 26
            # print(f"char_count : {char_count}")
            for c in s:
                char_count[ord(c) - ord("a")] +=1
            
            res[tuple(char_count)].append(s)
            
        
        return list(res.values())

