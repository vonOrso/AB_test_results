# Checking AB-test results
### Introduction
Hello everyone, this is a small analysis of the AB test. There is a lot of user data, so a z-test will be used. A little data processing will also be carried out, since the data is not so simple.
##### The project consists of three files:

  - ab_data.csv - File with AB test results;
  - A_B_Testing.ipynb - The main notebook that contains all steps;
  - sup_defs.py - Contains one function for visualization (I prefer to put visualization elements in a separate file).
### What we have?
Dataset from Kaggle: A/B testing (https://www.kaggle.com/zhangluyuan/ab-testing).
The description of the dataset is very cryptic (missing), so I will set a small task for myself.
### Selecting a task and completing it
##### Task
Our company selling various accessories decided to change the design of the site. The company's management believes that pictures with cats should be removed from the main page of the site and its design should be made more neutral. In this situation, you need to test the effectiveness of the new design in comparison with the old one.
##### What was done
There were no gaps in the data, but there was a mismatch between the 'group' and 'landing_page' columns. The same page was shown to one user, but he was assigned to different groups. Another user was shown different pages but was assigned to the same group. If during A-B testing both options are shown to one user, he should belong to different groups, and if there is one option, then the group should be the same. Most likely, the system began to incorrectly count users into groups and if you remove all inconsistencies, all duplicate users disappear (except one). But just in case, it is better not to take this user into account either.

After processing the data, it is necessary to determine the number of observations sufficient to conduct the test. As always, we will test the null hypothesis H0, which states that there are no significant differences between the new and old designs. We will also test the alternative hypothesis H1, which states that there are still differencesare still differences. I see no need to break the "gold standard" and chose alpha = 0.05, power = 0.8. The proportion_effectsize function calculates the effect size for a test comparing two proportions. The conversion rate is currently 12%, with the new page we expect this to increase by 2%. We need 4433 observations for each group.
##### Results
Statistics:
  - z statistic: 0.395
  - p-value: 0.693
  - ci 95% Control group: [0.110, 0.129]
  - ci 95% Reatment group: [0.107, 0.126]

The calculated p-value is much greater than 0.05, which means that the null hypothesis cannot be rejected. Interestingly, our theoretical estimate of 14% conversion on a new page is not even within the confidence interval. Thus, we determined that the old design with cats and the more neutral new one are not much different from each other.
![download](https://user-images.githubusercontent.com/43719238/153754001-f49fe25a-10e9-45c5-924f-0d09f8047519.png)
