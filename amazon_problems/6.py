# longest nice subarray

# a subarray is nice if the AND operation between right pointer and current_and is equal to zero

# the right pointer and the left pointer are initialized to 0 and will traverse from the starting position of the array

# the current_and is initialized to 0 and will be updated with the AND operation between the current_and and the right pointer

# the left pointer will moves only if a violation is seen which the AND operation != 0

# the right pointer will move to the next element in the array

# the maximum length of the nice subarray will be stored in the max_len variable

def longestNiceSubarray(nums):
    left = 0
    current_and = 0
    max_len = 0
    
    for right in range(len(nums)):
        while(current_and & nums[right] != 0):
            current_and ^= nums[left]
            left += 1
            
        current__and |= nums[right]
        
        max_len = max(max_len, right - left + 1)
        
        return max_len