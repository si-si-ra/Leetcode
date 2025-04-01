class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n=len(nums)
        element1,element2 = -1,-1
        count1,count2=0,0
         
        for element in nums:
             if element1==element:
                 count1+=1
             elif element2==element:
                 count2+=1
             elif count1==0:
                 element1=element
                 count1+=1
             elif count2==0:
                 element2=element
                 count2+=1
             else:
                 count1-=1
                 count2-=1
             
        result=[]
        count1,count2=0,0
         
        for element in nums:
             if element1==element:
                 count1+=1
             elif element2==element:
                 count2+=1
         
        if count1>n/3:
             result.append(element1)
        if count2>n/3 and element1!=element2:
             result.append(element2)
             
        if len(result)==2 and result[0]>result[1]:
             result[0],result[1]=result[1],result[0]
        return result