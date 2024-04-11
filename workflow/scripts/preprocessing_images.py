# import packages
import os
import pathlib
import pandas as pd
import numpy as np
from PIL import Image



#read files
print("reading images from:")


print(snakemake.input["train"])
path=snakemake.input["train"]
list_subfolders_with_paths = [f.path for f in os.scandir(path) if f.is_dir()]

X_list = [] #images as matrix
y = []      # pokemon class


print("adjusting image size")
for pokemon in list_subfolders_with_paths:
    from os import listdir
    from os.path import isfile, join
    onlyfiles = [f for f in listdir(pokemon) if isfile(join(pokemon, f)) and '.jpg' in f or '.jpeg'in f]    
    for img in onlyfiles:
        n = Image.open("%s/%s"%(pokemon,img))

        #drop if only 2 dim!
        if len(np.shape(n))!=3 or np.shape(n)[2] != 3:
            pass
        else:
            #keep images and add to X-list and y class
            #reshape
            n = n.resize((50, 50))
            n = np.asarray(n).astype(np.float32)/255.
            X_list.append(n)
            y.append(pokemon.split(os.sep)[-1])
        
      
print("saving train matrix and classes")
X = np.concatenate( X_list, axis=0 )
X = X.reshape(-1,50,50,3)

#save np object
np.save(snakemake.output["train_matrix"], X)
df_y = pd.DataFrame(y)
df_y.to_csv(snakemake.output["classes"])