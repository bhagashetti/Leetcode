class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []
        n = len(operations)
        for i in range(n):
            if operations[i].lstrip('-').isdigit():
                record.append(int(operations[i]))
            elif operations[i] == 'C':
                record.pop()
            elif operations[i] == 'D':
                ele = record[-1]
                ele = 2*ele
                record.append(ele)
            elif operations[i] == '+':
                l = len(record)
                ele1 = record[l-1]
                ele2 = record[l-2]
                record.append(ele1+ele2)
        sum = 0
        for num in record:
            sum+=num
        return sum




        