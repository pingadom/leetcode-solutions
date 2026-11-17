from collections import Counter

class Solution:
    def topKFrequent(self, words: list[str], k: int) -> list[str]:
        freq = Counter(words)
        total = sorted([(i,w) for w,i in freq.most_common(len(words))],key = lambda x: x[1])
        total = sorted(total, key = lambda x: -x[0])

        return ([c for _,c in total])[:k]
        