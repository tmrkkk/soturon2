#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import re
import os
import pandas as pd
import MeCab
from CustomMeCabTagger import *
from Preprocessing import *


VorW = "wolf_win"

path_list = os.listdir(VorW)

#path_list = os.listdir('wolf_win')

result = pd.Series() #頻度記入用

res_k2 = pd.Series()
res2 = pd.Series()

tag = CustomMeCabTagger()
col_names = ['c{0:02d}'.format(i) for i in range(1)]


for path in path_list:
    name = path[:-4]
    #Preprocessing(name, VorW) #前処理
    print(path)


    df = pd.read_csv(VorW + "/" + name + ".csv", header=None, names = col_names)#データ読み込み

    for index, row in df.iterrows():
        mor = tag.parseToDataFrame(str(row[0]))
        mor = mor.iloc[::-1]

        buf = ''
        flag=True
        for i, r in mor.iterrows():

            if 'する' in str(r[7]):
                buf = 'する'
                flag = False

            else:
                if '名詞' == str(r[1]) and 'サ変接続' == str(r[2]):
                    if flag == False:
                        buf = str(r[7]) + buf
                        flag=True
                        try:
                            result[buf] += 1
                        except KeyError:
                            result[buf] = 1
                            buf = ''
                else:
                    flag = True




#    res = result.sort_values(ascending = False)
#    res.to_csv('result1.csv')

#print("end1")



#res_k2.to_csv('result2.csv')
#print("end2")



    re_3 = re.compile(r'[\u4E00-\u9FFF][\u3041-\u309F]+[\u4E00-\u9FFF][\u3041-\u309F]')


    for index, row in df.iterrows():
        mor2 = tag.parseToDataFrame(str(row[0]))

        for i, r in mor2.iterrows():
            if re_3.fullmatch(str(r[7])) and '動詞' == str(r[1]):
                try:
                    res2[r[7]] += 1
                except KeyError:
                    res2[r[7]] = 1

#res2 = res2.sort_values(ascending = False)
#res2.to_csv('result3.csv')

#print("end3")

res = result.sort_values(ascending = False)
res.to_csv('result1.csv')


k2 = re.compile(r'^.*[\u4E00-\u9FFF]+.*[\u4E00-\u9FFF]+.*$')

for i,v in res.iteritems():
    if k2.fullmatch(i):
        res_k2[i] = v
res_k2.to_csv('result2.csv')

res2 = res2.sort_values(ascending = False)
res2.to_csv('result3.csv')


print("end")
