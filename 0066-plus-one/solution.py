class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = 0
        for i in range(len(digits)):
            print(digits[-(i+1)])
            n = n + (10**i)*(digits[-(i+1)])
            print(n)
        n = n + 1
        answer = []
        print(n)
        for i in str(n):
            answer.append(int(i))
        return answer