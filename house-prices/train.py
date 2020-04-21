import pandas as pd
from sklearn.ensemble import RandomForestRegressor

path_to_train = 'output/raw/train.csv'

df = pd.read_csv(path_to_train)
