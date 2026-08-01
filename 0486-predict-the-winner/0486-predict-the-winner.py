class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:

        def solve(left, right):
            # Only one number left
            if left == right:
                return nums[left]

            # Choose left
            take_left = nums[left] - solve(left + 1, right)

            # Choose right
            take_right = nums[right] - solve(left, right - 1)

            # Return the best score difference
            return max(take_left, take_right)

        return solve(0, len(nums) - 1) >= 0