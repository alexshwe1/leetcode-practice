class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # base case
        if len(s) == 1 or len(s) <= numRows:
            return s

        rows = [[] for row in range(numRows)]
        index = 0
        step = 1
        for char in s:
            rows[index].append(char)
            if index == 0:
                step = 1
            elif index == numRows - 1:
                step = -1
            index += step
        for i in range(numRows):
            rows[i] = "".join(rows[i])
        return "".join(rows)

# Example usage
solution = Solution()
input_str = "PAYPALISHIRING"
num_rows = 3
output_str = solution.convert(input_str, num_rows)
print(output_str)  # Output: "PAHNAPLSIIGYIR"