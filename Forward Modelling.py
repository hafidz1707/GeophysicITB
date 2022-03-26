#Tugas Forward Modelling Sederhana Metode Gravitasi
#Berith Atmaodi
#12317034
import numpy as np
import matplotlib.pyplot as plt

cora = []

def persegi():
    xa0 = int(input("X awal anomali = "))
    xa1 = int(input("X akhir anomali = "))
    ya0 = int(input("Batas atas anomali = "))
    ya1 = int(input("Batas bawah anomali = "))
    dg = float(input("Kontras densitas (kg/m^3) = "))
    c = str(input("Warna model = "))
    xa = np.arange(xa0, xa1 + 1, 1)
    ya = np.arange(-ya0, -ya1 - 1, -1)
    global cora
    for i in xa:
        for j in ya:
            cora.append([i, j, dg, c])
    print('---')

def manualinput():
    again = 1
    while(again == 1):
        xin = int(input("X anomali = "))
        yin = int(input("Y anomali = "))
        dg = float(input("Kontras densitas (kg/m^3) = "))
        c = str(input("Warna model = "))
        cora.append([xin,-yin, dg, c])
        again = int(input("Lanjutkan input? (Ya = 1/Tidak = 0) : "))
    print('---')

def inputfile():
    A = []
    file = open('Input FM.dat', 'r')
    f = file.readlines()[5:]
    for i in range(len(f)):
        A.append(f[i].split("\n")[0])
        A[i] = A[i].split(",")
        cora.append([int(A[i][0]), -int(A[i][1]), float(A[i][2]), str(A[i][3])])
    print('Input dari Input FM.dat sukses')
    print('---')

def carainput():
    print("Pilih cara input anomali")
    print("1. Anomali persegi")
    print("2. Anomali input manual")
    print("3. Input dari file")
    cara = int(input("Cara input = "))
    print('---')
    if (cara == 1):
        persegi()
    elif (cara == 2):
        manualinput()
    elif (cara == 3):
        inputfile()

#Main
print("Input Rentang Model")
xm0 = int(input("X awal model = "))
xm1 = int(input("X akhir model = "))
ym = int(input("Kedalaman maksimal = "))
print('---')
x = np.arange(xm0,xm1+1,1)
y = np.arange(0,-ym-1,-1)
again = 1
while (again == 1):
    carainput()
    again = int(input("Tambahkan anomali? (Ya = 1/Tidak = 0) = "))
    print('---')

#Kalkulasi Forward Modelling
G = float(-6.67 * 10**-11)
fm = []
f = open("Forward Modelling.txt","w+")
f.write("Nilai X" + '\t' + '|' + '\t' + "g Kalkulasi" + '\n')
for X in x:
    sumdgz = 0
    for i in range (len(cora)):
        dgz = (4/3*np.pi*G*cora[i][2]*(1**3)*cora[i][1])/(((X-cora[i][0])**2)+(cora[i][1]**2))**(3/2)
        sumdgz = sumdgz + dgz
    fm.append(sumdgz)
    f.write(str(X) + ' ' + '\t' + '|' + '\t' + str(sumdgz) + '\n')

#Modelling
circle = []
for i in range (len(x)):
    for j in range (len(y)):
        circle.append(plt.Circle((x[i], y[j]), 0.5, color='r', fill=False))

circlea = []
for i in range (len(cora)):
    circlea.append(plt.Circle((cora[i][0], cora[i][1]), 0.5, color=cora[i][3]))

fig, ax = plt.subplots(2)
plt.xlim(xm0-0.5,xm1+0.5)
plt.ylim(-ym-0.5,0)
plt.grid(linestyle='--')

#Plot Circle
for i in range (len(circle)):
    ax[1].add_artist(circle[i])
for i in range(len(circlea)):
    ax[1].add_artist(circlea[i])

#Plot Grafik
for i in range (len(x)):
    ax[0].plot(x[i],fm[i],'g-')

ax[0].plot(x,fm,'g-')
ax[0].set_title('Kalkulasi Forward Modelling', fontsize=14)
plt.xlabel('X (meter)', fontsize=10)
ax[0].set_ylabel('Anomali gravitasi (m/s^2)', fontsize=10)
ax[1].set_ylabel('Y (meter)', fontsize=10)
plt.savefig("Forward Modelling", bbox_inches='tight')
plt.show()