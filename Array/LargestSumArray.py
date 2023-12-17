class Solution:
    # Function to find the sum of the contiguous subarray with the maximum sum.
    def maxSubArraySum(self, arr, N):
        max_sum = float('-inf')
        current_sum = 0

        for i in range(N):
            current_sum = max(arr[i], current_sum + arr[i])
            max_sum = max(max_sum, current_sum)

        return max_sum


# Example usage:
my_arr = [-1, 2, 4, 6, -4]
sol = Solution()
largest_sum = sol.maxSubArraySum(my_arr, 5)
print(largest_sum)
