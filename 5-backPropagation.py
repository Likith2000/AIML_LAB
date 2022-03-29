import numpy as np

X = np.array(([2, 9], [1, 5], [3, 6]), dtype=float)
y = np.array(([92], [86], [89]), dtype=float)
X = X/np.amax(X, axis=0)
y = y/100


def sigmoid(x):
    return 1/(1 + np.exp(-x))


def derivatives_sigmoid(x):
    return x * (1 - x)


epoch = 5
lr = 0.1
inputlayer_neurons = 2
hiddenlayer_neurons = 3
output_neurons = 1

wh = np.random.uniform(size=(inputlayer_neurons, hiddenlayer_neurons))
bh = np.random.uniform(size=(1, hiddenlayer_neurons))
wout = np.random.uniform(size=(hiddenlayer_neurons, output_neurons))
bout = np.random.uniform(size=(1, output_neurons))

for i in range(epoch):
    hinp = np.dot(X, wh)
    hinp += bh
    hlayer_out = sigmoid(hinp)
    outinp = np.dot(hlayer_out, wout)
    outinp += bout
    output = sigmoid(outinp)

    EO = y-output
    d_output = EO * derivatives_sigmoid(output)
    EH = d_output.dot(wout.T)
    d_hiddenlayer = EH * derivatives_sigmoid(hlayer_out)
    wout += hlayer_out.T.dot(d_output) * lr
    wh += X.T.dot(d_hiddenlayer) * lr

    print("-----------Epoch-", i+1, "Starts----------")
    print("Input: \n" + str(X))
    print("Actual Output: \n" + str(y))
    print("Predicted Output: \n", output)
    print("-----------Epoch-", i+1, "Ends----------\n")
