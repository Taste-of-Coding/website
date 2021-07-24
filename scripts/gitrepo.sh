#!/bin/bash

# run settings.sh
. ./settings.sh --source-only

# configure git account
git config --global user.name $git_username
git config --global user.email $git_email

# download git repo to current directory
git clone https://github.com/cctong-castiel/taste_of_python_class.git

# cd taste_of_python_class directory and remove .git
cd taste_of_python_class && rm -rf .git

# git init
git init 

# git add
git add .

# git commit
git commit -m "first commit"

# create project
heroku create

# push to heroku master
git push heroku master
