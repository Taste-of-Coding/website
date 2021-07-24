#!/bin/bash

# install python using miniconda
conda create -n myenv5 python=3.7 -y

# conda init bash
source ~/anaconda3/etc/profile.d/conda.sh
#source /Users/user/opt/miniconda3/bin/activate

# start virtual env
conda activate myenv5

# update pip
pip3 install -U pip

# install requirements.txt
pip3 install -r requirements.txt