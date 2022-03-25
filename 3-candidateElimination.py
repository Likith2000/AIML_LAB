dataarr = []
with open('3-candidateEliminationData.csv') as f:
    for line in f:
        dataarr.append(line.strip().split(','))

rows = len(dataarr)
cols = len(dataarr[0]) - 1
shypo = ['0']*(cols)
ghypo = [['?']*(cols)]

print("Initial Specific Hypothesis is = ", shypo)
print("Initial General Hypothesis is = ", ghypo)

for x in range(1, rows):
    lst = dataarr[x]

    if lst[cols] == "1":
        for i in range(cols):
            if shypo[i] == lst[i]:
                continue
            else:
                if shypo[i] == '0':
                    shypo[i] = lst[i]
                else:
                    shypo[i] = '?'
                for g in ghypo:
                    if g[i] != '?' and shypo[i] == '?':
                        ghypo.remove(g)
    else:
        ghypo.clear()
        for i in range(cols):
            if lst[i] != shypo[i] and shypo[i] != '?':
                temp_list = ['?']*i + [shypo[i]] + (['?']*(cols-1-i))
                if temp_list not in ghypo:
                    ghypo.append(temp_list)

    print("S Hypothesis after row ", x, " = ", shypo)
    print("G Hypothesis after row ", x, " = ", ghypo)

print("Final SHypothesis ", shypo)
print("Final GHypothesis ", ghypo)
