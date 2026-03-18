class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        a = nums1[:m] + nums2
        a.sort()
        
        nums1.clear()
        for i in a:
            nums1.append(i)
