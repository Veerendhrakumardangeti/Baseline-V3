(ptbxl-venv) PS C:\Users\veer> python train_pdd.py `
>>   --data_dir C:\Users\veer\results\baseline `
>>   --difficulty C:\Users\veer\results\baseline\difficulty.npy `
>>   --model inception `
>>   --epochs 30 `
>>   --batch_size 32 `
>>   --ckpt_dir C:\Users\veer\results\pdd_mild_30ep `
>>   --easy_pct 0.3 `
>>   --medium_pct 0.85 `
>>   --gamma 0.985 `
>>   --num_workers 0
[INFO] Detected input channels: 12. Signal length: 1000
Epoch 1: using 1826 / 213 samples
[DEBUG] batch 0 — x.shape: torch.Size([32, 12, 1000]), x.dtype: torch.float32, device: cpu
Epoch 1/30  Train Loss=0.5692 Acc=0.8258  Val Loss=0.6657 Acc=0.8214
Saved best model

Epoch 2: using 1809 / 213 samples
[DEBUG] batch 0 — x.shape: torch.Size([32, 12, 1000]), x.dtype: torch.float32, device: cpu
Epoch 2/30  Train Loss=0.1884 Acc=0.9635  Val Loss=0.5950 Acc=0.8214
Epoch 3: using 1769 / 213 samples
[DEBUG] batch 0 — x.shape: torch.Size([32, 12, 1000]), x.dtype: torch.float32, device: cpu
Epoch 3/30  Train Loss=0.0539 Acc=0.9989  Val Loss=1.3511 Acc=0.7143
Epoch 4: using 1749 / 213 samples
[DEBUG] batch 0 — x.shape: torch.Size([32, 12, 1000]), x.dtype: torch.float32, device: cpu
Epoch 4/30  Train Loss=0.0267 Acc=1.0000  Val Loss=0.6797 Acc=0.8214
Epoch 5: using 1722 / 213 samples
[DEBUG] batch 0 — x.shape: torch.Size([32, 12, 1000]), x.dtype: torch.float32, device: cpu
Epoch 5/30  Train Loss=0.0110 Acc=1.0000  Val Loss=0.9197 Acc=0.7500
Epoch 6: using 1668 / 213 samples
[DEBUG] batch 0 — x.shape: torch.Size([32, 12, 1000]), x.dtype: torch.float32, device: cpu
Epoch 6/30  Train Loss=0.0082 Acc=1.0000  Val Loss=0.8505 Acc=0.7500
Epoch 7: using 1650 / 213 samples
[DEBUG] batch 0 — x.shape: torch.Size([32, 12, 1000]), x.dtype: torch.float32, device: cpu
Epoch 7/30  Train Loss=0.0063 Acc=1.0000  Val Loss=1.2136 Acc=0.7500
Epoch 8: using 1662 / 213 samples
[DEBUG] batch 0 — x.shape: torch.Size([32, 12, 1000]), x.dtype: torch.float32, device: cpu
Epoch 8/30  Train Loss=0.0038 Acc=1.0000  Val Loss=0.8596 Acc=0.7500
Epoch 9: using 1616 / 213 samples
[DEBUG] batch 0 — x.shape: torch.Size([32, 12, 1000]), x.dtype: torch.float32, device: cpu
Epoch 9/30  Train Loss=0.0029 Acc=1.0000  Val Loss=0.9041 Acc=0.7500
Epoch 10: using 1593 / 213 samples
[DEBUG] batch 0 — x.shape: torch.Size([32, 12, 1000]), x.dtype: torch.float32, device: cpu
Epoch 10/30  Train Loss=0.0023 Acc=1.0000  Val Loss=0.8843 Acc=0.7500
Epoch 11: using 1589 / 213 samples
[DEBUG] batch 0 — x.shape: torch.Size([32, 12, 1000]), x.dtype: torch.float32, device: cpu
Epoch 11/30  Train Loss=0.0022 Acc=1.0000  Val Loss=0.8689 Acc=0.7500
Epoch 12: using 1516 / 213 samples
[DEBUG] batch 0 — x.shape: torch.Size([32, 12, 1000]), x.dtype: torch.float32, device: cpu
Epoch 12/30  Train Loss=0.0019 Acc=1.0000  Val Loss=0.8466 Acc=0.7500
Epoch 13: using 1556 / 213 samples
[DEBUG] batch 0 — x.shape: torch.Size([32, 12, 1000]), x.dtype: torch.float32, device: cpu
Epoch 13/30  Train Loss=0.0017 Acc=1.0000  Val Loss=0.9075 Acc=0.7500
Epoch 14: using 1517 / 213 samples
[DEBUG] batch 0 — x.shape: torch.Size([32, 12, 1000]), x.dtype: torch.float32, device: cpu
Epoch 14/30  Train Loss=0.0014 Acc=1.0000  Val Loss=0.7900 Acc=0.7500
Epoch 15: using 349 / 213 samples
[DEBUG] batch 0 — x.shape: torch.Size([32, 12, 1000]), x.dtype: torch.float32, device: cpu
Epoch 15/30  Train Loss=0.0018 Acc=1.0000  Val Loss=0.8386 Acc=0.7500
Epoch 16: using 333 / 213 samples
[DEBUG] batch 0 — x.shape: torch.Size([32, 12, 1000]), x.dtype: torch.float32, device: cpu
Epoch 16/30  Train Loss=0.0014 Acc=1.0000  Val Loss=0.7871 Acc=0.7500
Epoch 17: using 332 / 213 samples
[DEBUG] batch 0 — x.shape: torch.Size([32, 12, 1000]), x.dtype: torch.float32, device: cpu
Epoch 17/30  Train Loss=0.0011 Acc=1.0000  Val Loss=0.7750 Acc=0.7500
Epoch 18: using 322 / 213 samples
[DEBUG] batch 0 — x.shape: torch.Size([32, 12, 1000]), x.dtype: torch.float32, device: cpu
Epoch 18/30  Train Loss=0.0011 Acc=1.0000  Val Loss=0.7918 Acc=0.8214
Epoch 19: using 314 / 213 samples
[DEBUG] batch 0 — x.shape: torch.Size([32, 12, 1000]), x.dtype: torch.float32, device: cpu
Epoch 19/30  Train Loss=0.0254 Acc=1.0000  Val Loss=1.2567 Acc=0.7500
Epoch 20: using 311 / 213 samples
[DEBUG] batch 0 — x.shape: torch.Size([32, 12, 1000]), x.dtype: torch.float32, device: cpu
Epoch 20/30  Train Loss=0.0447 Acc=0.9871  Val Loss=1.2825 Acc=0.6071
Epoch 21: using 329 / 213 samples
[DEBUG] batch 0 — x.shape: torch.Size([32, 12, 1000]), x.dtype: torch.float32, device: cpu
Epoch 21/30  Train Loss=0.0834 Acc=0.9787  Val Loss=5.8598 Acc=0.6786
Epoch 22: using 299 / 213 samples
[DEBUG] batch 0 — x.shape: torch.Size([32, 12, 1000]), x.dtype: torch.float32, device: cpu
Epoch 22/30  Train Loss=0.0901 Acc=0.9732  Val Loss=1.7405 Acc=0.6786
Epoch 23: using 289 / 213 samples
[DEBUG] batch 0 — x.shape: torch.Size([32, 12, 1000]), x.dtype: torch.float32, device: cpu
Epoch 23/30  Train Loss=0.0636 Acc=0.9896  Val Loss=1.7450 Acc=0.5000
Epoch 24: using 300 / 213 samples
[DEBUG] batch 0 — x.shape: torch.Size([32, 12, 1000]), x.dtype: torch.float32, device: cpu
Epoch 24/30  Train Loss=0.0511 Acc=0.9867  Val Loss=0.8076 Acc=0.7857
Epoch 25: using 291 / 213 samples
[DEBUG] batch 0 — x.shape: torch.Size([32, 12, 1000]), x.dtype: torch.float32, device: cpu
Epoch 25/30  Train Loss=0.1153 Acc=0.9588  Val Loss=1.1718 Acc=0.7143
Epoch 26: using 285 / 213 samples
[DEBUG] batch 0 — x.shape: torch.Size([32, 12, 1000]), x.dtype: torch.float32, device: cpu
Epoch 26/30  Train Loss=0.0906 Acc=0.9825  Val Loss=1.1190 Acc=0.7143
Epoch 27: using 276 / 213 samples
[DEBUG] batch 0 — x.shape: torch.Size([32, 12, 1000]), x.dtype: torch.float32, device: cpu
Epoch 27/30  Train Loss=0.0739 Acc=0.9928  Val Loss=0.9225 Acc=0.7143
Epoch 28: using 278 / 213 samples
[DEBUG] batch 0 — x.shape: torch.Size([32, 12, 1000]), x.dtype: torch.float32, device: cpu
Epoch 28/30  Train Loss=0.0464 Acc=0.9928  Val Loss=0.7676 Acc=0.7143
Epoch 29: using 267 / 213 samples
[DEBUG] batch 0 — x.shape: torch.Size([32, 12, 1000]), x.dtype: torch.float32, device: cpu
Epoch 29/30  Train Loss=0.0316 Acc=0.9963  Val Loss=0.7221 Acc=0.7500
Epoch 30: using 254 / 213 samples
[DEBUG] batch 0 — x.shape: torch.Size([32, 12, 1000]), x.dtype: torch.float32, device: cpu

Epoch 30/30  Train Loss=0.0149 Acc=1.0000  Val Loss=0.7951 Acc=0.6786
