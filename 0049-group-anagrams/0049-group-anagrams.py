class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        ordered = list(map(sorted, strs))
        final = {}
        c = set()
        for i,v in enumerate(ordered):
            if str(v) not in final:
                final[str(v)] = []
            final[str(v)].append(strs[i])
        
        return list(final.values())
        