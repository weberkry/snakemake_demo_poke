#!/bin/bash

# add bioconda channels
conda config --add channels defaults
conda config --add channels conda-forge
conda config --add channels bioconda
conda update conda

#source
echo ". /home/christiane/anaconda3/etc/profile.d/conda.sh" >> ~/.bashrc


# add created envs to the conda env list 
#conda config --append envs_dirs /opt/nanoDx/.snakemake/conda
