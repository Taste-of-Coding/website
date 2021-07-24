#!/bin/bash

# install python using miniconda
conda create -n myenv python=3

# start virtual env
conda activate myenv

# update pip
pip3 install -U pip

# install requirements.txt
pip3 install -r requirements.txt

# install git 
conda install -c anaconda git

# install heroku cli
brew tap heroku/brew && brew install heroku