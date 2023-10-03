
import os
import pandas as pd
import re

def atoi(text):
    return int(text) if text.isdigit() else text

def natural_keys(text):
    '''
    alist.sort(key=natural_keys) sorts in human order
    http://nedbatchelder.com/blog/200712/human_sorting.html
    (See Toothy's implementation in the comments)
    '''
    return [ atoi(c) for c in re.split(r'(\d+)', text) ]

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

path_of_the_directory = r"F:\Pesquisa TAITI\Dependências\sharetribe"

df = pd.read_csv('https___github.com_sharetribe_sharetribe.csv',engine="python", sep=';')


testIwithDeps = []
deps = []
precision = []
recall = []
f2= []
precisiondeps = []
recalldeps = []
f2deps= []
prodchangedfiles = []
testIwithFilteredDeps = []
filtereddeps = []
changedprecision = []
changedrecall = []
changedf2= []
changedprecisiondeps = []
changedrecalldeps = []
changedf2deps= []

index=0

for filename in sorted(os.listdir(path_of_the_directory), key = natural_keys):
    if filename.endswith('.csv') and not filename.startswith("http") and (pd.read_csv(filename, sep=";")).values.tolist() == []:

            Taiti= df.at[index,'TestI'][1:-1].split(",")
            Taiti = [x.strip(' ') for x in Taiti]

            Changed= df.at[index,'Changed files'][1:-1].split(",")
            Changed = [x.strip(' ') for x in Changed]


            precisionTemp = len(intersection(Taiti,Changed))/len(Taiti)
            recallTemp = len(intersection(Taiti,Changed))/len(Changed)
            if (4* precisionTemp + recallTemp == 0):
             f2Temp = 0
            else: f2Temp = (5*precisionTemp*recallTemp)/ (4* precisionTemp + recallTemp)

            testIwithDeps.append(Taiti)
            deps.append("")
            precision.append(precisionTemp)
            recall.append(recallTemp)
            precisiondeps.append(precisionTemp)
            recalldeps.append(recallTemp)
            f2.append(f2Temp)
            f2deps.append(f2Temp)

            # Métricas com filtradas de acordo com a pasta e com a extensão

            filteredChanged =  [s for s in Changed if (s.startswith('app') or s.startswith('lib')) and (s.endswith('.erb') or s.endswith('.rb') or s.endswith('.html') or s.endswith('.haml'))]
            filteredprecisionTemp = len(intersection(Taiti,filteredChanged))/len(Taiti)
            filteredrecallTemp = len(intersection(Taiti,filteredChanged))/len(filteredChanged)
            if (4* filteredprecisionTemp + filteredrecallTemp == 0):
             filteredf2Temp = 0
            else: filteredf2Temp = (5*filteredprecisionTemp*filteredrecallTemp)/ (4* filteredprecisionTemp + filteredrecallTemp)


            prodchangedfiles.append(filteredChanged)
            testIwithFilteredDeps.append(Taiti)
            filtereddeps.append('')
            changedprecision.append(filteredprecisionTemp)
            changedrecall.append(filteredrecallTemp)
            changedf2.append(filteredf2Temp)
            changedprecisiondeps.append(filteredprecisionTemp)
            changedrecalldeps.append(filteredrecallTemp)
            changedf2deps.append(filteredf2Temp)


            index = index+1
            print(filename)
            continue

    if filename.endswith('.csv') and not filename.startswith("http"):

        df1 = pd.read_csv(filename, engine="python", sep=',')

        weaklogicaldependence=df1['coupled'].tolist()

        stronglogicaldependence=df1['entity'].tolist()

        compare = list(zip(stronglogicaldependence,  weaklogicaldependence))


        Taiti= df.at[index,'TestI'][1:-1].split(",")
        Taiti= [x.strip(' ') for x in Taiti]
        Changed= df.at[index,'Changed files'][1:-1].split(",")
        Changed = [x.strip(' ') for x in Changed]

        Final = Matchmaker(compare,Taiti)

        testIwithDepstemp = Union(Final, Taiti)

        depstemp = [x for x in testIwithDepstemp if x not in Taiti]
        if depstemp == []:
            depstemp = ""

        precisionTemp = len(intersection(Taiti,Changed))/len(Taiti)


        recallTemp = len(intersection(Taiti,Changed))/len(Changed)

        precisiondepsTemp = len(intersection(testIwithDepstemp,Changed))/ len(testIwithDepstemp)


        recalldepsTemp = len(intersection(testIwithDepstemp,Changed))/ len(Changed)



        if (4* precisionTemp + recallTemp == 0):
            f2Temp = 0
        else: f2Temp = (5*precisionTemp*recallTemp)/ (4* precisionTemp + recallTemp)

        if (4* precisiondepsTemp + recalldepsTemp == 0):
            f2depsTemp = 0
        else: f2depsTemp = (5*precisiondepsTemp*recalldepsTemp)/ (4* precisiondepsTemp + recalldepsTemp)

        testIwithDeps.append(testIwithDepstemp)
        deps.append(depstemp)
        precision.append(precisionTemp)
        recall.append(recallTemp)
        precisiondeps.append(precisiondepsTemp)
        recalldeps.append(recalldepsTemp)
        f2.append(f2Temp)
        f2deps.append(f2depsTemp)

