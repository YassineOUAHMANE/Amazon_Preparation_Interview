class solution:
    #Brute force solution
    def subarraysum(nums,k):
        count = 0
        somme = 0
        for i in range(len(nums)):
            somme = 0
            for j in range(i,len(nums)):
                somme+=nums[i]
                if somme == k:
                    count+=1
        return count
    
    #Optimal solution
    def subarraysumOp(nums,k):
        prefixSum  = 0
        count = 0
        prefixmap = {0:1}
        for num in nums:
            prefixSum += num
            if prefixSum - k in prefixmap:
                count+= prefixmap[prefixSum - k]
            prefixmap[prefixSum - k]+=1
        return count

