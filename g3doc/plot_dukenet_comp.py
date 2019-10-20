# DukeNet 10/21 submission
# uint8: 72.56/91.34
# float: 73.00/91.39

import numpy as np
import matplotlib.pyplot as plt
# from matplotlib import gridspec
net = ('DukeNet_1.0_224_quant', 'Mobilenet_V1_1.0_224_quant','Mobilenet_V2_1.0_224_quant')
colors=['black', 'g', 'r']
        # 'r', 'brown', 'orange', 'gold', 'slateblue', 'violet']
# gs = gridspec.GridSpec(1, 2, width_ratios=[2, 3])

scaling_size = 20

Ours_latency = (6.29)
Ours_Top1 = (72.56)
Ours_Paras = np.array((3.87))*scaling_size

MobileNet_v1_latency = (5.19)
MobileNet_v1_Top1 = (70)
MobileNet_v1_Paras = np.array((4.3))*scaling_size

MobileNet_v2_latency = (5.95)
MobileNet_v2_Top1 = (70.80)
MobileNet_v2_Paras = np.array((3.4))*scaling_size



fig = plt.figure(figsize=(5*0.9, 4*0.9))
# box = [[6, 0], [12, 4]]
# ax = plt.subplot(gs[1])

MobileNet_v1 = plt.scatter(MobileNet_v1_latency, MobileNet_v1_Top1, s=MobileNet_v1_Paras, color='r', edgecolors='gray')
MobileNet_v2 = plt.scatter(MobileNet_v2_latency, MobileNet_v2_Top1, s=MobileNet_v2_Paras, color='g', edgecolors='gray')
DukeNet = plt.scatter(Ours_latency, Ours_Top1, s=Ours_Paras, color='black', edgecolors='gray')

# grey dots
reperenceParamx = reperenceParamxTex = np.array([6, 7.5, 9])
y_ref = 65
reperenceParamy = [y_ref, y_ref, y_ref]

param_size_ref = np.array([3.5, 4.0, 4.5])
parass = param_size_ref*scaling_size

plt.scatter(reperenceParamx, reperenceParamy, s=parass, color='gray', edgecolors='black', alpha=0.3)

reperenceParamxTex = np.array([5.5, 7, 8.5])
plt.text(reperenceParamxTex[0], y_ref+1, str(param_size_ref[0])+"M", fontsize=12)
plt.text(reperenceParamxTex[1], y_ref+1, str(param_size_ref[1])+"M", fontsize=12)
plt.text(reperenceParamxTex[2], y_ref+1, str(param_size_ref[2])+"M", fontsize=12)

for i in range(3):
    plt.text(6.5, 62.7-i*1.28, net[i], fontsize=12)
    plt.scatter(6, 63-1.28*i, s=60, color=colors[i])

plt.xscale('linear')
my_x_ticks = [5, 10, 15]
plt.xticks(my_x_ticks, my_x_ticks, fontsize=12)

plt.xlim(5,15)
plt.yticks(fontsize=12)
plt.grid(True, linestyle='-.')
plt.xlabel('Latency (ms)', fontsize=12)
plt.ylabel('Top-1 accuracy, ImageNet [%]', fontsize=12)
plt.subplots_adjust(left=0.15, bottom=0.15, right=0.9, top=0.9, wspace=0.2, hspace=0)

plt.savefig("performance_comparison.png")