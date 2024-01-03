import numpy as np

C = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
dimensi_ruang_nol = np.linalg.matrix_rank(C)
print(f"Dimensi ruang nol matriks C: {dimensi_ruang_nol}.")
