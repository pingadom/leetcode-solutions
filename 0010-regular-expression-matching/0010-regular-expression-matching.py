from functools import cache

class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        @cache
        def match(s, p):
            if not p:
                return not s

            first_match = bool(s) and (p[0] == s[0] or p[0] == ".")

            if len(p) >= 2 and p[1] == "*":
                return (
                    match(s, p[2:]) or
                    (first_match and match(s[1:], p))
                )

            return first_match and match(s[1:], p[1:])

        return match(s, p)