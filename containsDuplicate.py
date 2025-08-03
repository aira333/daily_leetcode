'''
brute force - compare each element with every other element in the array
            - time complexity - o(n^2)
            - space complecity - o(1)
better solution - sort all the values in the array and the duplicates would be adajacent to each other
                - time complexity - o(nlogn)
                - space complexity - o(1)
efficient solution - use a hashmap, and insert the elements in the array one by one and check if an element already exists,
                    if it does, return True, if it does not add it to the array to check again
                    - time complexity - o(n)
                    - space complexity - o(n)
'''

class Solution:
    def containsDuplicate(self, nums):
        hashset = set()
        
        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False