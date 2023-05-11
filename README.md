# depression_synthetic_data_project
## Oana notes
### Code
- `lexical_analysis.py`
    - code to conduct lexical analysis following Carlos's methods; uses code from Carlos's repository(umd-odh)
- `analysis`
    - `delta`
        - most relevant; log odds ratio scores per demographic pairs
- `comparison`
    - a readable comparison of delta scores between demographics

### Data
All data is stored in the `local` repo.
-  `p4_5_6_7.csv1
    - most relevant dataset; combination of outputs from prompts 4, 5, 6, and 7
    - ~50 samples per group
    - p4 = 'I want you to act like a {race}{gender} who is feeling depressed. Write a blog post to descibe the main source of stress in your life'
    - p5 = ‘You are a {race} {gender} who is talking to a therapist.  Respond to the question, ‘What is making you feel depressed?’
    - p6 = 'I want you to act like a {race} {gender} who is feeling depressed. Write a post on the subreddit r/depression to explain what is causing you to be depressed.'
    - p7 = "You are a {race} {gender} who is talking to a therapist.  Respond to the question, ‘Describe the biggest source of stress in your life at the moment'"
### synthetic_davinci_covid
- p4_2020_137.csv
    - 15 samples from 2020 with prompt4
- p4_2020_137.csv
    - 15 samples from 2021 with prompt4
- p5_2020_132.csv
    - 15 samples from 2020 with prompt5
- p5_2021_132.csv
    - 15 samples from 2021 with prompt5
- p6_2020_138.csv
    - 15 samples from 2020 with prompt6
- p6_2021_138.csv
    - 15 samples from 2021 with prompt6
- p7_2020_137.csv
    - 15 samples from 2020 with prompt7
- p7_2021_137.csv
    - 15 samples from 2021 with prompt7



- p4_p5_p6_p7_2020.csv
    - all data from 2020 with prompts p4, 5, 6, 7

- p4_p5_p6_p7_2021.csv
    - all data from 2021 with prompts p4, 5, 6, 7  
- non_covid_and_covid
