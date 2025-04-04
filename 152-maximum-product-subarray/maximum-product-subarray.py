class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        maxProd=float('-inf')
        lefttoright=1
        righttoleft=1
        for i in range(n):
            if lefttoright==0:
                lefttoright=1
            if righttoleft==0:
                righttoleft=1
            lefttoright*=nums[i]
            j=n-i-1
            righttoleft*=nums[j]
            maxProd=max(lefttoright,righttoleft,maxProd)
        return maxProd
        