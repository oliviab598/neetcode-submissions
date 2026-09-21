class Solution:
    def calPoints(self, operations: List[str]) -> int:
        ans = []

        for i in range(len(operations)):
            if operations[i] != '+' and operations[i] != 'D' and operations[i] != 'C':
                ans.append(int(operations[i]))
            elif operations[i] == '+':
                ans.append(int(ans[-2]) + int(ans[-1]))
            elif operations[i] == 'C':
                ans.pop()
            elif operations[i] == 'D':
                ans.append(2 * ans[-1])
        return sum(ans)