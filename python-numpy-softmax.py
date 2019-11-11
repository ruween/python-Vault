import numpy as np

# Write a function that takes as input a list of numbers, and returns
# the list of values given by the softmax function.
def softmax(L):
    expL = np.exp(L)
    sumExpL = sum(expL)
    result = []
    
    for i in expL:
        result.append(i*1.0/sumExpl)
    return result

    # else use the np.divide function
def softmax2(L):
    expL = np.exp(L)
    return np.divide(expL, expL.sum())
    pass
