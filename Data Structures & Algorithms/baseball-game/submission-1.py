class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []
        score = 0

        for op in operations:
            if op == "C":
                score -= record.pop()
                continue
            elif op == "D":
                record.append(record[-1] * 2)
            elif op == "+":
                record.append(record[-1] + record[-2])
            else:
                record.append(int(op))
            score += record[-1]
        
        return score