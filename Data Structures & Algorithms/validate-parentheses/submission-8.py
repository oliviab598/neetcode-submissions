class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dictionary = {
            ")": "(",
            "}": "{",
            "]": "["
        }

        for c in s:
            if c == ")" or c == "]" or c == "}":
                if len(stack) == 0:
                    return False
                open_b = dictionary[c]
                curr = stack.pop()
                if open_b != curr:
                    return False
            else:
                stack.append(c)
        return len(stack) == 0
            