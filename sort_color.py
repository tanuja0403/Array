class Solution(object):
    def sortColors(self, nums):
        start = 0 
        middle = 0 
        end = len(nums)-1

        while middle <= end :
            if nums[middle]==0 :
                nums[start] , nums[middle] = nums[middle] ,nums[start]
                start += 1
                middle +=1
            elif nums[middle]== 1 :
                middle +=1 
            else :
                nums[end] , nums[middle] = nums[middle] , nums[end]
                end -=1