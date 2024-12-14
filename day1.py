# merge two sorted arrays

# nums1 and nums2 in non-decreasing order - ascending order

# two integers m and n represent the number of elements in nums1 and nums2

# merge nums2 into nums1 as one sorted array



class Solution:
    def merge(self, nums1, m, nums2, n) -> None:
        # last index in nums1
        last = m + n - 1 
        # last points to the final position in nums1 where the merged element will go
    
        
        # merge nums1 and nums2 in reverse order
        while m > 0 and n > 0:
            if nums1[m - 1] > nums2[n - 1]:
                nums1[last] = nums1[m - 1]
                m -= 1
            else:
                nums1[last] = nums2[n - 1]
                n -= 1
            last -= 1

        # fill nums1 with leftover nums2 elements
        while n > 0:
            nums1[last] = nums2[n - 1]
            n -= 1
            last -= 1

        

