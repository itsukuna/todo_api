#!/bin/bash

for folder in models routes utils
do 
    mkdir -p app/$folder/
    touch app/$folder/__init__.py
done
touch app/__init__.py
