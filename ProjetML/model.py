import pandas as pd
import numpy as np
import pickle
from sklearn.neighbors import KNeighborsClassifier


df = pd.read_csv("data/labels.csv",",",encoding='utf-8', low_memory=False)

X = df[['hate_speech','offensive_language','neither']]
y = df['tweet']
neigh = KNeighborsClassifier(n_neighbors=3)
neigh.fit(X, y)
neigh.predict(X)
