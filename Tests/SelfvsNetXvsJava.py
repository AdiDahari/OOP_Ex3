from matplotlib import pyplot as plt
import numpy as np

labels = ['G1', 'G2', 'G3', 'G4', 'G5', 'G6']

mine_sp = [0.0009970664978027344, 0.0009968280792236328, 0.017952919006347656, 0.33910536766052246, 0.8965480327606201, 2.1417267322540283]
mine_cc = [0.0, 0.0, 0.00660252571105957, 0.08477115631103516, 0.20495820045471191, 0.40491628646850586]

nx_sp = [0.0, 0.0, 0.0, 0.0, 0.0, 0.000997781753540039]
nx_cc = [0.0, 0.0, 0.0, 0.0, 0.001027822494506836, 0.0]

java_sp = [0.002, 0.001, 0.037, 0.257, 0.537, 1.986]
java_cc = [0.0, 0.0, 0.003, 0.065, 0.134, 0.291]

x = np.arange(len(labels))
width = 0.3

fig, ax = plt.subplots()
rects1 = ax.bar(x - width, mine_cc, width, label='Python')
rects2 = ax.bar(x + width, nx_cc, width, label='NetX')
rects3 = ax.bar(x, java_cc, width, label='Java')

ax.set_ylabel("Score")
ax.set_title("Connected Components")
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()
fig.tight_layout()
plt.show()
