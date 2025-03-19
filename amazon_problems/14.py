# longest palindromic substring

class Solution(object):
    def longestPalindrome(self, s):
        def expandAroundCenter(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]

        longest = ""
        for i in range(len(s)):
            longest = max(longest, expandAroundCenter(i, i), expandAroundCenter(i, i + 1), key=len)
        return longest
