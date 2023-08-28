class Solution:
    def romanToInt(self, s: str) -> int:
        nums = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        
        ans = 0

        for i in range(len(s)):
            if i < len(s) - 1 and nums[s[i]] < nums[s[i+1]]:
                ans -= nums[s[i]]
            else:
                ans += nums[s[i]]
        return ans
            
# Example usage
solution = Solution()
roman_numeral = "MMCMXCIV"  # 1994
integer_value = solution.romanToInt(roman_numeral)
print("Integer value:", integer_value)