"""
Tugas Inversi - Forward Modelling & Inverse Modelling : Efek Gravitasi dari Lingkaran
Nama    : Hafidz Naufal Aryan
NIM     : 12317064
"""

# Import Library yang dibutuhkan
import numpy as np
import matplotlib.pyplot as plt

# Kalkulasi nilai Anomali
# Gz = 4/3 * pi * G * r^3 * deltaRho * (z / (x^2 + z^2)^3/2)
def Gravy (RhoA, r, z, x):
    G = 6.67e-11
    Rho0 = 0 # densitas background diabaikan
    return (4/3) * np.pi * G * (r**3) * (RhoA - Rho0) * 100000 * z / ((x**2 + z**2)**1.5)

# Parameter Model
panjangmin = 0
dalammin = 0
panjangmax = 30  # dari x = 0 sampai x = 30 (meter)
dalammax = 6  # kedalaman maksimal 6 (meter)
RhoA = 3000  # Nilai densitas anomali (kg/m3)
r = 0.5 # Jari-jari anomali lingkaran, jangan diganti karena akan merusak gambar model
# Parameter jumlah digitasi Y model yang akan di plot
xplot = np.arange(panjangmin, panjangmax, 0.1) # Resolusi = 0.1 meter

# Menentukan Titik Anomali Berbentuk Lingkaran dengan Jari-jari r
Sphere = [
    (3, -2),
    (4, -2),
    (5, -2),
    (6, -2),
    (3, -3),
    (4, -3),
    (5, -3),
    (6, -3),
    (3, -4),
    (4, -4),
    (5, -4),
    (6, -4),
    (22, -1),
    (22, -2),
    (22, -3),
    (22, -4),
    (22, -5),
    (17, -1),
    (16, -2),
    (15, -3),
    (14, -4),
    (13, -5),
    (28, -4),
    (29, -4),
    (28, -5),
    (29, -5)]

# Membuat array untuk nilai Gz sepanjang nilai xplot dengan nilai 0
Gz = np.linspace(0, 0, len(xplot))
i = 0
for data in xplot:
    # Mencari nilai G di setiap titik posisi sepanjang xplot
    Gpoint = 0 # Definisi ulang nilai G untuk digunakan di titik posisi selanjutnya
    for cell in Sphere:
        Gpoint = Gpoint + Gravy(RhoA, r, abs(cell[1]), abs(xplot[i] - cell[0])) # Nilai G yang disebabkan oleh satu lingkaran
    Gz[i] = Gpoint # Total Nilai G yang disebabkan oleh semua lingkaran di titik posisi sepanjang xplot
    i = i+1

# Membuat Figur untuk plot
fig, ax = plt.subplots(3, figsize=(11,8), constrained_layout=True)

# Membuat lingkaran background
for i in range (panjangmax+1):
    for j in range (dalammax+1):
        c = plt.Circle((i,j), r, color='b', fill=False)
        ax[1].add_artist(c)
# Membuat lingkaran anomali
for cell in Sphere:
    c = plt.Circle((cell[0],-cell[1]), r, color='r')
    ax[1].add_artist(c)

# Plot Data dan Parameter Grafik
ax[0].plot(xplot, Gz)
ax[0].set_xlim(panjangmin, panjangmax)
ax[1].set_ylim(dalammax, dalammin)
ax[1].set_xlim(panjangmin, panjangmax)
ax[0].set_xlabel('Posisi (meter)')
ax[0].set_ylabel('Gz (mGal)')
ax[1].set_xlabel('Posisi (meter)')
ax[1].set_ylabel('Kedalaman (meter)')
ax[0].set_title("Gravity Anomaly")
ax[1].set_title("Model Sebenarnya, Rho = 3000kg/m3")

# Inverse Modelling
# Input data = Gz
# Data yang ingin dicari = Rho
# Gz = M . Rho
# Mt . Gz = Mt . M . Rho
# (Mt.M)-1 . Mt . Gz = Rho

# M = F(h,r)
def MatrixInversi (x, z):
    G = 6.67e-11
    r = 0.5
    return (4/3) * np.pi * G * (r**3) * 100000 * z / ((x**2 + z**2)**1.5)
N = (panjangmax+1) * (dalammax)
Rho = np.linspace(0, 0, N)

# Membuat matrix inversi
xplot = np.arange(panjangmin, panjangmax, 0.1) # Resolusi = 0.1 meter
k = 0
Ndata = len(Gz)
M = np.zeros((len(Gz), len(Rho)))
for i in range (len(Gz)):
    posisix = 0
    posisiz = 1
    for j in range (len(Rho)):
        M[i,j] = MatrixInversi(abs(posisix-xplot[k]), posisiz)
        posisix = posisix + 1
        if posisix > panjangmax:
            posisix = 0
            posisiz = posisiz + 1
    k = k + 1

# Menentukan nilai densitas di bawah permukaan
# Gz = M . Rho
Gzt = np.transpose(Gz)
# Mt . Gz = Mt . M . Rho
Mt = np.transpose(M)
MtM = np.matmul(Mt,M)
MtGz = np.matmul(Mt,Gz)
# (Mt.M)-1 . Mt . Gz = Rho
MtMinv = np.linalg.pinv(MtM) # MtM mempunyai determinan 0, sehingga matrix singular
Rho = np.matmul(MtMinv,MtGz)

# Membuat lingkaran hasil inversi
posisix = np.linspace(0,0,N)
posisiz = np.linspace(0,0,N)
n = 0
for i in range(1,dalammax+1):
    for j in range(panjangmax+1):
        posisix[n] = j
        posisiz[n] = i
        n = n+1
plotinversi = ax[2].scatter(posisix, posisiz, c=Rho, s=r*1000)
fig.colorbar(plotinversi, ax=ax[2])

ax[2].set_ylim(dalammax, dalammin)
ax[2].set_xlim(panjangmin, panjangmax)
ax[2].set_xlabel('Posisi (meter)')
ax[2].set_ylabel('Kedalaman (meter)')
ax[2].set_title('Model Hasil Inversi')
plt.show()