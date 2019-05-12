#!/bin/bash
#
#Script to Install linux and basic python
#
# GENERAL LINUX
apt-get update #updates the package index cache 
apt-get upgrade -y #updates packages
#install system tools
apt-get install -y bzip2 gcc git htop screen vim wget
apt-get upgrade -y bash #upgrades bash if necessary
apt-get clean #cleans up the package index cache
#Install miniconda
wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh -O Miniconda.sh
bash Miniconda.sh -b #install miniconda
rm -rf Miniconda.sh #remove installer
export PATH="/root/miniconda3/bin:$PATH" #prepends the new path
#Install Python
conda update -y conda python #updates conda and python if necessary
conda install -y pandas
conda install -y ipython
