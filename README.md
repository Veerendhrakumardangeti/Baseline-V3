📌 Progressive Data Dropout for ECG Classification (PTB-XL)

This repository explores the use of Progressive Data Dropout (PDD) to improve training efficiency and generalization in ECG classification using the PTB-XL dataset.
A strong Inception-SE baseline model is compared with multiple PDD-based training strategies to understand whether difficulty-aware sample selection can reduce training time or improve performance.

The project documents the end-to-end pipeline:
preprocessing → baseline training → PDD integration → evaluation → results aggregation.

🚀 Project Motivation

Training deep learning models on PTB-XL is computationally expensive and often requires large numbers of epochs.
Progressive Data Dropout (PDD) is a recently proposed technique that drops “easier” samples early in training, allowing the model to focus on more informative or difficult examples.

This project investigates whether PDD can:

Reduce computation

Improve generalization

Change class-level behaviour

Provide a training-efficient alternative to full dataset training

🎯 Goals of the Project

Build a strong Inception-SE baseline ECG classifier

Compute difficulty scores for PTB-XL samples

Integrate PDD into the training loop

Compare Baseline vs PDD performance

Evaluate using:
✔ Accuracy
✔ Macro-F1
✔ Confusion matrices
✔ Per-class behaviour

Understand when PDD helps — and when it does not

📂 Repository Structure
train_inception.py        # Strong Inception-SE baseline
train_incepse_pdd.py      # Baseline with regularized + PDD variations
train_pdd.py              # Standalone PDD training implementation

evaluate_model.py         # Accuracy, F1, AUC, confusion matrix
threshold_search.py       
aggregate_metrics.py      # Aggregates results from all experiments

results/                  # All saved models, metrics, logs
README.md


Legacy work:
➡ https://github.com/Veerendhrakumardangeti/baseline-V2

(Earlier CNN baseline + early PDD-SRD experiments)

📈 Model Evolution
Baseline-V2 (Legacy)

Simple 1D-CNN

Early PDD-SRD prototypes

Limited model capacity → limited performance

Baseline-V3 (Current — This Repo)

Inception-SE architecture

Much stronger feature extraction

Updated PDD logic

Significantly improved validation performance

Primary version used for all final results

🔧 Running the Code
1️⃣ Train the Inception-SE Baseline
python train_incepse_pdd.py ^
  --data_dir C:\Users\dines\results\baseline ^
  --ckpt_dir C:\Users\dines\results\incepse_retrain_full_cpu ^
  --epochs 30 ^
  --batch_size 64 ^
  --num_workers 0

2️⃣ Evaluate the Baseline
python evaluate_model.py ^
  --data_dir C:\Users\dines\results\baseline ^
  --ckpt_dir C:\Users\dines\results\incepse_retrain_full_cpu ^
  --batch_size 64

3️⃣ Train PDD Variant
python train_pdd.py ^
  --data_dir C:\Users\dines\results\baseline ^
  --difficulty C:\Users\dines\results\baseline\difficulty.npy ^
  --ckpt_dir C:\Users\dines\results\pdd_final ^
  --epochs 30 ^
  --batch_size 32 ^
  --num_workers 0

4️⃣ Evaluate PDD Model
python evaluate_model.py ^
  --data_dir C:\Users\dines\results\baseline ^
  --ckpt_dir C:\Users\dines\results\pdd_final ^
  --batch_size 64

5️⃣ Aggregate All Experiment Results
python aggregate_metrics.py


This generates a CSV such as:

results_summary_20251211_124257.csv

📊 Results Summary
Model / Folder	Val Accuracy	Macro-F1
Inception-SE (Full Training)	0.8571	0.7208
Inception-SE (Regularized Variant)	0.8214	0.4042
PDD (40→70% schedule)	0.6786	0.2021
Older PDD versions (incompatible)	–	–
Legacy CNN baseline	–	–
Best Model: Inception-SE Baseline

✔ Validation Accuracy: 0.8571

✔ Macro-F1: 0.72

Key Finding

PDD did not outperform the strong baseline in its current configuration.
Reasons likely include:

Need for better PDD schedules

Deeper models may require different difficulty distributions

PDD may be more beneficial when aiming specifically to reduce training cost

🔄 Workflow Summary

Preprocess PTB-XL dataset

Compute difficulty scores

Train Inception-SE baseline

Evaluate baseline

Train PDD variants

Evaluate PDD

Aggregate results

Document findings

📁 Output Files

Each experiment produces:

best_model.pth
val_metrics.npz
test_metrics.npz
val_confusion.csv
test_confusion.csv
val_perclass.csv
test_perclass.csv


Final aggregated output:

results_summary_*.csv

📝 Key Observations

Switching to Inception-SE greatly improved performance vs earlier CNNs.

Baseline-V3 already fits PTB-XL well → less room for PDD to help.

Current PDD implementation may need:

Dynamic scheduling

Stronger difficulty scoring

Explicit compute-reduction objectives
