import polars as pl

def wsm(decision_matrix: pl.DataFrame, weights: list) -> pl.DataFrame:
    if len(weights) != len(decision_matrix.columns):
        raise ValueError("Jumlah bobot harus sama dengan jumlah kriteria dalam decision matrix.")
    norm_weights = [w / sum(weights) for w in weights] # Normalisasi bobot agar totalnya 1
    scores = decision_matrix.mul(norm_weights).sum(axis=1) # Hitung skor WSM (perkalian nilai kriteria dengan bobotnya)
    result = decision_matrix.with_columns(pl.Series("WSM Score", scores))  # Gabungkan hasil skor dengan alternatif
    return result