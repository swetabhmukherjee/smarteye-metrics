#!/bin/bash
#
# Created By: Swetabh
# Bash script to install and generate pip requirements.txt from inside a virtualenv.

# START

echo "---------------------------------------------------------------------" 
echo "Starting the script........" 

sudo apt-get upgrade
sudo apt upgrade
sudo apt-get update
sudo apt update
sudo apt install docker.io
#install pip based on os(macOS or linux)
if sudo apt install python3-pip; then
    sudo apt install python3-pip
else
    brew install python
fi

if sudo apt-get -y install python3-pip; then
    sudo apt-get -y install python3-pip
else
    brew install python
fi

if sudo apt-get install python-pip; then
    sudo apt-get install python-pip
else
    brew install python
fi

pip install --upgrade pip
pip3 install --upgrade setuptools pip

sudo apt-get install python-skimage

sudo pip3 install virtualenv
sudo apt install virtualenv
virtualenv api
source ./api/bin/activate

echo "Starting to install packages......." 
echo "---------------------------------------------------------------------" 
echo "Enter the path of requirements.txt file"
read requirements_path
echo "---------------------------------------------------------------------" 
echo "Requested packages are :"
while read line; do echo $line; done < $requirements_path
echo "---------------------------------------------------------------------" 


echo "Starting to install packages......." 
   #check virtualenv path 
if [[ "$VIRTUAL_ENV" != "" ]]; then 
    echo "You are in a working virtualenv $VIRTUAL_ENV";
   # virtual_env > check if packages is empty .. if [[ ]]; then
    # if [[ "$packages" != "" ]]; then
    pip3 install -r $requirements_path;
    pip3 freeze > "additional_requirements.txt"
echo "---------------------------------------------------------------------"
echo "Installing additional requirements......."
echo "---------------------------------------------------------------------"

    pip3 install -r additional_requirements.txt
    
else 
    echo "You are not in a working virtualenv"
    echo "Exiting .........."
    exit 1;
fi 
echo "---------------------------------------------------------------------" 
echo "Packages installed successfully" 
echo "---------------------------------------------------------------------" 

#END
