class Solution:
    def intersection_of_arrays(self, nums1, nums2):
        # Convert both lists to sets to remove duplicates
        set1 = set(nums1)
        set2 = set(nums2)

        result = []

        # Check for presence in set1, add to result
        for num in set2:
            if num in set1:
                result.append(num)

        return result

class TestSolution:
    def test_intersection(self):
        solution = Solution()

        assert solution.intersection_of_arrays([1, 2, 2, 1], [2, 2]) == [2]
        assert solution.intersection_of_arrays([], [1, 2, 3]) == []
        assert solution.intersection_of_arrays([1, 2, 3], []) == []
        assert solution.intersection_of_arrays([], []) == []

        print("All test cases passed.")

if __name__ == "__main__":
    test_solution = TestSolution()
    test_solution.test_intersection()
