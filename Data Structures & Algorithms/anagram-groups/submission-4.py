class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # print(f"list of strs, {strs}, type of the input, {type(strs)}")

        # Anagrams = words same in length and with the same word count. 
        # Main question to answer: what data structures should I store the letters and their frequency of each word and then compare them? 
        # The final structure will of course be a list of list as mentioned in the problem, i.e. List[List[str]]

        # Naive Solution
        # Sort each string and group them using a hash map
        
        res = {}
        for s in strs:
            sorted_s = ''.join(sorted(s))
            if sorted_s in res:
                res[sorted_s].append(s)
            else:
                res[sorted_s] = [s]

        print(res)
        return list(res.values())
