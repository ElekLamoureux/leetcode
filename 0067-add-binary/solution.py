class Solution:
    def addBinary(self, a: str, b: str) -> str:
        go = True
        a = list(a)
        b = list(b)
        carry = 0
        answer = []
        if len(a) != len(b):
            maxim = max(len(a), len(b))
            if maxim == len(a):
                for i in range(maxim-len(b)):
                    b.insert(0, "0")
            elif maxim == len(b):
                for i in range(maxim-len(a)):
                    a.insert(0, "0")
        else:
            maxim = len(a)

        for i in range(maxim):
            val = int(a[-(i+1)]) + int(b[-(i+1)]) + carry
            if val == 0:
                answer.insert(0, "0")
            elif val == 1:
                answer.insert(0, "1")
                carry = 0
            elif val == 2:
                answer.insert(0, "0")
                carry = 1
            elif val == 3:
                answer.insert(0, "1")
                carry = 1

        if carry == 1:
            answer.insert(0, "1")

        return "".join(answer)


        
