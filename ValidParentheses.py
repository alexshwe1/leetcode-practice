class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {
            "{": "}",
            "[": "]",
            "(": ")"
        }
        stack = []
        for bracket in s:
            if bracket in pairs:
                stack.append(bracket)
            elif len(stack) == 0 or bracket != pairs[stack.pop()]:
                return False

        return len(stack) == 0

# Example usage
solution = Solution()
input_str = "{[()]}"

if solution.isValid(input_str):
    print("The given string is valid.")
else:
    print("The given string is not valid.")