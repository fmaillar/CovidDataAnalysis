import numpy as np
import pandas as pd
import urllib.request
import matplotlib.pyplot as plt

# Importation du fichier
URL = "https://www.data.gouv.fr/fr/datasets/r/63352e38-d353-4b54-bfd1-f1b3ee1cabd7"
file = urllib.request.urlopen(URL)
df = pd.read_csv(file, header=0, sep=";")

# Transformation de l'index par l'id
df['jour'] = pd.to_datetime(df['jour'])
df = df.set_index('jour')

# On groupe par le sexe 0
grouped = df.groupby("sexe")
df1 = grouped.get_group(0)

# On groupe par jour
grouped2 = df1.groupby('jour')

Date = df1.index.unique()
lst = df.columns[2:8]
DataLst = []
# On crée les vecteurs en sommant sur le groupe de jour en jour (index)
for i in range(6):
    Tmp = [grouped2.get_group(t)[lst[i]].sum() for t in Date]
    DataLst.append(Tmp)

# Fenêtre glissante de 7 jours pour lisser les courbes
window = 7
# Plotting
plt.figure(figsize=(10, 3))
for i in range(5):
    #    plt.plot(Date, DataLst[i], label=lst[i])
    plt.plot(Date, pd.Series(DataLst[i]).rolling(window).mean(), label=lst[i])
plt.grid(True)
plt.legend()
