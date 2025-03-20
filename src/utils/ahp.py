import polars as pl
import numpy as np

def calculate_weights(pairwise_matrix: pl.DataFrame) -> pl.Series:
    """
    Menghitung bobot berdasarkan eigenvector terbesar dari matriks perbandingan berpasangan.
    """
    matrix_np = pairwise_matrix.to_numpy()
    eigenvalues, eigenvectors = np.linalg.eig(matrix_np)
    max_index = np.argmax(eigenvalues)
    weights = eigenvectors[:, max_index].real
    weights = weights / np.sum(weights)
    
    return pl.Series("Weights", weights)

def consistency_ratio(pairwise_matrix: pl.DataFrame, weights: pl.Series) -> tuple:
    """
    Menghitung indeks konsistensi (CI) dan rasio konsistensi (CR).
    """
    n = pairwise_matrix.shape[0]
    matrix_np = pairwise_matrix.to_numpy()
    weights_np = weights.to_numpy()
    
    lambda_max = np.sum(np.dot(matrix_np, weights_np) / weights_np) / n
    ci = (lambda_max - n) / (n - 1)

    ri_dict = {1: 0, 2: 0, 3: 0.58, 4: 0.9, 5: 1.12, 6: 1.24, 7: 1.32, 8: 1.41, 9: 1.45}
    ri = ri_dict.get(n, 1.45)
    
    cr = ci / ri if ri else 0
    return ci, cr

def ahp(criteria: list, pairwise_comparisons: list) -> tuple:
    """
    Menghitung bobot AHP berdasarkan matriks perbandingan berpasangan.
    """
    n = len(criteria)
    pairwise_matrix = pl.DataFrame(pairwise_comparisons)

    # Hitung bobot kriteria
    weights = calculate_weights(pairwise_matrix)

    # Hitung konsistensi
    ci, cr = consistency_ratio(pairwise_matrix, weights)

    return weights, ci, cr
