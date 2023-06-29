# depression_synthetic_data_project


### Data
All data is stored in the `local` repo.

- `headroom.csv`

  - The final dataset consisting of before/after COVID-19 samples

| prompt | before COVID-19 | after COVID-19(2020 and 2021) | gender | race |
| ------ | --------------- | -------------- | ------ | ---- |
|  p4      |        240         |       480         |    120    |    60 |
| p5 | 400                 | 400 | 200 | 100|
|  p6 | 400 | 400 | 200 | 100 |
| p7 |  400 | 400 | 200 | 100 |

Total : 3120

- Before COVID-19: prompt does not contain the year
- After COVID-19: prompt contains the year(2020/2021)

# Prompts
    - p4 = 'I want you to act like a {race}{gender} who is feeling depressed. Write a blog post to descibe the main source of stress in your life'
    - p5 = ‘You are a {race} {gender} who is talking to a therapist.  Respond to the question, ‘What is making you feel depressed?’
    - p6 = 'I want you to act like a {race} {gender} who is feeling depressed. Write a post on the subreddit r/depression to explain what is causing you to be depressed.'
    - p7 = "You are a {race} {gender} who is talking to a therapist.  Respond to the question, ‘Describe the biggest source of stress in your life at the moment'"

# Notes 
- `compare_topics.ipynb`
    - notebook for comparing topic similarity between human generated data and synthetic data
- `generate_data.py`
    - script for generating data
- `lexical_analysis.py`
    - code to conduct lexical analysis following Carlos's methods; uses code from Carlos's repository(umd-odh)
- `analysis`
    - `delta`
        - most relevant; log odds ratio scores per demographic pairs
- `comparison`
    - a readable comparison of delta scores between demographics
