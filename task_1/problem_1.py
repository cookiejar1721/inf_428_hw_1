class Solution(object):
    def find_length_of_longest_continuous_increasing_subsequence(self, nums):
        if not nums:
            return 0

        max_length = 1  # Maximum length found
        current_length = 1  # Current subsequence length

        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                current_length += 1
                max_length = max(max_length, current_length)
            else:
                current_length = 1

        return max_length

class TestSolution:
    def test_find_length_of_longest_continuous_increasing_subsequence(self):
        solution = Solution()

        assert solution.find_length_of_longest_continuous_increasing_subsequence([]) == 0
        assert solution.find_length_of_longest_continuous_increasing_subsequence([1]) == 1
        assert solution.find_length_of_longest_continuous_increasing_subsequence([1, 2, 3, 4]) == 4
        assert solution.find_length_of_longest_continuous_increasing_subsequence([1, 3, 5, 4, 7]) == 3
        assert solution.find_length_of_longest_continuous_increasing_subsequence([2, 2, 2, 2]) == 1

        print("All test cases passed.")

if __name__ == "__main__":
    test_solution = TestSolution()
    test_solution.test_find_length_of_longest_continuous_increasing_subsequence()
