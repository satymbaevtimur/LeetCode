class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        resultArray = sorted(nums1 + nums2)
        length = len(resultArray)
        
        median = length // 2
        
        if length % 2 == 0:
            return (resultArray[median - 1] + resultArray[median]) / 2
        
        return resultArray[median]      
