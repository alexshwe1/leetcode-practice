class Solution:
    @staticmethod
    def isPalindrome(s: str) -> bool:
        return (s == s[::-1])

    def longestPalindrome(self, s: str) -> str:
        ans = ""
        for i in range(len(s)):
            for j in range(i, len(s)):
                if self.isPalindrome(s[i:j+1]) and len(s[i:j+1]) > len(ans):
                    ans = s[i:j+1]
        return ans

# Example usage
solution = Solution()
input_str = "babad"
print(solution.longestPalindrome(input_str))  # Output: "bab"