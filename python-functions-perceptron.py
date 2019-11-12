# Implement the following functions

# Activation (sigmoid) function
def sigmoid(x):
    result_sigmoid = 1 / (1 + np.exp(-x))
    return result_sigmoid
    pass

# Output (prediction) formula
def output_formula(features, weights, bias):
    
    WX_matrix = np.matmul(features, weights)
    y_hat = sigmoid(WX_matrix + bias)
    return y_hat
    pass

# Error (log-loss) formula
def error_formula(y, output):
    Err = -(y) * np.log(output) - (1-y) * np.log(1-output)
    return Err
    pass

# Gradient descent step
def update_weights(x, y, weights, bias, learnrate):

	output = output_formula(x, weights, bias)
	d_error = -(y - outputs)
	weights = weights - learnrate * d_error * x
	bias = bias - learnrate * d_error
	return weights,bias    
   
    pass
