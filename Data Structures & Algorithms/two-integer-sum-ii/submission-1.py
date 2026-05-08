class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1


        for i in range(0, len(numbers) - 1):
            l = i
            r = len(numbers) - 1
            while r > l:
                if (numbers[l] + numbers[r] == target):
                    return [l + 1, r + 1]
                r -= 1
        