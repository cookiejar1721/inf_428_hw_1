import numpy as np

def generate_random_data(mean, variance, num_samples):
    return np.random.randint(max(mean - variance, 0), min(mean + variance + 1, 90), num_samples)

def calculate_department_average(threat_scores):
    return np.mean(threat_scores)

def calculate_aggregated_threat(departments):
    total_weighted_threat = 0
    total_importance = 0

    for department in departments:
        average_threat = calculate_department_average(department['scores'])
        weighted_threat = average_threat * department['importance']
        total_weighted_threat += weighted_threat
        total_importance += department['importance']

    return total_weighted_threat / total_importance

