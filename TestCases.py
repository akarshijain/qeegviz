# %%
import numpy as np

# %%
import pandas as pd

# %%
from CalculateICC import CalculateICC

# %%
import random

# %%
def display(objectName):
    print('MSp = ', objectName._generateMSP())
    print('MSe = ', objectName._generateMSE())
    print('ICC = ', objectName.generateICC())

# %%
def save_to_excel(testCaseDict, filename):
    df = pd.DataFrame(data=testCaseDict)
    df.to_excel(f'{filename}.xlsx')

# %%
SUBJECTS_LIST = ['sub1', 'sub2', 'sub3', 'sub4', 'sub5', 'sub6', 'sub7', 'sub8', 'sub9', 'sub10', 'sub 11', 'sub12']
numSubjects = len(SUBJECTS_LIST)
numSessions = 100

# %% [markdown]
# #### Test Case 1: msp ~ mse

# %%
testCase1_dict = {}

# %%
mu, sigma = 100, 100000
for subject in SUBJECTS_LIST:
    testCase1_dict[subject] = np.random.normal(mu, sigma, numSessions)
    mu += 0.5

# %%
testCase1 = CalculateICC(testCase1_dict)

# %%
display(testCase1)

# %%
save_to_excel(testCase1_dict, 'testCase1')

# %% [markdown]
# #### Test Case 2: msp < mse

# %%
testCase2_dict = {}

# %%
mu, sigma = 100, 500000
for subject in SUBJECTS_LIST:
    testCase2_dict[subject] = np.random.normal(mu, sigma, numSessions)
    mu += 0.00005

# %%
testCase2 = CalculateICC(testCase2_dict)

# %%
display(testCase2)

# %%
save_to_excel(testCase2_dict, 'testCase2')

# %% [markdown]
# #### Test Case 3: msp >> mse

# %%
testCase3_dict = {}

# %%
mu, sigma = 100, 10
for subject in SUBJECTS_LIST:
    testCase3_dict[subject] = np.random.normal(mu, sigma, numSessions)
    mu += 500

# %%
testCase3 = CalculateICC(testCase3_dict)

# %%
display(testCase3)

# %%
save_to_excel(testCase3_dict, 'testCase3')

# %% [markdown]
# #### Test Case 4: msp << mse

# %%
testCase4_dict = {}

# %%
mu, sigma = 0, 100000
for subject in SUBJECTS_LIST:
    testCase4_dict[subject] = np.random.normal(mu, sigma, numSessions)
    mu += 0.0001

# %%
testCase4 = CalculateICC(testCase4_dict)

# %%
display(testCase4)

# %%
save_to_excel(testCase4_dict, 'testCase4')


