
from time import sleep
import pandas as pd


df = pd.read_csv('tasks_990 - tasks_990.csv', engine="python", sep=';', on_bad_lines='skip', index_col=[0])

df = df.query("LAST == 'b0ce43166acd9c4b137851fbcff82e283ef32d0a' | LAST == '78f44872c591c32f463d5de782e6dd205a5c50de' | LAST == '3a54d9cc80f72418b75b15e3221e9e8aba920a73'")

print(df)

df1 = pd.read_csv('converted_fileproinfo_resultadocrown.csv', engine="python", sep=';', on_bad_lines='skip', index_col=[0])

df1 = df1.query("Task == '1000' | Task == '879' | Task == '18'")

df1 = df1.loc[:, ~df1.columns.str.contains('^Unnamed')]


print(df1)
taiti = pd.read_csv('resultadoTAITI.csv', engine="python", sep=';', on_bad_lines='skip', index_col=[0])

TestI= taiti['TestI'].str.split(',').values.tolist()

#taiti = taiti.drop('TestI', axis=1, errors='ignore')
print(taiti)

TestI[0]=TestI[0][1:]
TestI[-1] =  TestI[-1][:-1]
taiti[TestI] = TestI


print(taiti)
taiti.to_excel('Explode.xlsx')
#taiti=taiti.explode('TestI')

#print(taiti)

#taiti.to_excel('final.xlsx')

#sleep(6000)
