class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        cur = 0
        while left < right:
            cur = max(min(height[left], height[right]) * (right - left), cur)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return cur

# Example usage
solution = Solution()
heights = [1, 8, 6, 2, 5, 4, 8, 3, 7]
max_water = solution.maxArea(heights)
print("Maximum water that can be held:", max_water)