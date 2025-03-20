import polars as pl
import numpy as np

def wpm(decision_matrix: pl.DataFrame, weights: list, criteria_types: list) -> pl.DataFrame:
    """
    Menghitung skor WPM berdasarkan matriks keputusan dan bobot.
    
    :param decision_matrix: DataFrame Polars dengan nilai kriteria untuk setiap alternatif.
    :param weights: List bobot kriteria (jumlah harus sama dengan jumlah kolom decision_matrix).
    :param criteria_types: List berisi "max" atau "min" untuk setiap kriteria (menentukan apakah nilai perlu dinormalisasi).
    :return: DataFrame dengan skor akhir untuk setiap alternatif.
    """
    if len(weights) != len(decision_matrix.columns) or len(criteria_types) != len(decision_matrix.columns):
        raise ValueError("Jumlah bobot dan jenis kriteria harus sesuai dengan jumlah kolom decision matrix.")

    # Normalisasi bobot agar totalnya 1
    norm_weights = [w / sum(weights) for w in weights]

    # Normalisasi nilai untuk kriteria minimisasi
    for i, crit_type in enumerate(criteria_types):
        if crit_type == "min":
            decision_matrix = decision_matrix.with_columns(1 / decision_matrix[:, i].alias(decision_matrix.columns[i]))

    # Hitung skor WPM
    scores = decision_matrix.apply(lambda row: np.prod(row ** norm_weights), axis=1)

    # Gabungkan hasil skor dengan alternatif
    result = decision_matrix.with_columns(pl.Series("WPM Score", scores))

    return result