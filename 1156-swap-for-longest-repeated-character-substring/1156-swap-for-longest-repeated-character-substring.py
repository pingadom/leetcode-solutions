from collections import Counter

class Solution:
    def maxRepOpt1(self,text):
        freq = Counter(text)
        result = 0

        for c in freq:
            left = 0
            different = 0

            for right in range(len(text)):
                if text[right] != c:
                    different += 1

                while different > 1:
                    if text[left] != c:
                        different -= 1
                    left += 1

                result = max(result, min(right - left + 1, freq[c]))

        return result
        