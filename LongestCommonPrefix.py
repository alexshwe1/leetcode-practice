class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        elif len(strs) == 1:
            return strs[0] 

        base = strs[0]
        for i in range(len(base)):
            for word in strs[1:]:
                if i == len(word) or word[i] != base[i]:
                    return base[0:i]
        return base

# Example usage
solution = Solution()
input_strings = ["flower", "flour", "flourish"]
common_prefix = solution.longestCommonPrefix(input_strings)
print("Longest common prefix:", common_prefix)  # Output: "flo"