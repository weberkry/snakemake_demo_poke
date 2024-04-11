import numpy as np
import pandas as pd
import tensorflow as tf
import matplotlib.pyplot as plt
from PIL import Image

trained_model = tf.keras.models.load_model(snakemake.input["model"])
img = Image.open(snakemake.input["image"])

#classes
y_train = pd.read_csv(snakemake.input["classes"])
y_train = y_train.drop(columns=['Unnamed: 0'])


#prepare image
img = img.resize((50, 50))
X_new = np.asarray(img).astype(np.float32)/255.
X_new = X_new.reshape(1,50,50,3)

#predict
predict_x=trained_model.predict(X_new) 
y_new=np.argmax(predict_x,axis=1)

print('this is a %s'%(y_train.columns[y_new[0]]))
plt.imshow(X_new[0])
plt.savefig(snakemake.output["plot"])  

text_file = open(snakemake.output["result"], "w")
text_file.write(y_train.columns[y_new[0]])
text_file.close()

