from sklearn.preprocessing import OneHotEncoder
from tensorflow.keras.utils import to_categorical
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np

#replace with snakemake input
y= pd.read_csv(snakemake.input["y"]).iloc[:, 1].to_list()
X = np.load(snakemake.input["X"])

y_cat = pd.get_dummies(y)
X_train, X_val, y_train, y_val = train_test_split(X, y_cat, test_size=0.1, random_state=42)

#replace snakemake output
np.save(snakemake.output["X_train"], X_train)
np.save(snakemake.output["X_val"],X_val)
y_train.to_csv(snakemake.output["y_train"])
y_val.to_csv(snakemake.output["y_val"])
