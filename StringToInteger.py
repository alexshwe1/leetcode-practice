import re
class Solution:
    def myAtoi(self, s: str) -> int:
        MAX_INT = 2 ** 31 - 1 # 2,147,483,647
        MIN_INT = -2 ** 31    #-2,147,483,648

        pattern = r"^\s*[+-]?\d+"
        match = re.findall(pattern, s)
        if not match:
            return 0
        res = int(match[0])
        if res > MAX_INT:
            return MAX_INT
        elif res < MIN_INT:
            return MIN_INT
        return res

solution = Solution()
input_str = "   -42 words"
output_int = solution.myAtoi(input_str)
print(output_int)  # Output: -42