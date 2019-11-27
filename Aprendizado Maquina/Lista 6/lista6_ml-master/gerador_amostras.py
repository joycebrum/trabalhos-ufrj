import pandas as pd 
import random
import numpy as np
from datetime import datetime

#importar dados do csv 


random.seed(datetime.now())

df = pd.read_csv('data_comma.csv') 

headers = df.columns


#gerando vetor de treino
n_rows = len(df.index)
n_train_samples = 172

samples_column = [ 0 for i in range(n_rows) ]

samples = random.sample( range(n_rows), n_train_samples )


for samp_ind in samples:
    samples_column[ samp_ind ] = 1
        
df['Is_Sample'] = samples_column

train = df['Is_Sample'] == 1
test =  df['Is_Sample'] == 0



df_test = df[test][headers]
df_train = df[train][headers]


df_train.to_csv('train_data.csv', index=False)
df_test.to_csv('test_data.csv', index=False)


