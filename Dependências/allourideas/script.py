
import os
import pandas as pd

def Union(lst1, lst2):
    final_list = list(set(lst1) | set(lst2))
    return final_list

def Matchmaker(lsttuple, lst):
    final = []
    for str in lst:
        for tuple in lsttuple:
         if str == tuple[0]:
            final.append(tuple[1])
    return list(dict.fromkeys(final))

def intersection(lst1, lst2):
    lst3 = [value for value in lst1 if value in lst2]
    return lst3

path_of_the_directory = r"F:\Pesquisa TAITI\Dependências\allourideas"
degreeofdependence= 80
df = pd.read_csv('https___github.com_allourideas_allourideas.org.csv',engine="python", sep=';')


testIwithDeps = []
precision = []
recall = []
f2= []
precisiondeps = []
recalldeps = []
f2deps= []
index=0

for filename in os.listdir(path_of_the_directory):
    if filename.endswith('.csv') and not filename.startswith("http") and (pd.read_csv(filename, sep=";")).values.tolist() == []:

            Taiti= df.at[index,'TestI'][1:-1].split(",")
            #Taiti= [x.strip(' ') for x in Taiti]
            Changed= df.at[index,'Changed files'][1:-1].split(",")

            precisionTemp = len(intersection(Taiti,Changed))/len(Taiti)
            recallTemp = len(intersection(Taiti,Changed))/len(Changed)
            if (4* precisionTemp + recallTemp == 0):
             f2Temp = "Null"
            else: f2Temp = (5*precisionTemp*recallTemp)/ (4* precisionTemp + recallTemp)

            testIwithDeps.append(Taiti)
            precision.append(precisionTemp)
            recall.append(recallTemp)
            precisiondeps.append(precisionTemp)
            recalldeps.append(recallTemp)
            f2.append(f2Temp)
            f2deps.append(f2Temp)

            index = index+1
            continue

    if filename.endswith('.csv') and not filename.startswith("http"):

        df1 = pd.read_csv(filename, engine="python", sep=',')
        df1.drop(df1[df1['degree'] > degreeofdependence ].index, inplace = True)

        weaklogicaldependence=df1['coupled'].tolist()

        stronglogicaldependence=df1['entity'].tolist()

        compare = list(zip(stronglogicaldependence,  weaklogicaldependence))


        Taiti= df.at[index,'TestI'][1:-1].split(",")
        Changed= df.at[index,'Changed files'][1:-1].split(",")

        Taiti= [x.strip(' ') for x in Taiti]

        Final = Matchmaker(compare,Taiti)

        testIwithDepstemp = Union(Final, Taiti)

        precisionTemp = len(intersection(Taiti,Changed))/len(Taiti)


        recallTemp = len(intersection(Taiti,Changed))/len(Changed)

        precisiondepsTemp = len(intersection(testIwithDepstemp,Changed))/ len(testIwithDepstemp)


        recalldepsTemp = len(intersection(testIwithDepstemp,Changed))/ len(Changed)



        if (4* precisionTemp + recallTemp == 0):
            f2Temp = "Null"
        else: f2Temp = (5*precisionTemp*recallTemp)/ (4* precisionTemp + recallTemp)

        if (4* precisiondepsTemp + recalldepsTemp == 0):
            f2depsTemp = "Null"
        else: f2depsTemp = (5*precisiondepsTemp*recalldepsTemp)/ (4* precisiondepsTemp + recalldepsTemp)

        testIwithDeps.append(testIwithDepstemp)
        precision.append(precisionTemp)
        recall.append(recallTemp)
        precisiondeps.append(precisiondepsTemp)
        recalldeps.append(recalldepsTemp)
        f2.append(f2Temp)
        f2deps.append(f2depsTemp)


        index = index+1

df['TestIWithDeps'] = testIwithDeps
df['Precision'] = precision
df['Recall'] = recall
df['F2'] = f2
df['PrecisionDeps'] = precisiondeps
df['RecallDeps'] = recalldeps
df['F2Deps'] = f2deps


df.to_excel('TaitiWithdeps-allourideas.xlsx', index=False)




