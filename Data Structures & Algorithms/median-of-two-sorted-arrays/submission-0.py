class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums_sorted = []

        l, r = 0, 0
        while l < len(nums1) and r < len(nums2):
            if nums1[l] <= nums2[r]:
                nums_sorted.append(nums1[l])
                l += 1
            else:
                nums_sorted.append(nums2[r])
                r += 1

        while l < len(nums1):
            nums_sorted.append(nums1[l])
            l += 1

        while r < len(nums2):
            nums_sorted.append(nums2[r])
            r += 1

        l, r = 0, len(nums_sorted) - 1
        m = (l + r) // 2
        
        if len(nums_sorted) % 2 == 0:
            return float(nums_sorted[m] + nums_sorted[m + 1]) / 2
        else:
            return float(nums_sorted[m])