class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # print(strs, len(strs))
        le_group = {}
        # print(freq_counter)

        for str in strs:
            freq_counter = [0]*26
            for c in str:
                if freq_counter[ord(c)-ord('a')]: 
                    freq_counter[ord(c)-ord('a')] += 1 
                else:
                    freq_counter[ord(c)-ord('a')] = 1
            if tuple(freq_counter) in le_group:
                le_group[tuple(freq_counter)].append(str)
            else:
                le_group[tuple(freq_counter)] = [str]
        return(list(le_group.values()))