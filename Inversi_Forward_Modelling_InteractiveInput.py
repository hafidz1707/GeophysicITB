"""
Tugas Inversi - Forward Modelling : Efek Gravitasi dari Lingkaran
Nama    : Hafidz Naufal Aryan
NIM     : 12317064
Dimodifikasi dari program milik Daffa Dewantara - 12317012
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


def parameterinput():
    global panjangmax, dalammax, RhoA
    opsi = int(input("Masukkan parameter secara default atau manual? \
                    \nParameter yang diatur adalah Panjang Lintasan(default 30), Kedalaman(default 6), dan Density(default 3000) \
                    \n(Default = 1, Manual = 2) : "))
    if opsi == 1:
        panjangmax = 30  # dari x = 0 sampai x = 30 (meter)
        dalammax = 6  # kedalaman maksimal 6 (meter)
        RhoA = 3000  # Nilai densitas anomali (kg/m3)
    elif opsi == 2:
        panjangmax = int(input("Masukkan panjang bentangan arah X (meter): "))
        dalammax = int(input("Masukkan kedalaman maksimal dari model (meter) : "))
        RhoA = float(input("Masukkan nilai densitas anomaly (kg/m3) : "))
    else:
        (print("Wrong Command"))
        parameterinput()

# First Step Run
parameterinput()
# Parameter Model posisi 0
panjangmin = 0
dalammin = 0
r = 0.5 # Jari-jari anomali lingkaran, jangan diganti karena akan merusak gambar model
# Parameter jumlah digitasi Y model yang akan di plot
xplot = np.arange(panjangmin, panjangmax, 0.01) # Resolusi = 0.01 meter

# Menentukan Titik Anomali Berbentuk Lingkaran dengan Jari-jari r (Bisa diinputkan, to be continued)
def anomaliinput():
    global Sphere
    opsi = int(input("Masukkan posisi anomali manual atau default? (Default = 1, Manual = 2) : "))
    if opsi == 1:
        # Format (Posisi X, Posisi Z)
        Sphere = [
            (4, -3),
            (5, -3),
            (6, -3),
            (15, -3),
            (16, -3),
            (3, -4),
            (4, -4),
            (5, -4),
            (6, -4),
            (15, -4),
            (16, -4),
            (7, -4),
            (4, -5),
            (5, -5),
            (6, -5),]
    elif opsi == 2:
        opsi2 = str(input("Peringatan! File harus bernama input.txt dengan format kolom pertama adalah x dan kolom kedua adalah z! Lanjut?(Y/N) : "))
        if opsi2 is 'Y':
            Sphere = np.loadtxt('input.txt', delimiter="\t")
        else:
            anomaliinput()
    else:
        anomaliinput()

# Second Step Run
anomaliinput()

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

# Membuat Plot
fig, ax = plt.subplots(2, figsize=(panjangmax,dalammax+1))

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
plt.suptitle("Gravity Anomaly")
plt.show()