import math
class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        first_pointer = 0
        result = []
        second_pointer = len(nums) - 1
        nums.sort()
        for i in range(math.floor(len(nums) / 2)):
            print(nums[second_pointer], nums[first_pointer])
            result.append((nums[second_pointer] + nums[first_pointer]) / 2)
            first_pointer += 1
            second_pointer -= 1
        return min(result)