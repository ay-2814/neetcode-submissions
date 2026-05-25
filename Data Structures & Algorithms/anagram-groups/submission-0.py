class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) # mapping of characterCount to list of strings. Strings with same character count are anagrams

        for s in strs:
            count_c = [0] * 26 # for storing a....z

            for c in s: 
                count_c[ord(c) - ord('a')] +=1
            res[tuple(count_c)].append(s)
        
        return res.values()
            

        