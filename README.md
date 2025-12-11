***Progressive Data Dropout for ECG Classification (PTB-XL)"**

  This repository investigates Progressive Data Dropout (PDD), a difficulty-aware
  training strategy for ECG classification using the PTB-XL dataset. A strong
  Inception-SE baseline is compared with multiple PDD strategies to understand
  whether selective data exposure improves performance or reduces training cost.

**motivation:**
  - Deep learning on PTB-XL is computationally expensive.
  - PDD attempts to improve efficiency by sampling based on difficulty.
  - The project evaluates whether PDD helps without reducing generalization.

**goals:**
  - Build a strong Inception-SE baseline.
  - Compute difficulty scores for PTB-XL.
  - Integrate PDD with the training loop.
  - Compare baseline vs PDD on accuracy, macro-F1, and class behavior.
  - Evaluate scenarios where PDD helps or does not help.

**repository_structure:**
  **files:**
    - train_inception.py: "Inception-SE baseline training"
    - train_incepse_pdd.py: "Inception-SE with PDD integrated"
    - train_pdd.py: "Standalone PDD implementation"
    - evaluate_model.py: "Evaluation (accuracy, macro-F1, AUC, confusion matrix)"
    - threshold_search.py
    - aggregate_metrics.py: "Aggregates all experiment results"
    - results/: "Saved training runs, logs, CSVs"
    - README.md
  legacy:
    url: "https://github.com/Veerendhrakumardangeti/baseline-V2"
    description: "Earlier CNN-based baseline with initial PDD experiments"

model_evolution:
  baseline_v2:
    architecture: "1D-CNN"
    notes:
      - Early PDD-SRD testing
      - Limited model capacity
  baseline_v3:
    architecture: "Inception-SE (deep, expressive)"
    improvements:
      - Stronger representations
      - More stable training
      - Updated PDD logic
      - Significant performance boost
    status: "Primary model used for experiments"

commands:
  train_inception_se:
    command: >
      python train_incepse_pdd.py
        --data_dir C:\Users\dines\results\baseline
        --ckpt_dir C:\Users\dines\results\incepse_retrain_full_cpu
        --epochs 30
        --batch_size 64
        --num_workers 0
  evaluate_baseline:
    command: >
      python evaluate_model.py
        --data_dir C:\Users\dines\results\baseline
        --ckpt_dir C:\Users\dines\results\incepse_retrain_full_cpu
        --batch_size 64
  train_pdd:
    command: >
      python train_pdd.py
        --data_dir C:\Users\dines\results\baseline
        --difficulty C:\Users\dines\results\baseline\difficulty.npy
        --ckpt_dir C:\Users\dines\results\pdd_final
        --epochs 30
        --batch_size 32
        --num_workers 0
  evaluate_pdd:
    command: >
      python evaluate_model.py
        --data_dir C:\Users\dines\results\baseline
        --ckpt_dir C:\Users\dines\results\pdd_final
        --batch_size 64
  aggregate_results:
    command: "python aggregate_metrics.py"
    output: "results_summary_YYYYMMDD_HHMMSS.csv"

  best_model:
    name: "Inception-SE baseline"
    val_accuracy: 0.8571
    macro_f1: 0.72
  observations:
    - The Inception-SE baseline generalizes strongly.
    - PDD did not outperform the baseline in current configuration.
    - PDD requires improved schedules and adaptive dropout strategies.
    - Deeper architectures react more sensitively to difficulty-based sampling.

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

**outputs:**
  files_generated:
    - best_model.pth
    - val_metrics.npz
    - test_metrics.npz
    - val_confusion.csv
    - test_confusion.csv
    - val_perclass.csv
    - test_perclass.csv
  aggregated_results: "Generated via aggregate_metrics.py"

---------------------------------------------------------------
# 💾 Output Files

Each experiment produces:
   
  observation: "PDD did NOT outperform the baseline."

**workflow_summary:**
  - Preprocess PTB-XL dataset
  - Compute difficulty scores
  - Train baseline Inception-SE model
  - Evaluate baseline
  - Train PDD variants
  - Evaluate PDD
  - Aggregate and compare metrics

**output_files:**
  - best_model.pth
  - val_metrics.npz
  - test_metrics.npz
  - val_confusion.csv
  - test_confusion.csv
  - val_perclass.csv
  - test_perclass.csv
  - results_summary_*.csv

**key_observations:**
  - Inception-SE outperforms 1D-CNN by a large margin
  - Baseline model achieves high accuracy and macro-F1 without PDD
  - PDD did not outperform baseline due to:
      * Suboptimal difficulty scheduling
      * Strong baseline already saturating PTB-XL performance
      * Sensitivity of PDD in deeper architectures
      * Need for more selective sample dropout mechanisms

**conclusion:** 

  This repository provides a complete exploration of Progressive Data Dropout using a strong
  Inception-SE ECG classifier on PTB-XL. Although PDD did not outperform the baseline,
  the project demonstrates valuable insights into curriculum learning, difficulty-based sampling,
  and training efficiency in medical time-series classification.
