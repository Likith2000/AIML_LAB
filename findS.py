# FIND S ALGO
import pandas as pd
import numpy as np

data = pd.read_csv("data1.csv")

d = np.array(data)[:, :-1]
print("\nThe attributes are:\n", d)

target = np.array(data)[:, -1]
print("\nThe target is:", target)


def train(c, t):
    specific_hypothesis = 1
    for i, val in enumerate(t):
        if val == 'Yes':
            specific_hypothesis = c[i].copy()
            break

    for i, val in enumerate(c):
        if t[i] == "Yes":
            for x in range(len(specific_hypothesis)):
                if val[x] != specific_hypothesis[x]:
                    specific_hypothesis[x] = '?'
                else:
                    pass

    return specific_hypothesis


print("\nThe final hypothesis is:", train(d, target))
