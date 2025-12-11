project:
  title: "Progressive Data Dropout for ECG Classification (PTB-XL)"
  description: |
    This repository explores the use of Progressive Data Dropout (PDD) for improving
    training efficiency and behavior in ECG classification using the PTB-XL dataset.
    A strong Inception-SE baseline model is compared against multiple PDD training
    strategies to evaluate whether difficulty-based sample selection offers
    performance improvements or training-time benefits. The project implements the
    full pipeline: preprocessing → baseline training → PDD integration → evaluation
    → metrics aggregation.

motivation: |
  Deep learning models trained on PTB-XL require significant compute and long training cycles.
  Progressive Data Dropout (PDD) is a difficulty-aware method that selectively drops easy samples early.
  This project investigates whether PDD can improve generalization, reduce dataset dependence, and enhance efficiency.

objectives:
  - Build a strong and reliable Inception-SE ECG classifier
  - Compute difficulty scores for PTB-XL samples
  - Integrate PDD into the Inception-SE training loop
  - Compare baseline vs PDD models
  - Evaluate accuracy, macro-F1, AUC, class-level metrics
  - Identify when PDD helps and when it does not

repository_structure:
  - train_inception.py: "Inception-SE baseline"
  - train_incepse_pdd.py: "Inception-SE + PDD training"
  - train_pdd.py: "Alternate PDD implementation"
  - evaluate_model.py: "Evaluation script (Accuracy, Macro-F1, AUC, confusion matrix)"
  - threshold_search.py: "Threshold finder"
  - aggregate_metrics.py: "Aggregates results from all experiments"
  - results/: "Logs, checkpoints, metrics, CSV outputs"
  - README.md

legacy_repo:
  name: "Baseline-V2"
  url: "https://github.com/Veerendhrakumardangeti/baseline-V2"
  notes: "Contains earlier CNN-based experiments with limited capacity"

model_evolution:
  baseline_v2:
    model: "1D-CNN"
    features:
      - Simple model
      - Early PDD-SRD prototypes
      - Limited learning capacity
  baseline_v3:
    model: "Inception-SE"
    improvements:
      - Deeper and more expressive
      - Better representation learning
      - More stable optimization
      - Updated PDD logic
      - Dramatic improvement in validation metrics
    used_for_final_results: true

running_code:
  train_baseline:
    command: |
      python train_incepse_pdd.py ^
        --data_dir C:\Users\dines\results\baseline ^
        --ckpt_dir C:\Users\dines\results\incepse_retrain_full_cpu ^
        --epochs 30 ^
        --batch_size 64 ^
        --num_workers 0

  evaluate_baseline:
    command: |
      python evaluate_model.py ^
        --data_dir C:\Users\dines\results\baseline ^
        --ckpt_dir C:\Users\dines\results\incepse_retrain_full_cpu ^
        --batch_size 64

  train_pdd:
    command: |
      python train_pdd.py ^
        --data_dir C:\Users\dines\results\baseline ^
        --difficulty C:\Users\dines\results\baseline\difficulty.npy ^
        --ckpt_dir C:\Users\dines\results\pdd_final ^
        --epochs 30 ^
        --batch_size 32 ^
        --num_workers 0

  evaluate_pdd:
    command: |
      python evaluate_model.py ^
        --data_dir C:\Users\dines\results\baseline ^
        --ckpt_dir C:\Users\dines\results\pdd_final ^
        --batch_size 64

  aggregate_results:
    command: "python aggregate_metrics.py"
    output_example: "results_summary_20251211_124257.csv"

results_summary:
  
---

# 📊 Results Summary

| Model / Folder                     | Val Accuracy | Macro-F1 |
|-----------------------------------|--------------|----------|
| **Inception-SE (full training)**  | **0.8571**   | **0.7208** |
| Inception-SE (regularized)        | 0.8214       | 0.4042   |
| **PDD (probe 40 → 70%)**          | 0.6786       | 0.2021   |
| Older PDD versions                | –            | –        |
| Legacy CNN baseline               | –            | –        |

### **Best-Performing Model**
- **Inception-SE Baseline**
- Accuracy: **0.8571**  
- Macro-F1: **0.72**

### ❗ Important Observation  
**PDD did not outperform the strong Inception-SE baseline**.  
The baseline model already fits the dataset well, and PDD needs further tuning for deeper architectures.

---

# 🔄 Workflow Summary

1. Preprocess PTB-XL dataset  
2. Compute difficulty scores  
3. Train Inception-SE baseline  
4. Evaluate baseline  
5. Train PDD variants  
6. Evaluate PDD models  
7. Aggregate all experiment results  

---

# 💾 Output Files

Each experiment produces:


   
  observation: "PDD did NOT outperform the baseline."

workflow_summary:
  - Preprocess PTB-XL dataset
  - Compute difficulty scores
  - Train baseline Inception-SE model
  - Evaluate baseline
  - Train PDD variants
  - Evaluate PDD
  - Aggregate and compare metrics

output_files:
  - best_model.pth
  - val_metrics.npz
  - test_metrics.npz
  - val_confusion.csv
  - test_confusion.csv
  - val_perclass.csv
  - test_perclass.csv
  - results_summary_*.csv

key_observations:
  - Inception-SE outperforms 1D-CNN by a large margin
  - Baseline model achieves high accuracy and macro-F1 without PDD
  - PDD did not outperform baseline due to:
      * Suboptimal difficulty scheduling
      * Strong baseline already saturating PTB-XL performance
      * Sensitivity of PDD in deeper architectures
      * Need for more selective sample dropout mechanisms

conclusion: |
  This repository provides a complete exploration of Progressive Data Dropout using a strong
  Inception-SE ECG classifier on PTB-XL. Although PDD did not outperform the baseline,
  the project demonstrates valuable insights into curriculum learning, difficulty-based sampling,
  and training efficiency in medical time-series classification.
