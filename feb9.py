class Solution:
    def countBadPairs(self, nums):
        n = len(nums)
        total = n * (n - 1) // 2
        success = 0
        store = {}

        for i, num in enumerate(nums):
            diff = i - num
            store[diff] = store.get(diff, 0) + 1

        for count in store.values():
            success += count * (count - 1) // 2

        return total - success