# Métricas com filtradas de acordo com a pasta e com a extensão

        filteredChanged =  [s for s in Changed if (s.startswith('app') or s.startswith('lib')) and (s.endswith('.erb') or s.endswith('.rb') or s.endswith('.html') or s.endswith('.haml'))]
        mask = df.coupled.str.contains(r"^(app|lib).*(\.erb|\.rb|\.html|\.haml)$")
        compare_ = df1[mask]
        weaklogicaldependencetemp=df1['coupled'].tolist()
        stronglogicaldependencetemp=df1['entity'].tolist()

        filteredcompare = list(zip(stronglogicaldependencetemp,  weaklogicaldependencetemp))

        filteredFinal = Matchmaker(filteredcompare,Taiti)

        filteredtestIwithDepstemp = Union(filteredFinal, Taiti)

        filtereddepstemp = [x for x in filteredtestIwithDepstemp if x not in Taiti]
        if filtereddepstemp == []:
            filtereddepstemp = ""

        filteredprecisionTemp = len(intersection(Taiti, filteredChanged))/len(Taiti)


        filteredrecallTemp = len(intersection(Taiti, filteredChanged))/len( filteredChanged)

        filteredprecisiondepsTemp = len(intersection(filteredtestIwithDepstemp, filteredChanged))/ len(filteredtestIwithDepstemp)


        filteredrecalldepsTemp = len(intersection(filteredtestIwithDepstemp, filteredChanged))/ len( filteredChanged)



        if (4* filteredprecisionTemp + filteredrecallTemp == 0):
            filteredf2Temp = 0
        else: filteredf2Temp = (5*filteredprecisionTemp*filteredrecallTemp)/ (4* filteredprecisionTemp + filteredrecallTemp)

        if (4* filteredprecisiondepsTemp + filteredrecalldepsTemp == 0):
            filteredf2depsTemp = 0
        else: filteredf2depsTemp = (5*filteredprecisiondepsTemp*filteredrecalldepsTemp)/ (4* filteredprecisiondepsTemp + filteredrecalldepsTemp)

        prodchangedfiles.append(filteredChanged)
        testIwithFilteredDeps.append(filteredtestIwithDepstemp)
        filtereddeps.append(filtereddepstemp)
        changedprecision.append(filteredprecisionTemp)
        changedrecall.append(filteredrecallTemp)
        changedf2.append(filteredf2Temp)
        changedprecisiondeps.append(filteredprecisiondepsTemp)
        changedrecalldeps.append(filteredrecalldepsTemp)
        changedf2deps.append(filteredf2depsTemp)






        print(filename)
        index = index+1

df['TestIWithDeps'] = testIwithDeps
df['IsolatedDeps'] = deps
df['Precision'] = precision
df['Recall'] = recall
df['F2'] = f2
df['PrecisionDeps'] = precisiondeps
df['RecallDeps'] = recalldeps
df['F2Deps'] = f2deps
df['ProductionChangedFiles'] = prodchangedfiles
df['TestIwithFilteredDeps'] = testIwithFilteredDeps
df['FilteredDeps'] = filtereddeps
df['ChangedPrecision'] = changedprecision
df['ChangedRecall'] = changedrecall
df['Changedf2'] = changedf2
df['ChangedPrecisionDeps'] = changedprecisiondeps
df['ChangedRecallDeps'] = changedrecalldeps
df['Changedf2Deps'] = changedf2deps







df.to_csv('TaitiWithdeps_sharetribe.csv', index=False)




