#!/bin/bash

NAME_ENV="scrapping_NY_Project"
VER_PY="3.8"

export PATH="$HOME/anaconda3/bin:$PATH"
conda create --name $NAME_ENV python=$VER_PY
conda activate $NAME_ENV
conda install -y pandas
conda install -y requests
conda install -y bs4
conda deactivate

echo "Done!"
