#!/bin/bash
mkdir dataset
cd dataset
git clone https://github.com/ArvindSridhar/CNN-DM-Dataset.git
mv CNN-DM-Dataset .
rm -rf CNN-DM-Dataset
cd ..