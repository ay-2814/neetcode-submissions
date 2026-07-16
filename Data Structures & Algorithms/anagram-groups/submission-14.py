class Solution:
    from collections import defaultdict
    
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # print(f"input: {strs}, input type: {type(strs)} ")
        le_group = defaultdict(list)

        for s in strs:
            char_map = [0] * 26
            for c in s:
                char_map[ord(c) - ord('a')] += 1 
            # print(f"char_map: for {s} is {char_map}")
            
            le_group[tuple(char_map)].append(s)
        
        print(f"le_group : {le_group}")
        return list(le_group.values())
                


