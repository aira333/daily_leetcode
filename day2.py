# remove element
# integer array nums
# integer val
# remove all instances of val in nums
# the order of elements may be changed
# return the number of elements in nums which are not equal to val
# change the array nums such that forst k elements of nums contains the elements which are not equal to val
# return k

class Solution:
    def remove(self, nums, val):
        k=0 #initialize the pointer

        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k+=1
        return k

            