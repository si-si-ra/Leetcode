class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        k%=n
         # Reverse first part
        self.reverse(nums, 0, n - k - 1)
        # Reverse second part
        self.reverse(nums, n - k, n - 1)
        # Reverse the entire array
        self.reverse(nums, 0, n - 1)
    def reverse(self,nums,start,end):
        while start<end:
            nums[start],nums[end]=nums[end],nums[start]
            start+=1
            end-=1
        