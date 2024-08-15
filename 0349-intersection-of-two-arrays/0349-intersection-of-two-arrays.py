class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # set1 = set(nums1)
        # set2 = set(nums2)
        # return set1.intersection(set2)
        my_set = set(nums1)
        l = []
        for elm in nums2:
            if elm in my_set:
                l.append(elm)
                my_set.remove(elm)
        return l
