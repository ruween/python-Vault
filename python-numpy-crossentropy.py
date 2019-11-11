import numpy as np

# Write a function that takes as input two lists Y, P,
# and returns the float corresponding to their cross-entropy.
# def cross_entropy(Y, P):
#     sum = 0
#     for y,p in zip(Y,P):
#         return -np.sum(y* np.log(p) + (1-y)* np.log(1-p)) 
#     pass

def cross_entropy(Y, P):
    sum = 0
    for y,p in zip(Y, P):
        temp = y * np.log(p) + (1-y) * np.log(1-p)
        sum += temp
    return -(sum)


Prob = [0.2, 0.3, 0.1]
Yval = [1,1,0]

jj = cross_entropy(Yval, Prob)
jj
