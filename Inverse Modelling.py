# Tugas Inverse Modelling Sederhana Metode Gravitasi
# Berith Atmaodi
# 12317034
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

def plot_examples(data, colormaps):
    """
    Helper function to plot data with associated colormap.
    """
    n = len(colormaps)
    fig, axs = plt.subplots(1, n, figsize=(data.shape[1], data.shape[0]),squeeze=False)
    for [ax, cmap] in zip(axs.flat, colormaps):
        psm = ax.pcolormesh(data, cmap=cmap, rasterized=True)
        fig.colorbar(psm, ax=ax)
    plt.gca().invert_yaxis()
    plt.suptitle('Inverse Modelling Data Gravitasi', fontsize = 20)
    plt.xlabel('X (meter)', fontsize=14)
    plt.ylabel('Y (meter)', fontsize=14)
    plt.savefig("Inverse Modelling.png")
    plt.show()

d = []
file = open('Forward Modelling.txt','r')
f = file.readlines()[1:]
xmin = int(f[0].split("\t|\t")[0])
xmax = int(f[-1].split("\t|\t")[0])
for i in range (len(f)):
    d.append(f[i].split("\n")[0])
    d[i] = float(d[i].split("\t|\t")[1])
d = np.vstack(d)
file.close()

depth = int(input("Input kedalaman = "))
model = np.zeros([depth+1,xmax - xmin+1])

G = np.zeros([model.shape[1], model.shape[0]*model.shape[1]])
filee = open('G.txt', 'w+')
for k in range (G.shape[0]):
    c = 0
    for i in range (1, depth+1):
        for j in range (xmax - xmin+1):
            G[k][c+xmax - xmin+1] = 4/3*np.pi*6.67*(10**-11)*(1**3)*i/((i**2 + (j-k)**2)**(3/2))
            c = c+1

for i in range (G.shape[0]):
    for j in range (G.shape[1]):
        filee.write(str(G[i][j]))
        filee.write('\t')
    filee.write('\n')
filee.close()

GT = np.transpose(G)
GGT = np.matmul(G,GT)
GGTi = np.linalg.inv(GGT)
GTGGTi = np.matmul(GT,GGTi)
m = np.matmul(GTGGTi,d)

filez = open('Inverse Model.txt', 'w+')
c = 0
for i in range(depth+1):
    for j in range(xmax - xmin + 1):
        model[i][j] = m[c]
        filez.write(str(model[i][j]))
        filez.write('\t')
        c = c+1
    filez.write('\n')
filez.close()

viridis = cm.get_cmap('viridis', 256)
plot_examples(model, [viridis])