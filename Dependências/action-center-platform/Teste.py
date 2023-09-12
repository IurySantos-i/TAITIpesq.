#t
import pandas as pd
import os


df = (pd.read_csv('120_raw_gitlog.logdependencies.csv')).values.tolist()
print(df)

df2 =pd.read_csv('https___github.com_EFForg_action-center-platform.csv',sep=";")
print(df2)


