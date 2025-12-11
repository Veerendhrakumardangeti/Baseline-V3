**Progressive Data Dropout for ECG Classification (PTB-XL)**


This repository explores the use of Progressive Data Dropout (PDD) to improve ECG classification performance and training efficiency on the PTB-XL dataset. The work compares a strong Inception-SE baseline model with several PDD-based training strategies to understand whether difficulty-based sample selection can improve generalization or reduce the need for full dataset exposure during training.

The project documents the full pipeline including preprocessing, baseline training, PDD integration, evaluation, and aggregated results.

1. Project Motivation

Deep learning models trained on PTB-XL often require significant compute and long training times. This project investigates whether Progressive Data Dropout, a difficulty-aware sample selection approach, can improve training efficiency without compromising model performance.

The goals of this work are:

Build a strong, reliable baseline ECG classifier.

Compute difficulty scores and integrate PDD into training.

Compare baseline vs PDD performance on PTB-XL.

Evaluate accuracy, macro-F1, and class-level behaviour.

Understand when PDD helps and when it does not.

2. Repository Structure
train_inception.py            # Strong baseline (Inception-SE architecture)
train_incepse_pdd.py          # Inception-SE + PDD training
train_pdd.py                  # Alternate PDD implementation
evaluate_model.py             # Evaluation script (accuracy, macro-F1, AUC, confusion matrix)
threshold_search.py
aggregate_metrics.py          # Aggregates results from all experiments
results/                      # Saved models, logs, CSV outputs
README.md


Legacy project (Baseline-V2) with earlier CNN-based experiments:
https://github.com/Veerendhrakumardangeti/baseline-V2

3. Model Evolution
Baseline-V2 (legacy)

Implemented a simple 1D-CNN.

Included early PDD-SRD experiments.

Demonstrated concept but limited by model capacity.

Baseline-V3 (current)

Uses a deeper, more expressive Inception-SE network.

More stable optimization and stronger representation learning.

Updated PDD logic adapted for the stronger model.

Significantly improved validation performance.

Baseline-V3 is the primary version used for the results summarised in this README.

4. Running the Code
4.1 Train the Inception-SE Baseline
python train_incepse_pdd.py ^
  --data_dir C:\Users\dines\results\baseline ^
  --ckpt_dir C:\Users\dines\results\incepse_retrain_full_cpu ^
  --epochs 30 ^
  --batch_size 64 ^
  --num_workers 0

4.2 Evaluate the Baseline Model
python evaluate_model.py ^
  --data_dir C:\Users\dines\results\baseline ^
  --ckpt_dir C:\Users\dines\results\incepse_retrain_full_cpu ^
  --batch_size 64

4.3 Train the PDD Variant
python train_pdd.py ^
  --data_dir C:\Users\dines\results\baseline ^
  --difficulty C:\Users\dines\results\baseline\difficulty.npy ^
  --ckpt_dir C:\Users\dines\results\pdd_final ^
  --epochs 30 ^
  --batch_size 32 ^
  --num_workers 0

4.4 Evaluate the PDD Model
python evaluate_model.py ^
  --data_dir C:\Users\dines\results\baseline ^
  --ckpt_dir C:\Users\dines\results\pdd_final ^
  --batch_size 64

4.5 Aggregate All Experiment Results
python aggregate_metrics.py


This produces a CSV such as:

results_summary_20251211_124257.csv

5. Results Summary

Actual results from the experiments conducted:

Model / Folder	Val Accuracy	Macro-F1
Inception-SE (full training)	0.8571	0.7208
Inception-SE (regularized variant)	0.8214	0.4042
PDD (probe 40→70%)	0.6786	0.2021
Older PDD versions (not compatible)	–	–
Legacy CNN baseline	–	–

Best-performing model:

Inception-SE baseline

Validation accuracy: 0.8571

Macro-F1: 0.72

PDD did not outperform the strong baseline in this configuration, likely because the model already fits the dataset well and the difficulty schedule requires further tuning.

6. Workflow Summary
1. Preprocess PTB-XL dataset
2. Compute difficulty scores for PDD
3. Train the baseline Inception-SE model
4. Evaluate baseline model performance
5. Train PDD models with difficulty-based sampling
6. Evaluate and compare PDD vs baseline
7. Aggregate and document all experiment results

7. Output Files

Each experiment generates:

best_model.pth                   # Trained checkpoint
val_metrics.npz
test_metrics.npz
val_confusion.csv
test_confusion.csv
val_perclass.csv
test_perclass.csv


Aggregated CSV from all runs is produced by:

aggregate_metrics.py

8. Key Observations

Switching from a 1D-CNN to Inception-SE led to a major improvement in performance.

The strong baseline model achieved high accuracy and macro-F1 without PDD.

PDD with the current settings did not outperform the baseline, indicating the need for:

Better scheduling,

More selective dropout,

Or training-time reduction objectives.

Difficulty-aware training is more sensitive when applied to deeper architectures.
