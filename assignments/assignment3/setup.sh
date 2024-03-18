#!/usr/bin/bash
# activate env
source ./as3env/bin/activate
# install requirements
pip install --upgrade pip
pip install -r requirements.txt
# close the environment
deactivate