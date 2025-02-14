class Solution(object):
    def longestPalindrome(self, s):
        def expand_around_center(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]  # Extract the valid palindrome
        
        longest_palindrome = ""
        
        for i in range(len(s)):
            odd_palindrome = expand_around_center(i, i)      # Odd-length palindrome
            even_palindrome = expand_around_center(i, i + 1) # Even-length palindrome
            longest_palindrome = max(longest_palindrome, odd_palindrome, even_palindrome, key=len)
        
        return longest_palindrome
