import pandas as pd

result = pd.Series()
resultA = pd.read_csv("v_result3.csv", header = None)
resultB = pd.read_csv("w_result3.csv", header = None)

for index,row in resultA.iterrows():
    #print(row)
    try:
        result[row[0]] += int(row[1])
    except KeyError:
        result[row[0]] = int(row[1])


for index,row in resultB.iterrows():
    try:
        result[row[0]] += int(row[1])
    except KeyError:
        result[row[0]] = int(row[1])


result.to_csv('sum_result3.csv')
