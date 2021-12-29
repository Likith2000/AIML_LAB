import numpy as np

# define Unit Step Function


def unitStep(v):
    if v >= 0:
        return 1
    else:
        return 0

# design Perceptron Model


def perceptronModel(x, w, b):
    v = np.dot(w, x) + b
    y = unitStep(v)
    return y

# AND Logic Function
# w1 = 1, w2 = 1, b = -1.5


def AND_logicFunction(x):
    w = np.array([-1, -1])
    b = 1.5
    return perceptronModel(x, w, b)


# testing the Perceptron Model
test1 = np.array([0, 1])
test2 = np.array([1, 1])
test3 = np.array([0, 0])
test4 = np.array([1, 0])

print("NAND({}, {}) = {}".format(0, 0, AND_logicFunction(test3)))
print("NAND({}, {}) = {}".format(0, 1, AND_logicFunction(test1)))
print("NAND({}, {}) = {}".format(1, 0, AND_logicFunction(test4)))
print("NAND({}, {}) = {}".format(1, 1, AND_logicFunction(test2)))


def OR_logicFunction(x):
    w = np.array([-1, -1])
    b = 0.5
    return perceptronModel(x, w, b)


# testing the Perceptron Model
test1 = np.array([0, 1])
test2 = np.array([1, 1])
test3 = np.array([0, 0])
test4 = np.array([1, 0])
print("\n")
print("NOR({}, {}) = {}".format(0, 0, OR_logicFunction(test3)))
print("NOR({}, {}) = {}".format(0, 1, OR_logicFunction(test1)))
print("NOR({}, {}) = {}".format(1, 0, OR_logicFunction(test4)))
print("NOR({}, {}) = {}".format(1, 1, OR_logicFunction(test2)))
