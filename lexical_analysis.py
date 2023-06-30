import sys
# caution: path[0] is reserved for script path (or '' in REPL)
sys.path.insert(1, '/home/shinkamo/umd-odh/language_analysis')
from llr import llr_compare
# from bayesequal import get_deltas
from helper import Vocab, read_prior
import sys
sys.path.insert(1, '/home/shinkamo/umd-odh/language_analysis')
from llr import llr_compare
from bayesequal import get_deltas
# from helper import *
import json
import pandas as pd 




from liwc import LIWCTransformer
import pandas as pd

"""
@params: 
df = data with demographics and depression text
group1 = first group to compare
group2 = second group to compare
gender = true if comparing gender

"""
def get_analysis(df, group1, group2, gender = True):
    if gender:
        df1 = df.loc[df['gender'] == group1]
        df2 = df.loc[df['gender'] == group2]
    else:
        df1 = df.loc[df['race'] == group1]
        df2 = df.loc[df['race'] == group2]
    countera, counterb = Vocab(df1, df2, category='vocab', do_filter = False).get_frequencies()
    
    prior = read_prior('word_prior.txt')    

    diff = llr_compare(countera, counterb)
    delta = get_deltas(countera, counterb, prior)
    def to_df(delta, countera, counterb):
        liwc = []
        delta_val = []
        a = []
        b = []

        for v in delta.keys():
            liwc.append(v)
            delta_val.append(delta[v])
            a.append(countera[v])
            b.append(counterb[v])
        df = pd.DataFrame(list(zip(liwc, delta_val, a, b)), columns=['liwc', 'delta', group1, group2])
        return df
    df = to_df(delta, countera, counterb)
    df.to_csv('word_analysis/'+group1 + '_' + group2 + '.csv')#write the complete log-odds to csv

    #get top-30 log odds
    group1 = df.loc[df['delta']>0][['delta', 'liwc']].sort_values(['delta'], ascending=False)[:30].reset_index(drop=True)
    cols = group1.columns.tolist()
    cols = cols[-1:] + cols[:-1]
    group1 = group1[cols]  
    group2 = df.loc[df['delta']<0][['delta', 'liwc']].sort_values(['delta'])[:30].reset_index(drop=True)
    cols = group2.columns.tolist()
    cols = cols[-1:] + cols[:-1]
    group2 = group2[cols]  
    comp = pd.concat([group1, group2], axis=1, join='inner')
    comp = comp.round(2)

    with open('word_analysis/comparison/' + group1 + '_'+ group2 + '.txt', 'w') as f:
        f.writelines('|' + '|'.join(list(comp.columns)) + '|\n')
        f.writelines('|--------|-------|-------|-------|\n')
        for row in comp.itertuples():
            value = [str(r) for r in list(row)[1:]]
            f.writelines('|' + '|'.join(value) + '|\n')


if __name__ == "__main__":
    datadir = "../../../local/gpt3_data/synthetic_davinci_covid/data/"
    df = pd.read_csv(datadir+'non_covid_and_covid.csv', index_col=0)
    df.rename({'race':"races"}, inplace=True)
    get_analysis(df, 'woman', 'man', True)
    get_analysis(df, 'white', 'black', False)
    get_analysis(df, 'white', 'asian', False)
    get_analysis(df, 'white', 'hispanic', False)
    get_analysis(df, 'asian', 'hispanic', False)
    get_analysis(df, 'asian', 'black', False)
    get_analysis(df, 'hispanic', 'black', False)










    


