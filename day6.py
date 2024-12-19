# remove duplicates from sorted array II

# we are given an array, and we remove duplicates in-place (no extra memory), such that each unique element appears at most twice.

# we initialize the pointers i, j at index 1

# Every single time if i = i-1 then count = 1 ((which means continuous increment, so count += 1 )) 

# if count <= 2 then nums[i] = nums[j], and keep on incrementing j (j+= 1)

class Solution(object):
    def removeDuplicates (self, nums):
        j = 1
        count = 1
        n = len(nums)

        for i in range (1,n):
            if nums[i] == nums[i-1]:
                count += 1
            else:
                count = 1
            
            if count <= 2:
                nums[j] = nums[i]
                j += 1
        return j

