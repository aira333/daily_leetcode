# search suggestion system

'''
sort products lexicographically
initialize left = 0, right = n-1, result = [], prefix = ""
for each character in searchWord: 
a. append character to prefix
b. move left to first product starting with prefix
c. move right to last product starting with prefix
d. append at most 3 matching products from left to right to result
return result
'''

from typing import List

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        result = []
        left, right = 0, len(products) - 1
        prefix = ""

        for char in searchWord:
            prefix += char
            suggestions = []
            count = 0

            # Move the left pointer to the first product that starts with the current prefix
            while left <= right and not products[left].startswith(prefix):
                left += 1

            # Move the right pointer to the last product that starts with the current prefix
            while left <= right and not products[right].startswith(prefix):
                right -= 1

            # Collect at most 3 suggestions within the current [left, right] range
            for i in range(left, min(right + 1, left + 3)):
                suggestions.append(products[i])

            result.append(suggestions)

        return result



