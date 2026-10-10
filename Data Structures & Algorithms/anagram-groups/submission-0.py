class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        prev = {}

        for i in range(len(strs)):
            sorted_str = str(sorted(strs[i]))
            if sorted_str in prev:
                prev[sorted_str].append(strs[i])
            else:
                prev[sorted_str] = [strs[i]]
        
        return list(prev.values())
            