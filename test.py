import numpy as np
import torch
a = np.array([[1,2], [3,4], [5,6]])
a = torch.tensor(a, dtype = float)

print(torch.std(a, dim=1))
