import numpy as np
import matplotlib.pyplot as plt

global N
global x
global y
def menuutama():
    print("=================================================================================================")
    print("MENU UTAMA > 4. Metode Interpolasi Polinom Newton  ")
    print("-------------------------------------------------------------------------------------------------")
    print("Bentuk Persamaan :")
    print("1. Input soal secara manual.")
    print("2. Input soal dari file.")
    print("3. Hitung solusi.")
    print("4. Tulis solusi ke dalam file.")
    print("5. Simpan plot ke dalam file.")
    print("6. Kembali ke menu sebelumnya.")
    print("0. Kembali ke menu utama.")
    print("-------------------------------------------------------------------------------------------------")
    perintah=int(input("Masukkan menu untuk melanjutkan : "))
    print("=================================================================================================")
    return perintah


def perintah1():
    global N
    global x
    global y

    N= int(input("Masukkan banyak data = "))
    x= np.zeros(N)
    y= np.zeros(N)
    for i in range (0,N):
        print("Masukkan data x ke", i+1,"= ")
        x[i]=float(input())
        print("Masukkan data y ke", i + 1, "= ")
        y[i] = float(input())

def perintah2():
    global N
    global x
    global y

    namafile = input("Masukkan nama file untuk input : ")
    file = open(namafile, "r")
    with open(namafile, "r") as file1:
        isifile = file1.read().splitlines()  # readlines()
    N = int(isifile[0])
    x = np.zeros(N)
    y = np.zeros(N)
    i = N * 2 + 1
    l = 0
    for j in range(1, i, 2):
        x[l] = float(isifile[j])
        y[l] = float(isifile[j + 1])
        l = l + 1
    file.close()

def perintah3():
    global N
    global x
    global y
    global x_soal
    global y_jawab
    global x_plot
    global y_plot

    n_polinom = N-1
    n_polinom = n_polinom + 1
    ST = [[0 for j in range(n_polinom)]for i in range(N)]
    for i in range (N):
        ST[i][0]=y[i]
    for j in range (1,n_polinom):
        for i in range(N-j):
            ST[i][j] = (ST[i+1][j-1] - ST[i][j-1])/(x[i+j]-x[i])
    x_soal = float(input("Masukkan x yang diestimasi= "))
    jumlah = ST[0][0]
    for i in range(1,n_polinom):
        suku=ST[0][i]
        for j in range(i):
            suku = suku*(x_soal-x[j])
        jumlah=jumlah+suku
    y_jawab = jumlah
    print("Nilai Estimasi :",y_jawab)
    N = int((max(x)-min(x))*100)
    x_min = min(x)-10
    x_max = max(x)+10
    y_min = min(y)-10
    y_max = max(y)+10
    x_plot = [0 for i in range(N)]
    y_plot = [0 for i in range(N)]
    for ii in range (N):
        x_plot[ii] = ((x_max-x_min) / N) * ii + x_min
        jumlah = ST[0][0]
        for i in range(1, n_polinom):
            suku = ST[0][i]
            for j in range(i):
                suku = suku * (x_plot[ii] - x[j])
            jumlah = jumlah + suku
        y_plot[ii] = jumlah
    fig, ax = plt.subplots()
    ax.plot(x,y, 'ro', label='data')
    ax.plot(x_soal, y_jawab, 'bs', label='titik yang diestimasi')
    ax.plot(x_plot, y_plot, "g", label='garis interpolasi derajat 4')
    legend = ax.legend()
    plt.xlabel("x")
    plt.ylabel("f(x) = y")
    plt.axis([x_min,x_max,y_min,y_max])
    plt.show()

def perintah4():
    global y_jawab
    N = str(y_jawab)
    namafile = input("Tulis nama file : ")
    file = open(namafile, "w+")
    file.write(N)
    file.close()
    print("Beres Bos")

def perintah5():
    global N
    global x
    global y
    global x_soal
    global y_jawab
    global x_plot
    global y_plot
    fig, ax = plt.subplots()
    ax.plot(x,y, 'ro', label='data')
    ax.plot(x_soal, y_jawab, 'bs', label='titik yang diestimasi')
    ax.plot(x_plot, y_plot, "g", label='garis interpolasi derajat 4')
    legend = ax.legend()
    plt.xlabel("x")
    plt.ylabel("f(x) = y")
    namafile = input("Tulis nama file : ")
    plt.savefig(namafile)
    print("Beres Bos")

def callback():
    perintah = 0
    while type(perintah) is int:
        perintah = int(menuutama())
        if perintah == 1:
            perintah1()
        elif perintah == 2:
            perintah2()
        elif perintah == 3:
            perintah3()
        elif perintah == 4:
            perintah4()
        elif perintah == 5:
            perintah5()
        elif perintah == 6:
            return 0
        elif perintah == 0:
            return 0