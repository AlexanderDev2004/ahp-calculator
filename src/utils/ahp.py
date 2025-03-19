import numpy as np

def calculate_weights(pairwise_matrix):
    eigenvalues, eigenvectors = np.linalg.eig(pairwise_matrix)
    max_index = np.argmax(eigenvalues)
    weights = eigenvectors[:, max_index].real
    weights = weights / np.sum(weights)
    return weights

def consistency_ratio(pairwise_matrix, weights):
    n = pairwise_matrix.shape[0]
    lambda_max = np.sum(np.dot(pairwise_matrix, weights) / weights) / n
    ci = (lambda_max - n) / (n - 1)
    
    ri_dict = {1: 0, 2: 0, 3: 0.58, 4: 0.9, 5: 1.12, 6: 1.24, 7: 1.32, 8: 1.41, 9: 1.45}
    ri = ri_dict.get(n, 1.45)
    
    cr = ci / ri if ri else 0
    return ci, cr

def ahp(criteria, pairwise_comparisons):
    n = len(criteria)
    pairwise_matrix = np.array(pairwise_comparisons).reshape(n, n)
    
    # Hitung bobot kriteria
    weights = calculate_weights(pairwise_matrix)
    
    # Hitung konsistensi
    ci, cr = consistency_ratio(pairwise_matrix, weights)
    
    return weights, ci, cr