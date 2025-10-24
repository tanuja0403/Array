def majorityElement(self , nums) :
    candidate = None 
    count = 0

    for num in nums :
        if count == 0 :
            candidate = num 
        if num == candidate :
            count +=1 
        else :
            count -=1 

    if nums.count (candidate) > len(nums)//2:
        return candidate
    else :
        return None 