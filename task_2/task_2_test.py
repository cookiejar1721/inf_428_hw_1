import unittest
import numpy as np

from task_2 import generate_random_data, calculate_department_average, calculate_aggregated_threat

class TestAggregatedThreatScore(unittest.TestCase):

    def test_case_1_similar_scores_equal_importance(self):
        departments = [
            {'name': 'Engineering', 'scores': generate_random_data(30, 5, 50), 'importance': 3},
            {'name': 'Marketing', 'scores': generate_random_data(32, 5, 50), 'importance': 3},
            {'name': 'Finance', 'scores': generate_random_data(31, 5, 50), 'importance': 3},
            {'name': 'HR', 'scores': generate_random_data(30, 5, 50), 'importance': 3},
            {'name': 'Science', 'scores': generate_random_data(32, 5, 50), 'importance': 3},
        ]
        aggregated_score = calculate_aggregated_threat(departments)
        print(f"Aggregated Score for Case 1: {aggregated_score}")
        self.assertAlmostEqual(aggregated_score, 30, delta=5)

    def test_case_2_high_threat_high_importance(self):
        departments = [
            {'name': 'Engineering', 'scores': generate_random_data(20, 5, 50), 'importance': 2},
            {'name': 'Marketing', 'scores': generate_random_data(70, 5, 50), 'importance': 5},
            {'name': 'Finance', 'scores': generate_random_data(25, 5, 50), 'importance': 2},
            {'name': 'HR', 'scores': generate_random_data(30, 5, 50), 'importance': 2},
            {'name': 'Science', 'scores': generate_random_data(28, 5, 50), 'importance': 2},
        ]
        aggregated_score = calculate_aggregated_threat(departments)
        print(f"Aggregated Score for Case 2: {aggregated_score}")
        self.assertGreater(aggregated_score, 50)

    def test_case_3_small_high_threat_department(self):
        departments = [
            {'name': 'Engineering', 'scores': generate_random_data(20, 5, 100), 'importance': 3},
            {'name': 'Marketing', 'scores': generate_random_data(85, 5, 5), 'importance': 3},
            {'name': 'Finance', 'scores': generate_random_data(25, 5, 50), 'importance': 3},
            {'name': 'HR', 'scores': generate_random_data(30, 5, 50), 'importance': 3},
            {'name': 'Science', 'scores': generate_random_data(28, 5, 50), 'importance': 3},
        ]
        aggregated_score = calculate_aggregated_threat(departments)
        print(f"Aggregated Score for Case 3: {aggregated_score}")
        self.assertLess(aggregated_score, 40)

    def test_case_4_varied_threats_importance_users(self):
        departments = [
            {'name': 'Engineering', 'scores': generate_random_data(15, 10, 200), 'importance': 2},
            {'name': 'Marketing', 'scores': generate_random_data(60, 20, 100), 'importance': 4},
            {'name': 'Finance', 'scores': generate_random_data(40, 15, 75), 'importance': 3},
            {'name': 'HR', 'scores': generate_random_data(25, 5, 120), 'importance': 5},
            {'name': 'Science', 'scores': generate_random_data(30, 5, 60), 'importance': 1},
        ]
        aggregated_score = calculate_aggregated_threat(departments)
        print(f"Aggregated Score for Case 4: {aggregated_score}")
        self.assertGreater(aggregated_score, 30)
        self.assertLess(aggregated_score, 50)

    def test_case_5_zero_threat_scores(self):
        departments = [
            {'name': 'Engineering', 'scores': generate_random_data(0, 0, 50), 'importance': 3},
            {'name': 'Marketing', 'scores': generate_random_data(0, 0, 100), 'importance': 3},
            {'name': 'Finance', 'scores': generate_random_data(0, 0, 150), 'importance': 3},
            {'name': 'HR', 'scores': generate_random_data(0, 0, 200), 'importance': 3},
            {'name': 'Science', 'scores': generate_random_data(0, 0, 75), 'importance': 3},
        ]
        aggregated_score = calculate_aggregated_threat(departments)
        print(f"Aggregated Score for Case 5: {aggregated_score}")
        self.assertEqual(aggregated_score, 0)

    def test_case_6_high_threat_low_importance(self):
        departments = [
            {'name': 'Engineering', 'scores': generate_random_data(10, 5, 100), 'importance': 3},
            {'name': 'Marketing', 'scores': generate_random_data(85, 5, 50), 'importance': 1},
            {'name': 'Finance', 'scores': generate_random_data(20, 5, 50), 'importance': 3},
            {'name': 'HR', 'scores': generate_random_data(30, 5, 50), 'importance': 3},
            {'name': 'Science', 'scores': generate_random_data(28, 5, 50), 'importance': 3},
        ]
        aggregated_score = calculate_aggregated_threat(departments)
        print(f"Aggregated Score for Case 6: {aggregated_score}")
        self.assertLess(aggregated_score, 40)

    def test_case_7_large_user_variance_similar_threats(self):
        departments = [
            {'name': 'Engineering', 'scores': generate_random_data(30, 5, 200), 'importance': 3},
            {'name': 'Marketing', 'scores': generate_random_data(32, 5, 10), 'importance': 3},
            {'name': 'Finance', 'scores': generate_random_data(31, 5, 150), 'importance': 3},
            {'name': 'HR', 'scores': generate_random_data(30, 5, 100), 'importance': 3},
            {'name': 'Science', 'scores': generate_random_data(32, 5, 5), 'importance': 3},
        ]
        aggregated_score = calculate_aggregated_threat(departments)
        print(f"Aggregated Score for Case 7: {aggregated_score}")
        self.assertAlmostEqual(aggregated_score, 30, delta=5)

    def test_case_8_high_threat_high_importance_all_departments(self):
        departments = [
            {'name': 'Engineering', 'scores': generate_random_data(80, 5, 50), 'importance': 5},
            {'name': 'Marketing', 'scores': generate_random_data(85, 5, 50), 'importance': 5},
            {'name': 'Finance', 'scores': generate_random_data(90, 5, 50), 'importance': 5},
            {'name': 'HR', 'scores': generate_random_data(88, 5, 50), 'importance': 5},
            {'name': 'Science', 'scores': generate_random_data(89, 5, 50), 'importance': 5},
        ]
        aggregated_score = calculate_aggregated_threat(departments)
        print(f"Aggregated Score for Case 8: {aggregated_score}")
        self.assertGreater(aggregated_score, 80)


if __name__ == '__main__':
    unittest.main()
