class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        prefixes = []
        for item in strs:
            s = []
            for i in range(1,len(item)+1):
                s.append(item[:i])
            prefixes.append(s)
        
        common = set(prefixes[0])

        for arr in prefixes[1:]:
            common &= set(arr)

        return max(common, key=len, default="")


        