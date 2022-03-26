"""
Nama    : Hafidz Naufal Aryan
NIM     : 12317064
Tugas Inversi - Mencari Titik Hiposenter
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Data yang digunakan
stasiun = np.array([[2.,3.,0.,0.],[6.,12.,0.,0.],[18.,15.,0.,0.],[14.,2.,0.,0.],[12.,18.,0.,0.]]) # [x,y,z,t_datang]
Tobs = ([28.2146, 28.1623, 29.5826, 27.3579, 29.6904]) # t_datang observasi
velocity = 3 # km/s
model = np.array([12,12,8,20]) # [x,y,z,t_inisial]
t0 = model[3] # 20 second
d = np.zeros(len(stasiun))

# Membuat fungsi-fungsi perhitungan
# Tdatang = Tinisial + Tkalkulasi
def fungsiwaktutiba(T0, coor_hp, coor_st, vel):
    return (T0 + np.sqrt((coor_hp[0]-coor_st[0])**2 + (coor_hp[1]-coor_st[1])**2 + (coor_hp[2]-coor_st[2])**2)/vel)
def fungsid(Tobs, Tcalc):
    return Tobs - Tcalc
def fungsijacob(dcoor_hp, dcoor_st, coor_hp, coor_st, vel):
    return (dcoor_hp-dcoor_st) / (vel * np.sqrt((coor_hp[0]-coor_st[0])**2 + (coor_hp[1]-coor_st[1])**2 + (coor_hp[2]-coor_st[2])**2))
def fungsirms(deltatime):
    return (np.mean(deltatime**2))**0.5

# Membuat plot awal
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_xlabel('sumbu X (km)')
ax.set_ylabel('sumbu Y (km')
ax.set_zlabel('kedalaman (km)')
ax.scatter(model[0],model[1],-model[2], marker = '*', c = 'black')

# Melakukan Perhitungan Step-by-Step
error = 100
iterasi = 1
while error >= 0.01:
    # Mencari waktu tiba gelombang kalkulasi di setiap stasiun
    for i in range (len(stasiun)):
        stasiun[i,3] = float(fungsiwaktutiba(t0, model, stasiun[i], velocity))

    # Mencari Matrix Travel Time
    for i in range (len(stasiun)):
        d[i] = fungsid(Tobs[i], stasiun[i,3])

    # Mencari Error RMS
    error = fungsirms(d)
    print('Error RMS iterasi ke', iterasi, '=', error, '%')

    # Mencari matrix Jacobian
    jacob = np.ones([len(stasiun),4])
    for i in range (len(stasiun)):
        jacob[i,0] = fungsijacob(model[0], stasiun[i,0], model, stasiun[i], velocity)
        jacob[i,1] = fungsijacob(model[1], stasiun[i,1], model, stasiun[i], velocity)
        jacob[i,2] = fungsijacob(model[2], stasiun[i,2], model, stasiun[i], velocity)

    # Mencari matrix dm
    # d = J.dm
    # Jt.d = Jt.J . dm
    # [Jt.J]-1 . [Jt.d] = dm
    jt = np.transpose(jacob)
    jtj = np.matmul(jt,jacob)
    jtjinv = np.linalg.inv(jtj)
    jtd = np.matmul(jt,d)
    dm = np.matmul(jtjinv,jtd)

    model = model + dm
    t0 = model[3]
    print('posisi hiposenter iterasi ke', iterasi)
    print(model)
    iterasi = iterasi + 1
    # Plot titik hiposenter setiap iterasi
    if error >= 0.01:
        ax.scatter(model[0], model[1], -model[2], marker='*', c='y')

# Plot Stasiun dan Pusat Hiposenter
ax.scatter(model[0], model[1], -model[2], marker='*', c='r')
for i in range (len(stasiun)):
    ax.scatter(stasiun[i,0],stasiun[i,1],stasiun[i,2], marker = '^', c = 'b')
plt.show()