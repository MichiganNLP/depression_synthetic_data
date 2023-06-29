# %%
import openai
import pandas as pd
from argparse import ArgumentParser


parser = ArgumentParser()
parser.add_argument("-k", "--key",
                    help="OpenAI key", type = str)

parser.add_argument("-d", "--dir",
                    type = str,
                    help="Directory to write output", default = '../../../local/gpt3_data/synthetic_davinci_covid/data/')

args = parser.parse_args()

race_set = ['black', 'white', 'hispanic', 'asian']
gender_set = ['woman', 'man']
year_set = ['2020', '2021']

keys= args.k
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
    prompt_dict = {'p4': "I want you to act like a {race}{gender} who is feeling depressed. Write a blog post to descibe the main source of stress in your life.",
              'p5': "You are a {race} {gender} who is talking to a therapist.  Respond to the question, 'What is the main source of your stress?",
              'p6': "I want you to act like a {race} {gender} who is feeling depressed. Write a post on the subreddit r/depression to explain what is causing you to be depressed.",
              'p7': "You are a {race} {gender} who is talking to a therapist.  Respond to the question, 'Describe the biggest source of stress in your life at the moment'",
                'p4_cov': "I want you to act like a {race} {gender} who is feeling depressed in the year {year}. Write a blog post to descibe the main source of stress in your life",
            'p5_cov': "You are a {race} {gender} who is talking to a therapist in the year {year}. Respond to the question, 'What is the main source of your stress?",
            'p6_cov': "I want you to act like a {race} {gender} who is feeling depressed in the year {year}. Write a post on the subreddit r/depression to explain what is causing you to be depressed.",
            'p7_cov': "You are a {race} {gender} who is talking to a therapist in the year {year}.  Respond to the question, 'Describe the biggest source of stress in your life at the moment'"
    }

    tokens_dict = [ 'p4': 35,
              'p5': 31,
              'p6': 34, 
              'p7': 34,
              'p4_cov': 37,
              'p5_cov': 32,
              'p6_cov': 38,
              'p7_cov': 34
    ]
    output_dir = args.o

    prompt = prompt_dict['p4']
    tok = tokens_dict['p4']

    #generating non-covid data
    total_tok = int(400/4) + tok

    df = generate_samples(total_tok, 1)
    df.to_csv(output_dir + prompt + '_' + str(total_tok) + '.csv')

    prompt = prompt_dict['p4_cov']
    tok = tokens_dict['p4_cov']

    #generating covid data
    total_tok = int(400/4) + tok
    df = generate_samples(total_tok, 1, '2020')
    df.to_csv(output_dir + prompt + '_' + str(total_tok) + '.csv')
