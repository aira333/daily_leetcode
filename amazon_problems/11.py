#two sum

# brute force

def twoSum (nums, target):
    for i in range (len(nums)):
        for j in range (i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
            
# Time complexity: O(n^2)

# Space complexity: O(1)

# optimized solution using hash map

def twoSum(nums, target):
    num_map = {}
    
    for i, num in enumerate(nums):
        diff = target - num
        
        if diff in num_map:
            return [num_map[diff], i]
        
        num_map[num] = i
        
# Time complexity: O(n)
# Space complexity: O(n) for the hash map