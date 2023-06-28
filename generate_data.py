# %%
import os
import openai
import pandas as pd
import json
from tqdm import tqdm
from collections import defaultdict
from argparse import ArgumentParser


parser = ArgumentParser()
parser.add_argument("-k", "--key",
                    help="OpenAI key", type = str)

parser.add_argument("-d", "--dir",
                    type = str,
                    help="Directory to write output", default = '../../../local/gpt3_data/synthetic_davinci_covid/data/')
parser.add_argument("-t", "-tok",
                    type = int,
                    help="Total tokens in prompt; check https://platform.openai.com/tokenizer")
args = parser.parse_args()

race_set = ['black', 'white', 'hispanic', 'asian']
gender_set = ['woman', 'man']
year_set = ['2020', '2021']
prompts = {}

keys='my key'#comment oit
openai.api_key = keys# os.getenv(keys)
output_dir = args.d
sample_dir = output_dir+'samples/'



def generate_samples(text, num_sample, total_tok, year = ''):
    dem_dict = {
        'gender': [],
        'race' : [],
        'tok': [],
        'total tok': [],
        'text': [],
        'reason': []
    }

    
    for g in gender_set:
        for r in race_set:
            if year:
                prompt = text.format(race = r, gender = g, year = year)
            else:
                prompt = text.format(race = r, gender = g)
            response = openai.Completion.create(
            model="text-davinci-002",
            prompt=prompt,
            max_tokens = total_tok,
            temperature = 0.9, 
            n = num_sample
            )
            # print(response)
            for i in range(num_sample):
                dem_dict['gender'].append(g)
                dem_dict['race'].append(r)
                dem_dict['tok'].append(response['usage']['completion_tokens']/num_sample)
                dem_dict['total tok'].append(response['usage']['prompt_tokens'])
                dem_dict['text'].append(response['choices'][i]['text'])
                dem_dict['reason'].append(response['choices'][i]['finish_reason'])
    
    results_df = pd.DataFrame.from_dict(dem_dict,orient='index').transpose()
            
    return results_df

if __name__ == "__main__":
    prompt = ["I want you to act like a {race}{gender} who is feeling depressed. Write a blog post to descibe the main source of stress in your life.",
              "You are a {race} {gender} who is talking to a therapist.  Respond to the question, 'What is the main source of your stress?",
              "I want you to act like a {race} {gender} who is feeling depressed. Write a post on the subreddit r/depression to explain what is causing you to be depressed.",
              "You are a {race} {gender} who is talking to a therapist.  Respond to the question, 'Describe the biggest source of stress in your life at the moment'"    
              ]
    prompt_covid = ["I want you to act like a {race} {gender} who is feeling depressed in the year {year}. Write a blog post to descibe the main source of stress in your life",
              "You are a {race} {gender} who is talking to a therapist in the year {year}. Respond to the question, 'What is the main source of your stress?",
              "I want you to act like a {race} {gender} who is feeling depressed in the year {year}. Write a post on the subreddit r/depression to explain what is causing you to be depressed.",
              "You are a {race} {gender} who is talking to a therapist in the year {year}.  Respond to the question, 'Describe the biggest source of stress in your life at the moment'"
    ]

    
    tok = args.t
    output_dir = args.o

    #generating non-covid data
    total_tok = int(400/4) + tok

    df = generate_samples(total_tok, 10)
    df.to_csv(output_dir + prompt + '_' + str(total_tok) + '.csv')

    #generating covid data
    total_tok = int(400/4) + tok
    df = generate_samples(total_tok, 10, '2020')
    df.to_csv(output_dir + prompt + '_' + str(total_tok) + '.csv')
