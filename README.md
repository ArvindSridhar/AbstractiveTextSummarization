This is an implementation of the abstractive text summarization model described in https://arxiv.org/pdf/1704.04368.pdf

Code creds go to https://github.com/abisee/pointer-generator

This is built to run with Python3 and Tensorflow 1.5.0+

## Pre-processing
Get the dataset folder from Google Drive
Name this folder `dataset` and put it inside the current directory
Also create a folder `logs` in the current directory
Each time, make sure to name your experiment uniquely (shouldn't share name with an experiment already in logs/)

## Training
Simply run the following, you can tune the experiment name:
`python3 run_summarization.py --mode=train --data_path=dataset/finished_files/chunked/train_* --vocab_path=dataset/finished_files/vocab --log_root=logs/ --exp_name=exp1`

## Hyperparameter Tuning
Hyperparameters that you can tune: `max_enc_steps`, `max_dec_steps` (both of these can be found in run_summarization.py, on lines 50 and 51). The original values were max_enc_steps = 400, max_dec_steps = 100, but this takes a while to train. Reduced them both to 10 to improve training time.

Other hyperparameters that you can tune are `num_epochs_train` and `num_epochs_eval`, found on lines 47-48 of run_summarization.py

## Evaluation
Simply run the following, experiment name must be same as training run:
`python3 run_summarization.py --mode=eval --data_path=dataset/finished_files/chunked/val_* --vocab_path=dataset/finished_files/vocab --log_root=logs/ --exp_name=exp1`
