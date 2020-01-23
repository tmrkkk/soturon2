# -*- coding: utf-8 -*-

import pandas as pd
import MeCab

import sys

class CustomMeCabTagger(MeCab.Tagger):
    COLUMNS = ['表層形', '品詞', '品詞細分類1', '品詞細分類2', '品詞細分類3', '活用型', '活用形', '原型', '読み', '発音']

    def parseToDataFrame(self, text: str) -> pd.DataFrame:
        #テキストをparseした結果をPandas DataFrameとして返す

        results = []
        for line in self.parse(text).split('\n'):
            if line == 'EOS':
                break
            surface, feature = line.split('\t')
            feature = [None if f == '*' else f for f in feature.split(',')]
            results.append([surface, *feature])

        try:
            return pd.DataFrame(results, columns=type(self).COLUMNS)
        except ValueError:
            while len(results[0]) < 10:
                results[0].append("None")
            #print(len(results[0]))
            return pd.DataFrame(results, columns=type(self).COLUMNS)
