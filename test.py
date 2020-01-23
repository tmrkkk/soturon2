# -*- coding: utf-8 -*-
import pandas as pd

path = "villager_win_test/Pvillage_g18.csv"

col_names = ['c{0:02d}'.format(i) for i in range(1)]
df = pd.read_csv(path, header=None, names = col_names)#データ読み込み

print(df)
