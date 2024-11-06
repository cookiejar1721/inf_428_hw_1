import numpy as np

def generate_random_data(mean, variance, num_samples):
    return np.random.randint(max(mean - variance, 0), min(mean + variance + 1, 90), num_samples)

def calculate_department_average(threat_scores):
    return np.mean(threat_scores)

def calculate_aggregated_threat(department_data, department_importance):
    total_importance = sum(department_importance.values())
    weighted_threat_sum = 0

    for department, scores in department_data.items():
        department_mean = np.mean(scores)
        weighted_threat_sum += department_mean * department_importance[department]

    aggregated_threat = weighted_threat_sum / total_importance

    return min(max(aggregated_threat, 0), 90)
