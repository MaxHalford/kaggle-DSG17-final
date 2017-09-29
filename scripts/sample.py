import numpy as np
import pandas as pd

NB_OBS = 200
np.random.seed(42)

train_df = pd.read_csv('data/train.csv', sep=';')

material_ids = train_df['Material'].unique()
mids_sample = np.random.choice(material_ids, NB_OBS)

train_df = train_df[train_df['Material'].isin(mids_sample)]
train_df.to_csv('data/train_sample.csv')
