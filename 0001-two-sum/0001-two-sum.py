class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prev_map = {}
        for i, n in enumerate(nums):
            diff = target - nums[i]
            if diff in prev_map:
                return [prev_map[diff], i]
            prev_map[n] = i