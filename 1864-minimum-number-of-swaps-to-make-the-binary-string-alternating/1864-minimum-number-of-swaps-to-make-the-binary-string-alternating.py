class Solution:
    def minSwaps(self, s: str) -> int:
        zeros = s.count("0")
        ones = s.count("1")

        if abs(zeros - ones) > 1:
            return -1

        def count(start):
            mismatches = 0

            for i in range(len(s)):
                expected = start if i % 2 == 0 else 1 - start

                if int(s[i]) != expected:
                    mismatches += 1

            return mismatches // 2

        if zeros > ones:
            return count(0)

        if ones > zeros:
            return count(1)

        return min(count(0), count(1))