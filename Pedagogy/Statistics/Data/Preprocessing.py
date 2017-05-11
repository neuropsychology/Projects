import pandas as pd
import os

files = []
for file in os.listdir("./Raw/"):
    file = pd.read_excel("./Raw/" + file)
    file = file.drop("Teacher", axis=1)
    files.append(file)

df = pd.concat(files)
df.to_csv("../df.csv", index=False)
