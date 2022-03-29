import pandas as pd
from collections import Counter
import math


def entropy(alist):
    count = Counter(x for x in alist)
    length = len(alist)
    prob = [x / length for x in count.values()]
    return sum([-p*math.log(p, 2) for p in prob])


def gain(data, target, split):
    splitting = data.groupby(split)
    n = len(data.index)
    agent = splitting.agg({target: [entropy, lambda x: len(x)/n]})[target]
    agent.columns = ['Entropy', 'observations']
    newentropy = sum(agent['Entropy'] * agent['observations'])
    oldentropy = entropy(data[target])
    return oldentropy - newentropy


def id3(sub, target, a):
    count = Counter(x for x in sub[target])
    if len(count) == 1:
        return next(iter(count))
    else:
        Igain = [gain(sub, target, attr) for attr in a]
        print("Gain=", Igain)
        maximum = Igain.index(max(Igain))
        best = a[maximum]
        print("Best Attribute:", best)
        tree = {best: {}}
        remaining = [i for i in a if i != best]
        for val, subset in sub.groupby(best):
            subtree = id3(subset, target, remaining)
            tree[best][val] = subtree
        return tree


data = pd.read_csv('4-id3Data.csv')
names = list(data.columns)
print("List of Attributes:", names)
names.remove('answer')
print("Predicting Attributes:", names)
tree = id3(data, 'answer', names)
print("\n\nThe Resultant Decision Tree is :\n")
print(tree)
