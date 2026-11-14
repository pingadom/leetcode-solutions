class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # Determine whether the result is negative
        negative = (dividend < 0) ^ (divisor < 0)

        dividend = abs(dividend)
        divisor = abs(divisor)

        quotient = 0

        # Try powers of two from largest to smallest
        for shift in range(31, -1, -1):
            if (divisor << shift) <= dividend:
                dividend -= divisor << shift
                quotient += 1 << shift

        if negative:
            quotient = -quotient

        # Clamp to signed 32-bit integer range
        INT_MAX = (1 << 31) - 1
        INT_MIN = -(1 << 31)

        return max(INT_MIN, min(quotient, INT_MAX))