import numpy as np

def menuawal():
    print("=================================================================================================")
    print("MENU UTAMA > 2. Metode Trapezoidal ")
    print("-------------------------------------------------------------------------------------------------")
    print("1. Persamaan Polinom Pangkat 2 ")
    print("2. Persamaan Polinom Pangkat 3")
    print("3. Persamaan Polinom Pangkat 4")
    print("4. Kembali ke menu sebelumnya")
    print("0. Kembali ke menu utama")
    print("-------------------------------------------------------------------------------------------------")
    pilihanmenu = int(input("Masukkan menu untuk melanjutkan : "))
    print("=================================================================================================")
    return pilihanmenu

def menuutama1():
    print("MENU UTAMA > 2. Metode Trapezoidal > 1. Persamaan polinom pangkat 2")
    print("Bentuk Persamaan :")
    print("1. Input soal secara manual.")
    print("2. Input soal dari file.")
    print("3. Hitung solusi.")
    print("4. Tulis solusi ke dalam file.")
    print("5. Kembali ke menu sebelumnya.")
    print("0. Kembali ke menu utama.")
    print("-------------------------------------------------------------------------------------------------")
    perintah = int(input("Masukkan menu untuk melanjutkan : "))
    print("=================================================================================================")
    return perintah

def menuutama2():
    print("MENU UTAMA > 2. Metode Trapezoidal > 2. Persamaan polinom pangkat 3")
    print("Bentuk Persamaan :")
    print("1. Input soal secara manual.")
    print("2. Input soal dari file.")
    print("3. Hitung solusi.")
    print("4. Tulis solusi ke dalam file.")
    print("5. Kembali ke menu sebelumnya.")
    print("0. Kembali ke menu utama.")
    print("-------------------------------------------------------------------------------------------------")
    perintah = int(input("Masukkan menu untuk melanjutkan : "))
    print("=================================================================================================")
    return perintah

def menuutama3():
    print("MENU UTAMA > 2. Metode Trapezoidal > 3. Persamaan polinom pangkat 4")
    print("Bentuk Persamaan :")
    print("1. Input soal secara manual.")
    print("2. Input soal dari file.")
    print("3. Hitung solusi.")
    print("4. Tulis solusi ke dalam file.")
    print("5. Kembali ke menu sebelumnya.")
    print("0. Kembali ke menu utama.")
    print("-------------------------------------------------------------------------------------------------")
    perintah=int(input("Masukkan menu untuk melanjutkan : "))
    print("=================================================================================================")
    return perintah

def perintah1menu1():
    global a2
    global b2
    global a
    global b
    global c
    a2 = int(input('Masukan nilai batas bawah : '))
    b2 = int(input('Masukan nilai batas atas : '))
    # f(x) = ax^3 + bx^2 + cx + d = 0
    a = float(input("Masukan koefisien x^2 : "))
    b = float(input("Masukan koefisien x : "))
    c = float(input("Masukan konstanta : "))

def perintah2menu1():
    global a2
    global b2
    global a
    global b
    global c
    namafile = input("Masukkan nama file untuk input : ")
    file = open(namafile, "r")
    with open(namafile, "r") as file1:
        isifile = file1.read().splitlines()  # readlines()
    a2 = float(isifile[0])
    b2 = float(isifile[1])
    a = float(isifile[2])
    b = float(isifile[3])
    c = float(isifile[4])
    file.close()

def perintah3menu1():
    global a2
    global b2
    global a
    global b
    global c
    def f(x, a, b, c) :
        return a*x*x + b*x + c
    N = int(input('Masukan jumlah segmen : '))
    h = (b2 - a2) / N
    jum = 0.5 * f(a2, a, b, c)
    for i in range(1, N):
        xi = a2 + h * i
        jum = jum + f(xi, a, b, c)
    jum = jum + 0.5 * f(b2, a, b, c)
    global hasil
    hasil = jum * h
    print("Hasil Penyelesaian =", hasil)

def perintah4menu1():
    global hasil
    N = str(hasil)
    namafile = input("Tulis nama file : ")
    file = open(namafile, "w+")
    file.write(N)
    file.close()
    print("Beres Bos")

def perintah1menu2():
    global a2
    global b2
    global a
    global b
    global c
    global d

    a2 = int(input('Masukan nilai batas bawah : '))
    b2 = int(input('Masukan nilai batas atas : '))
    # f(x) = ax^3 + bx^2 + cx + d = 0
    a = float(input("Masukan koefisien x^3 : "))
    b = float(input("Masukan koefisien x^2 : "))
    c = float(input("Masukan koefisien x : "))
    d = float(input("Masukan konstanta : "))

def perintah2menu2():
    global a2
    global b2
    global a
    global b
    global c
    global d

    namafile = input("Masukkan nama file untuk input : ")
    file = open(namafile, "r")
    with open(namafile, "r") as file1:
        isifile = file1.read().splitlines()  # readlines()
    a2 = float(isifile[0])
    b2 = float(isifile[1])
    a = float(isifile[2])
    b = float(isifile[3])
    c = float(isifile[4])
    d = float(isifile[5])
    file.close()

