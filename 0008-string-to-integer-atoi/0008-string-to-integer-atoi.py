
class Solution:
    def myAtoi(self, s: str) -> int:
        i = 0
        neg = 1
        n = len(s)

        # Step 1: Skip leading spaces
        while i < n and s[i] == " ":
            i += 1

        # Step 2: Determine sign
        if i < n and s[i] in ["-", "+"]:
            if s[i] == "-":
                neg = -1
            i += 1

        # Step 3: Read digits until a non-digit
        integer = 0

        while i < n and "0" <= s[i] <= "9":
            integer = integer * 10 + int(s[i])
            i += 1

        # Step 4: Apply sign
        integer *= neg

        # Step 5: Clamp to 32-bit integer range
        if integer < -(2**31):
            return -(2**31)
        elif integer > (2**31) - 1:
            return (2**31) - 1

        return integer
