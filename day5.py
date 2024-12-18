# remove duplicates from sorted array

# given in ascending order

# no-duplicates in the putput

# no extra memory to be used, should do it in place

# return the number of unique values

# we take two pointer r and l, 
# both initialized at index 1 and r pointer used to check the unique values, 
# if the number at which r pointer points is not equal to the number before it then the number get swaped at the index l pointer points to

class Solution(object):
    def removeDuplicates(self, nums):
        l = 1

        for r in range (1, len(nums)):
            if nums[r] != nums[r-1]:
                nums[l] = nums[r]
                l += 1
        return l

        
