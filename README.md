# ECG Classification Using 1D-CNN with Progressive Data Dropout (PDD)

This project implements a **1D Convolutional Neural Network (1D-CNN)** for ECG signal classification using the **PTB-XL dataset**.  
Two training strategies are implemented:

1. **Baseline Training** – Standard supervised deep learning  
2. **Progressive Data Dropout (PDD)** – Curriculum-based training where easy samples are dropped early and gradually reintroduced

The objective is to improve **generalization**, **reduce overfitting**, and **boost minority-class performance**.

---

#  Dataset Download

Download the **PTB-XL dataset** from PhysioNet:

- Full dataset:  
  https://physionet.org/content/ptb-xl/1.0.3/

- Direct ZIP:  
  https://physionet.org/static/published-projects/ptb-xl/ptb-xl-1.0.3.zip

- Metadata CSV:  
  https://physionet.org/content/ptb-xl/1.0.3/ptbxl_database.csv

Extract into:

---

# Project Structure

project-root/
-│ train_1d_baseline.py
-│ train_local.py
-│ preprocess_local.py
-│ preprocess_quick.py
-│ compute_difficulty.py
-│ pdd_split.py
-│
-├── ptbxl_data/
-│
-├── results/
-│ ├── baseline/
-│ ├── pdd_srd_ckpt/
-│ └── reports/
-│ ├── baseline_report.txt
-│ ├── pdd_srd_gamma0.95_report.txt
-│ └── comparison/
-│ └── baseline_vs_pdd.txt

---

#  Method Overview

### **1. Preprocessing**
- Loads raw WFDB ECG files  
- Extracts diagnostic labels  
- Resamples and normalizes ECG signals  
- Creates stratified train/val/test splits

### **2. Baseline 1D-CNN**
A compact CNN trained on the full dataset **without curriculum**.

### **3. Difficulty Scoring**
Evaluates sample difficulty using model confidence (entropy-based).

Output saved at: results/baseline/difficulty.npy

### **4. Progressive Data Dropout (PDD)**
Curriculum strategy:
- Drop "easy" samples early  
- Train on "hard" informative samples  
- Reintroduce all samples in the final epochs  

---

# How to Run the Pipeline

## **1. Install Dependencies**
pip install numpy pandas scipy wfdb scikit-learn tqdm torch

## **2. Preprocess Dataset**
python preprocess_local.py

## **3. Compute Difficulty Scores**
python compute_difficulty.py

## **4. Train with PDD**
python train_1d_baseline.py
--data_dir ./results/baseline
--epochs 30
--batch_size 32
--ckpt_dir ./results/pdd_srd_ckpt
--augment
--mode pdd_srd
--gamma 0.95

## **5. Train Baseline (Optional)**
python train_1d_baseline.py
--data_dir ./results/baseline
--epochs 30
--batch_size 32
--ckpt_dir ./results/baseline_ckpt
--augment
--mode baseline


---

# Results

## **Baseline Model Performance**

| Metric            | Score    |
|------------------|----------|
| Test Accuracy     | **0.69** |
| Best Val Accuracy | **0.82** |
| Macro F1          | **0.45** |

### Confusion Matrix (Baseline)
[[ 1 1 2 0]
[ 1 5 3 1]
[ 0 5 34 2]
[ 1 2 0 1]]

---

## **PDD-SRD Performance**

| Metric            | Score    |
|------------------|----------|
| Test Accuracy     | **0.74** |
| Best Val Accuracy | **0.85** |
| Macro F1          | **0.53** |

### Confusion Matrix (PDD-SRD)
[[ 2 1 1 0]
[ 1 6 3 0]
[ 2 2 35 2]
[ 1 1 1 1]]


---

# Baseline vs PDD — Comparison

| Feature                 | Baseline | PDD-SRD |
|-------------------------|----------|---------|
| Curriculum Learning     | No       | Yes     |
| Hard Sample Emphasis    | No       | Yes     |
| Test Accuracy           | 0.69     | **0.745** |
| Macro F1                | 0.45     | **0.53**  |
| Minority Recall         | Lower    | Improved |
| Training Stability      | Medium   | High     |

### **Conclusion**
PDD provides **better generalization**, **higher F1**, and **stronger minority-class performance** than the baseline model.

---

# Saving Results

All logs, confusion matrices, and evaluation reports are saved automatically inside:
results/

Folders include:
- `baseline/`
- `pdd_srd_ckpt/`
- `reports/`
- `comparison/`

---






