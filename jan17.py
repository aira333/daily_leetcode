class Solution:
    def doesValidArrayExist(self, derived) -> bool:
        return reduce(xor, derived)==0
        