
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""

        # Insert separators to handle odd and even lengths
        t = "#" + "#".join(s) + "#"
        n = len(t)

        # Palindrome radius at each index
        p = [0] * n

        # Centre and right boundary of the
        # rightmost-reaching palindrome found so far
        C = 0
        R = 0

        for i in range(n):
            mirror = 2 * C - i

            # Reuse previously calculated information
            if i < R:
                p[i] = min(R - i, p[mirror])

            # Expand beyond the known palindrome
            while (
                i - p[i] - 1 >= 0
                and i + p[i] + 1 < n
                and t[i - p[i] - 1] == t[i + p[i] + 1]
            ):
                p[i] += 1

            # Update centre and rightmost boundary
            if i + p[i] > R:
                C = i
                R = i + p[i]

        # Find the largest palindrome radius
        max_len = max(p)
        centre = p.index(max_len)

        # Convert transformed index to original index
        start = (centre - max_len) // 2

        return s[start:start + max_len]
