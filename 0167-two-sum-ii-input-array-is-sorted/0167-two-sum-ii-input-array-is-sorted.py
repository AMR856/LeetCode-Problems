class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        pointer_one = 0
        pointer_two = len(numbers) - 1
        while (pointer_one < pointer_two):
            sum = numbers[pointer_one] + numbers[pointer_two]
            if sum < target:
                pointer_one += 1
            elif sum > target:
                pointer_two -= 1
            else:
                return [pointer_one + 1, pointer_two + 1]