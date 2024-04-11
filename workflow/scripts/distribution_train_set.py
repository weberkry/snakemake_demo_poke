import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

y_train= pd.read_csv(snakemake.input["y_train"])
y_train = y_train.drop(columns=['Unnamed: 0'])

plt.figure(figsize=(25,15))
plt.bar(y_train.columns, y_train.sum())
plt.xticks(rotation=90)

plt.savefig(snakemake.output["plot"])  
