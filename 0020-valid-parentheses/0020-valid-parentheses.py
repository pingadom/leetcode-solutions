class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        temp = {")": "(", "}": "{", "]": "["}

        for letter in s:
            if letter in ["(", "{", "["]:
                stack.append(letter)

            else:
                if not stack or stack[-1] != temp[letter]:
                    return False

                stack.pop()

        return len(stack) == 0
        