class Solution(object):
    def merge_sorted_arrays(self, nums1, m, nums2, n):
        i = m - 1  # Pointer for nums1
        j = n - 1  # Pointer for nums2
        k = m + n - 1  # Position to fill in nums1

        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1

        # To copy, if there are remaining elements
        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1


class TestSolution:
    def test_merge_sorted_arrays(self):
        solution = Solution()

        nums1 = [1]
        nums2 = []
        solution.merge_sorted_arrays(nums1, 1, nums2, 0)
        assert nums1 == [1]

        nums1 = [0]
        nums2 = [1]
        solution.merge_sorted_arrays(nums1, 0, nums2, 1)
        assert nums1 == [1]

        nums1 = [4, 5, 6, 0, 0, 0]
        nums2 = [1, 2, 3]
        solution.merge_sorted_arrays(nums1, 3, nums2, 3)
        assert nums1 == [1, 2, 3, 4, 5, 6]

        nums1 = [0, 0, 0, 0]
        nums2 = [1, 2, 3]
        solution.merge_sorted_arrays(nums1, 0, nums2, 3)
        assert nums1 == [1, 2, 3, 0]

        nums1 = [3, 4, 5, 0, 0, 0]
        nums2 = [1, 2]
        solution.merge_sorted_arrays(nums1, 3, nums2, 2)
        assert nums1 == [1, 2, 3, 4, 5, 0]

        print("All test cases passed.")

if __name__ == "__main__":
    test_solution = TestSolution()
    test_solution.test_merge_sorted_arrays()
