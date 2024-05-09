import warnings
warnings.filterwarnings('ignore')
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics.pairwise import cosine_similarity
from collections import defaultdict
from sklearn.metrics import mean_squared_error

CHARGEMENT DE DONNEES :

df=pd.read_csv('/content/Copynew.csv')
np.random.seed(42)
df['rating'] = np.random.randint(1, 6, size=len(df))
df = pd.DataFrame(df)
df

TRAITEMENT DE DONNEES :

from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
cols = ['user_id', 'song_id']
df[cols] = df[cols].apply(LabelEncoder().fit_transform)
df.head()
users = df.user_id
ratings_count = dict()
for user in users:
    if user in ratings_count:
        ratings_count[user] += 1
    else:
        ratings_count[user] = 1
      
RATINGS_CUTOFF = 90
remove_users = []
for user, num_ratings in ratings_count.items():
    if num_ratings < RATINGS_CUTOFF:
        remove_users.append(user)
      df = df.loc[~df.user_id.isin(remove_users)]

songs = df.song_id
ratings_count = dict()
for song in songs:

    if song in ratings_count:
        ratings_count[song] += 1
    else :
        ratings_count[song] = 1

RATINGS_CUTOFF = 120
remove_songs = []
for song, num_ratings in ratings_count.items():
    if num_ratings < RATINGS_CUTOFF:
        remove_songs.append(song)
df_final= df.loc[~df.song_id.isin(remove_songs)]

df_final = df_final[df_final.listen_count<=5]
df_final.reset_index(drop=True, inplace=True)
df_final.head()

print(df_final.groupby(['title']).sum().sort_values('listen_count', ascending=False).index[0])
df_final.groupby(['title']).sum().sort_values('listen_count', ascending=False).song_id[0]
df_final.groupby(['user_id']).sum().sort_values('listen_count', ascending=False).index[0]

num_songs_per_yr = df.groupby('year')['listen_count'].count().to_frame()
num_songs_per_yr = num_songs_per_yr[num_songs_per_yr.index != 0]
num_songs_per_yr.tail()












