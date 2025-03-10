class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        answerlist = []
        check = 0
        for i in range(len(nums1)+len(nums2)):
            if len(nums1) == 0:
                for z in range(len(nums2)):
                    answerlist.append(nums2.pop(0))
                break
            if len(nums2) == 0:
                for z in range(len(nums1)):
                    answerlist.append(nums1.pop(0))
                break
            elif nums1[0] <= nums2[0]:
                answerlist.append(nums1.pop(0))
                print(nums1)
            else:
                answerlist.append(nums2.pop(0))
                print(nums2)
        print(answerlist)
        index = len(answerlist) / 2
        if index.is_integer():
            return (answerlist[int(index-1)] + answerlist[int(index)])/2
        else:
            return answerlist[int(index)]
               
