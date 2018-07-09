#!/bin/bash

#update repository(optional)

#yum -y update

#git install
yum install git

#install pyenv

curl -L https://raw.githubusercontent.com/yyuu/pyenv-installer/master/bin/pyenv-installer | bash


#configure environment

printf "export PATH=\"$HOME/.pyenv/bin:$PATH\"\n" >> ~/.bashrc
printf "eval \"$(pyenv init -)\"\n" >> ~/.bashrc
printf "eval \"$(pyenv virtualenv-init -)\"\n" >> ~/.bashrc

source ~/.bashrc


#install dependeces

yum -y install zlib-devel bzip2 bzip2-devel readline-devel sqlite sqlite-devel mysql-devel 

#install python and virtual environment


pyenv install 2.7
pyenv local 2.7
pip install --upgrade pip
pyenv virtualenv python270

pyenv install 3.5.0
pyenv local 3.5.0
pip install --upgrade pip
pyenv virtualenv python350
