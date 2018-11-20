This is an implementation of the abstractive text summarization model described in https://arxiv.org/pdf/1704.04368.pdf

Code creds go to https://github.com/abisee/pointer-generator

This is built to run with Python3 and Tensorflow 1.5.0+

## Pre-processing
Create a log folder `logs/` at the root
Get the folder that contains the dataset by running `get_dataset.sh`

## Training
Simply run the following, you can tune the experiment name
`python3 run_summarization.py --mode=train --data_path=make_dataset/finished_files/chunked/train_* --vocab_path=make_dataset/finished_files/vocab --log_root=logs/ --exp_name=training1`

## Evaluation
Simply run the following, experiment name must be same as training run
`python3 run_summarization.py --mode=eval --data_path=make_dataset/finished_files/chunked/val_* --vocab_path=make_dataset/finished_files/vocab --log_root=logs/ --exp_name=training1`
