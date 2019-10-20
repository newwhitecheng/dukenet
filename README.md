# DukeNet
a mobile vision model for DSP

## model description
It's inspired by MobileNetv3. We add the following modifications for Qualcomm Hexagon DSP.
+ Remove all of the ‘fancy’ activations (e.g. Hard swish, ReLU6) which may either incompatible with hardware or induce significant accuracy drop after quantization.
+ Replace 5x5 depthwise separable convolutions with their 3x3 counterparts as they are not supported by the NNAPI.
+ Remove the final FC layer to reduce the number of parameters.
+ Scale up the model by 1.4x to fully utilize the given computation budget.


## Performance of Quantized models
| Model                     | Top-1 Accuracy (%) | Top-5 Accuracy (%) | \# Parameters | MACs     | Latency |
| ------------------------- | ------------------ | ------------------ | ------------- | -------- | ------- |
| DukeNet-1.4               | 73.00              | 91.38              | 3.96 M        | 410.33 M | 16.8ms  |
| DukeNet-1.4-quantized     | 72.56              | 91.34              | 3.96 M        | 410.33 M | 6.29ms  |
| MobileNetV3-1.0           | 75.2               | N/A                | 5.4M          | 219M     | ?       |
| MobileNetV3-1.0-quantized | N/A                | N/A                | 5.4M          | 219M     |         |
| MobileNetV2-1.4           | 75.0               | 92.5               | 6.06M         | 582M     | 21.02ms |
| MobileNetV2-1.0           | 71.8               | 90.6               |               |          | 19.98ms |
| MobileNetV2-1.0-quantized | 70.8               | 89.9               |               |          | 5.95ms  |
| MobileNetV1-1.0           | 71.0               | 89.9               |               |          | 17.15ms |
| MobileNetV1-1.0-quantized | 70.0               | 89.0               |               |          | 5.19ms  |
| MnasNet-0.75              | 71.72              | 90.17              |               |          | 26.88ms |
| MnasNet-1.0               | 74.08              | 91.75              |               |          | 27.54ms |
| MnasNet-1.3               | 75.24              | 92.55              |               |          | 27.59ms |




<p align="center">
<img src="g3doc/performance_comparison.png">
</p>

## Version
**Alpha Release v1.0 (10/21)**
+ model folder: Model1017_71.7_6.39
+ benchmark log on cpu
+ benchmark log on dsp with nnapi enabled.
+ note: meet the requirements - >71% Top-1 on ImageNet, <7ms

**v1.1**
+ coming soon

## team information
+ team name: foreverDuke
+ team member: Tunhou Zhang, Shiyu Li, Hsin-Pai Cheng

