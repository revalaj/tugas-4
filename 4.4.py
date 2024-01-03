import numpy as np

A = np.array([[1, 2], [3, 4]])
B = np.array([5, 6])
solusi = np.linalg.solve(A, B)
print(f"Solusi sistem persamaan linier: {solusi}.")
