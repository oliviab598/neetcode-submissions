class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dictionary = {
            ")": "(",
            "}": "{",
            "]": "["
        }

        for c in s:
            if c == ')' or c == '}' or c == ']':
                if len(stack) == 0:
                    return False
                open_bracket = dictionary[c]
                curr = stack.pop()
                print('got here')
                if curr != open_bracket:
                    return False
            else:
                stack.append(c)
        return len(stack) == 0
            