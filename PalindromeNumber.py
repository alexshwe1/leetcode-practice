class Solution:
    def isPalindrome(self, x: int) -> bool:

        # edge cases
        if x < 0: # negative numbers not a palindrome
            return False
        elif math.trunc(x / 10) == 0: # single digit numbers always a palindrome
            return True
        
        strx = str(x)
        left = 0
        right = len(strx) - 1

        while left < right:
            if strx[left] != strx[right]:
                return False
            left += 1
            right -= 1
        return True

# Example usage
solution = Solution()
num1 = 121
num2 = 12321
num3 = 12345

print(solution.isPalindrome(num1))  # Output: True
print(solution.isPalindrome(num2))  # Output: True
print(solution.isPalindrome(num3))  # Output: False