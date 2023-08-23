import numpy as np
import fractions
np.set_printoptions(formatter={'all':lambda x: str(fractions.Fraction(x).limit_denominator())})

m = [[0, 1, 0, 1], [0, 0, 1/2, 0], [1/2, 0, 0, 0], [1/2, 0, 1/2, 0]]
M = np.array(m)
# print(M.shape)

v = [[1/4], [1/4], [1/4], [1/4]] 
v = np.array(v)
# print(v)

mult1 = np.dot(M, v)
mult2 = np.dot(M, mult1)

for num in range(1, 100):
    if np.allclose(mult1, mult2) == True: 
        break # Once they converge, break
    else:
        mult1 = mult2
        mult2 = np.dot(M, mult1)
print('The ranks converge at the %d iteration with the following ranks %s' %(num, mult2))

# m = [[0, 1, 1/2], [0, 0, 1/2], [1, 0, 0]]
# M = np.array(m)
# print(M.shape)

# v = [[1/3], [1/3], [1/3]]
# v = np.array(v)


# mult1 = np.dot(M, v)
# mult2 = np.dot(M, mult1)

# for num in range(1, 100):
#     if np.allclose(mult1, mult2) == True: 
#         break # Once they converge, break
#     else:
#         mult1 = mult2
#         mult2 = np.dot(M, mult1)
# print('The ranks converge at the %d iteration with the following ranks %s\n' %(num, mult2))

