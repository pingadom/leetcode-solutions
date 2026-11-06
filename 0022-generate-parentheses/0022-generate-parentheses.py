
class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        result = []
        self.recurse(n, "", 0, 0, result)
        return result

    def recurse(self, n, curr, opened, closed, result):

        # All n pairs have been placed
        if opened == n and closed == n:
            result.append(curr)
            return

        # Add an opening bracket
        if opened < n:
            self.recurse(
                n, curr + "(", opened + 1, closed, result
            )

        # Add a closing bracket
        if closed < opened:
            self.recurse(
                n, curr + ")", opened, closed + 1, result
            )
