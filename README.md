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
@inproceedings{mori-etal-2024-towards-algorithmic,
    title = "Towards Algorithmic Fidelity: Mental Health Representation across Demographics in Synthetic vs. Human-generated Data",
    author = "Mori, Shinka  and
      Ignat, Oana  and
      Lee, Andrew  and
      Mihalcea, Rada",
    editor = "Calzolari, Nicoletta  and
      Kan, Min-Yen  and
      Hoste, Veronique  and
      Lenci, Alessandro  and
      Sakti, Sakriani  and
      Xue, Nianwen",
    booktitle = "Proceedings of the 2024 Joint International Conference on Computational Linguistics, Language Resources and Evaluation (LREC-COLING 2024)",
    month = may,
    year = "2024",
    address = "Torino, Italy",
    publisher = "ELRA and ICCL",
    url = "https://aclanthology.org/2024.lrec-main.1423",
    pages = "16378--16391",
    abstract = "Synthetic data generation has the potential to impact applications and domains with scarce data. However, before such data is used for sensitive tasks such as mental health, we need an understanding of how different demographics are represented in it. In our paper, we analyze the potential of producing synthetic data using GPT-3 by exploring the various stressors it attributes to different race and gender combinations, to provide insight for future researchers looking into using LLMs for data generation. Using GPT-3, we develop HeadRoom, a synthetic dataset of 3,120 posts about depression-triggering stressors, by controlling for race, gender, and time frame (before and after COVID-19). Using this dataset, we conduct semantic and lexical analyses to (1) identify the predominant stressors for each demographic group; and (2) compare our synthetic data to a human-generated dataset. We present the procedures to generate queries to develop depression data using GPT-3, and conduct analyzes to uncover the types of stressors it assigns to demographic groups, which could be used to test the limitations of LLMs for synthetic data generation for depression data. Our findings show that synthetic data mimics some of the human-generated data distribution for the predominant depression stressors across diverse demographics.",
}
```