def perintah3menu2():
    global a2
    global b2
    global a
    global b
    global c
    global d

    def f(x, a, b, c, d):
        return a * x * x * x + b * x * x + c * x + d

    N = int(input('Masukan jumlah segmen : '))
    h = (b2 - a2) / N
    jum = 0.5 * f(a2, a, b, c, d)
    for i in range(1, N):
        xi = a2 + h * i
        jum = jum + f(xi, a, b, c, d)
    jum = jum + 0.5 * f(b2, a, b, c, d)
    hasil = jum * h
    print("Hasil Penyelesaian =",hasil)

def perintah4menu2():
    global hasil
    N = str(hasil)
    namafile = input("Tulis nama file : ")
    file = open(namafile, "w+")
    file.write(N)
    file.close()
    print("Beres Bos")


def perintah1menu3():
    global a2
    global b2
    global a
    global b
    global c
    global d
    global e

    a2 = int(input('Masukan nilai batas bawah : '))
    b2 = int(input('Masukan nilai batas atas : '))
    # f(x) = ax^3 + bx^2 + cx + d = 0
    a = float(input("Masukan koefisien x^4 : "))
    b = float(input("Masukan koefisien x^3 : "))
    c = float(input("Masukan koefisien x^2 : "))
    d = float(input("Masukan koefisien x : "))
    e = float(input("Masukan konstanta : "))

def perintah2menu3():
    global a2
    global b2
    global a
    global b
    global c
    global d
    global e
    namafile = input("Masukkan nama file untuk input : ")
    file = open(namafile, "r")
    with open(namafile, "r") as file1:
        isifile = file1.read().splitlines()  # readlines()
    a2 = float(isifile[0])
    b2 = float(isifile[1])
    a = float(isifile[2])
    b = float(isifile[3])
    c = float(isifile[4])
    d = float(isifile[5])
    e = float(isifile[6])
    file.close()

def perintah3menu3():
    global a2
    global b2
    global a
    global b
    global c
    global d
    global e

    def f(x, a, b, c, d, e):
        return a * x * x * x * x + b * x * x * x + c * x * x + d * x + e

    N = int(input('Masukan jumlah segmen : '))
    h = (b2 - a2) / N
    jum = 0.5 * f(a2, a, b, c, d, e)
    for i in range(1, N):
        xi = a2 + h * i
        jum = jum + f(xi, a, b, c, d, e)
    jum = jum + 0.5 * f(b2, a, b, c, d, e)
    hasil = jum * h
    print("Hasil Penyelesaian = ",hasil)
def perintah4menu3():
    global hasil
    N = str(hasil)
    namafile = input("Tulis nama file : ")
    file = open(namafile, "w+")
    file.write(N)
    file.close()
    print("Beres Bos")

def daftarperintah(pilihanmenu):
    perintah = 0
    while type(perintah) is int:
        if (pilihanmenu == 1):
            perintah = int(menuutama1())
            if perintah == 1:
                perintah1menu1()
            elif perintah == 2:
                perintah2menu1()
            elif perintah == 3:
                perintah3menu1()
            elif perintah == 4:
                perintah4menu1()
            elif perintah == 5:
                return perintah
            elif perintah == 0:
                return 0
        elif (pilihanmenu == 2):
            perintah = int(menuutama2())
            if perintah == 1:
                perintah1menu2()
            elif perintah == 2:
                perintah2menu2()
            elif perintah == 3:
                perintah3menu2()
            elif perintah == 4:
                perintah4menu2()
            elif perintah == 5:
                return perintah
            elif perintah == 0:
                return 0
        elif (pilihanmenu == 3):
            perintah = int(menuutama3())
            if perintah == 1:
                perintah1menu1()
            elif perintah == 2:
                perintah2menu3()
            elif perintah == 3:
                perintah3menu3()
            elif perintah == 4:
                perintah4menu3()
            elif perintah == 5:
                return perintah
            elif perintah == 0:
                return 0

        elif (pilihanmenu == 2):
            perintah = int(menuutama2())
            if perintah == 1:
                perintah1menu2()
            elif perintah == 5:
                return perintah

        elif (pilihanmenu == 3):
            perintah = int(menuutama3())
            if perintah == 1:
                perintah1menu3()
            elif perintah == 5:
                return perintah



def callback():
    pilihanmenu = 0
    while type(pilihanmenu) is int:
        pilihanmenu=int(menuawal())
        if pilihanmenu == 1 or pilihanmenu == 2 or pilihanmenu == 3:
            pilihanmenu = daftarperintah(pilihanmenu)
            if pilihanmenu == 0:
                return 0
        elif pilihanmenu == 4:
            return 0
        elif pilihanmenu == 0:
            return 0