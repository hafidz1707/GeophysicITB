import numpy as np
import matplotlib.pyplot as plt

global z
global x
global y

def menuutama():
    print("=================================================================================================")
    print("MENU UTAMA > 3. Metode Regresi Kuadrat Terkecil ")
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
    global z
    global x
    global y
    z = int(input("Masukkan banyak data = "))
    x = np.zeros(z)
    y = np.zeros(z)

    for i in range(0, z):
        print("Masukkan data x ke", i + 1, "= ")
        x[i] = float(input())
        print("Masukkan data y ke", i + 1, "= ")
        y[i] = float(input())

def perintah2():
    global z
    global x
    global y
    namafile = input("Masukkan nama file untuk input : ")
    file = open(namafile, "r")
    with open(namafile, "r") as file1:
        isifile = file1.read().splitlines()# readlines()
    z = int(isifile[0])
    x = np.zeros(z)
    y = np.zeros(z)
    i = z*2 + 1
    l = 0
    for j in range(1, i, 2):
        x[l] = float(isifile[j])
        y[l] = float(isifile[j+1])
        l = l+1
    file.close()

def perintah3():
    global z
    global x
    global y
    global x_soal
    global y_jawab
    global x_plot
    global y_plot
    n = x.size
    x_total = 0
    y_total = 0
    x_sq_total = 0
    xy_total = 0
    for i in range(n):
        x_total = x_total + x[i]
        y_total = y_total + y[i]
        x_sq_total = x_sq_total + x[i] * x[i]
        xy_total = xy_total + x[i] * y[i]
    b = (n * xy_total - x_total * y_total) / (n * x_sq_total - (x_total) * x_total)
    a = y_total / n - b * x_total / n
    print("a = ", a)
    print("b = ", b)
    x_soal = float(input("Masukkan nilai x yang ingin diestimasi: "))
    global y_jawab
    y_jawab = f(a, b, x_soal)
    print("Nilai perkiraan y untuk x = ", x_soal, " adalah : ", y_jawab)
    N = int((max(x) - min(x)) * 100)
    x_plot = [0 for i in range(N)]
    y_plot = [0 for i in range(N)]
    for i in range(0, N):
        x_plot[i] = ((max(x) + 2) / N) * i
        y_plot[i] = f(a, b, x_plot[i])

    fig, ax = plt.subplots()
    ax.plot(x, y, 'bs', label='data')
    ax.plot(x_soal, y_jawab, 'ro', label='titik yang diestimasi')
    ax.plot(x_plot, y_plot, 'g', label='garis regresi')
    legend = ax.legend()
    plt.xlabel("x")
    plt.ylabel("f(x) = y")
    plt.show()

def perintah4():
    global y_jawab
    z = str(y_jawab)
    namafile = input("Tulis nama file : ")
    file = open(namafile,"w+")
    file.write(z)
    file.close()
    print("Beres Bos")

def perintah5():
    global x_soal
    global y_jawab
    global x_plot
    global y_plot
    fig, ax = plt.subplots()
    ax.plot(x, y, 'bs', label='data')
    ax.plot(x_soal, y_jawab, 'ro', label='titik yang diestimasi')
    ax.plot(x_plot, y_plot, 'g', label='garis regresi')
    legend = ax.legend()
    plt.xlabel("x")
    plt.ylabel("f(x) = y")
    namafile = input("Tulis nama file : ")
    plt.savefig(namafile)
    print("Beres Bos")
def f(a,b,d):
    return a + b * d

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