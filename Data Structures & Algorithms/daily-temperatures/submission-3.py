class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        temp = deque()
        for i in range(len(temperatures)):
            while temp and temperatures[i] > temperatures[temp[-1]]:
                prev = temp.pop()
                result[prev] = i - prev
            temp.append(i)
        return result




    def bruteForce(self, temperatures):
        result = [0] * len(temperatures)
        for i in range(len(temperatures)):
            count = 0
            for j in range(i + 1, len(temperatures)):
                if temperatures[j] > temperatures[i]:
                    result[i] = j - i
                    break
        return result