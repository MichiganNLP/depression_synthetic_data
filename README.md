# Towards Algorithmic Fidelity: Mental Health Representation across Demographics in Synthetic vs. Human-generated Data

[[Paper]](https://arxiv.org/abs/2403.16909)
[[ACL Anthology page]](TODO)
[[Poster]](TODO)


This work proposes to study the application of GPT-3 as a synthetic data generation tool for mental health, by analyzing its *Algorithmic Fidelity*, a term coined by Argyle et al 2022 to refer to the ability of LLMs to approximate real-life text distributions.

We hope our work contributes to the study of synthetic data generation and helps researchers analyze and understand how closely GPT-3 can mimic real-life depression data.

For more information, read our [COLING 2024](https://lrec-coling-2024.org/) paper:

[Towards Algorithmic Fidelity: Mental Health Representation across Demographics in Synthetic vs. Human-generated Data](https://arxiv.org/abs/2403.16909)

By [Shinka Mori](https://shinkam.github.io/), [Oana Ignat](https://oanaignat.github.io/), [Andrew Lee](https://ajyl.github.io/), and [Rada Mihalcea](https://web.eecs.umich.edu/~mihalcea/).


## Data
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

### Prompts
    - p4 = 'I want you to act like a {race}{gender} who is feeling depressed. Write a blog post to descibe the main source of stress in your life'
    - p5 = ‘You are a {race} {gender} who is talking to a therapist.  Respond to the question, ‘What is making you feel depressed?’
    - p6 = 'I want you to act like a {race} {gender} who is feeling depressed. Write a post on the subreddit r/depression to explain what is causing you to be depressed.'
    - p7 = "You are a {race} {gender} who is talking to a therapist.  Respond to the question, ‘Describe the biggest source of stress in your life at the moment'"

### Notes 
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

## Citation

```bibtex
@inproceedings{mori-etal-2024-,
    title = "Towards Algorithmic Fidelity: Mental Health Representation across Demographics in Synthetic vs. Human-generated Data",
    author = "Mori, Shinka  and
      Ignat, Oana  and
      Lee, Andrew  and
      Mihalcea, Rada",
    booktitle = "TODO",
    month = may,
    year = "2024",
    address = "Torino, Italia",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/TODO",
    pages = "284--294",
    abstract = "",
    series = {COLING '24}
}
```
