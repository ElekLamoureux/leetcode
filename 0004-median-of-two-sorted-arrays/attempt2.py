import math

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        x = 0
        y = 0
        total = len(nums1) + len(nums2)
        if total % 2: # odd
            center = total // 2
            
            while x + y < center:
                if nums1[x] < nums2[y] and x < lnum1-1:
                    x+=1
                elif x < lnum2-1:
                    y+=1
            if nums1[x] > nums2[y]:
                return nums1[x]
            else:
                return nums2[y]
        else:
            n = 0
            for i in range(int(av+0.5)):
                if nums1[x] < nums1[y] and x < lnum1-1:
                    x+=1
                    if i == av-0.5:
                        n = x
                elif x < lnum2-1:
                    y+=1
                    if i == av-0.5:
                        n = y
            print(x, y)
            if nums1[x] > nums2[y]:
                return (nums1[x] + n)/2
            else:
                return (nums2[y] + n)/2