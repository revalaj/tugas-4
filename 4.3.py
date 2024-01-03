import numpy as np

C = np.array([[1, 1e-10], [1e-10, 1]])
kondisi_buruk = np.linalg.cond(C)
print(f"Kondisi buruk matriks C: {kondisi_buruk}.")
