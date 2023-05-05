import sys
# caution: path[0] is reserved for script path (or '' in REPL)
sys.path.insert(1, '/home/shinkamo/umd-odh/language_analysis')
from llr import llr_compare
# from bayesequal import get_deltas
from helper import Vocab, read_prior
import sys
# caution: path[0] is reserved for script path (or '' in REPL)
sys.path.insert(1, '/home/shinkamo/umd-odh/language_analysis')
from llr import llr_compare
from bayesequal import get_deltas
# from helper import *
import json
import pandas as pd 




from liwc import LIWCTransformer
import pandas as pd
# import pandas as pd 

# datadir ='../../../local/gpt3_data/synthetic_davinci/'
# df = pd.read_csv(datadir+'p2_p4_p5_p6_p7.csv', index_col=0)
# df.rename({'race':"races"}, inplace=True)

# woman = df.loc[df['gender'] == 'woman']
# man = df.loc[df['gender'] == 'man']

# voc = Vocab(woman, man, category='vocab', tokenized='text')

# w, b = voc.get_frequencies()
# liwc_transformer = LIWCTransformer()
# # print(liwc_transfo
# # rmer.classify(['upcoming ']))

# datadir ='../../../local/gpt3_data/synthetic_davinci/'
# df = pd.read_csv(datadir+'p2_p4_p5_p6_p7.csv', index_col=0)
# df.rename({'race':"races"}, inplace=True)

# # woman = df.loc[df['gender'] == 'woman']
# # man = df.loc[df['gender'] == 'man']
# woman = df.loc[df['race'] == 'white']
# man = df.loc[df['race'] == 'black']
# print(woman)
# voc = Vocab(woman, man, category='liwc')
# # breakpoint()
# countera, counterb = voc.get_frequencies()
# # print(countera, counterb)
# # print(counterb)

# diff = llr_compare(countera, counterb)
# print(diff)
# # entries, cache, dim = liwc_transformer.get_feature()
# # # print(cache)
# # word, matched, count = liwc_transformer.classify(['yup', 'without'])
# prior = read_prior('sample.pkl', 'liwc')
# delta = get_deltas(countera, counterb, prior)
# print(delta)
def get_analysis(df, group1, group2, gender = True):
    if gender:
        df1 = df.loc[df['gender'] == group1]
        df2 = df.loc[df['gender'] == group2]
    else:
        df1 = df.loc[df['race'] == group1]
        df2 = df.loc[df['race'] == group2]
    # print(df1)
    # breakpoint()
    countera, counterb = Vocab(df1, df2, category='liwc', do_filter = False).get_frequencies()
    # print('countera\n', countera)
    # print(counterb)
    prior = read_prior('/home/shinkamo/depression_synthetic_data_project/sample_prior_reddit.pkl', 'liwc')    
    # print(prior)
    # prior = read_prior('/home/shinkamo/depression_synthetic_data_project/sample.pkl', 'liwc')    
    diff = llr_compare(countera, counterb)
    # print(diff)
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
        df = pd.DataFrame(list(zip(liwc, delta_val, a, b)), columns=['liwc', 'delta', 'a', 'b'])
        return df
    df = to_df(delta, countera, counterb)
    print('analysis/delta/'+group1 + '_' + group2 + '.csv')
    df.to_csv('analysis/delta/'+group1 + '_' + group2 + '.csv')
    # with open('analysis/llr/'+group1 + '_' + group2 + '.json', 'w') as f:
    #     json.dump([{f"liwc": v, "delta": diff[v], "a": countera[v], "b": counterb[v]} for v in diff.keys()], f)
    # with open('analysis/delta/'+group1 + '_' + group2 + '.json', 'w') as f:
    #     json.dump([{f"liwc": v, "delta": delta[v], "a": countera[v], "b": counterb[v]} for v in delta.keys()], f)
    # print('diff\n', diff)
    # print('delta\n', delta)
    # print(prior)

if __name__ == "__main__":
    datadir ='../../../local/gpt3_data/synthetic_davinci/'
    # df = pd.read_csv(datadir+'p2_p4_p5_p6_p7.csv', index_col=0)
    df = pd.read_csv(datadir+'p4_5_6_7.csv', index_col=0)

    # df.rename({'race':"races"}, inplace=True)
    get_analysis(df, 'woman', 'man', True)
    get_analysis(df, 'white', 'black', False)
    get_analysis(df, 'white', 'asian', False)
    get_analysis(df, 'white', 'hispanic', False)
    get_analysis(df, 'asian', 'hispanic', False)
    get_analysis(df, 'asian', 'black', False)
    get_analysis(df, 'asian', 'white', False)
    get_analysis(df, 'hispanic', 'black', False)
    get_analysis(df, 'hispanic', 'asian', False)
    get_analysis(df, 'hispanic', 'white', False)
    get_analysis(df, 'black', 'white', False)
    get_analysis(df, 'black', 'asian', False)
    get_analysis(df, 'black', 'hispanic', False)










    


