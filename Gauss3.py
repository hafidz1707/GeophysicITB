import numpy as np

def menuawal():
    print("=================================================================================================")
    print("MENU UTAMA > 1. Metode Gauss ")
    print("-------------------------------------------------------------------------------------------------")
    print("1. SIstem Persamaan Linear 3 Variabel ")
    print("2. SIstem Persamaan Linear 4 Variabel")
    print("3. SIstem Persamaan Linear 5 Variabel")
    print("4. Kembali ke menu sebelumnya")
    print("0. Kembali ke menu utama")
    print("-------------------------------------------------------------------------------------------------")
    pilihanmenu = int(input("Masukkan menu untuk melanjutkan : "))
    print("=================================================================================================")
    return pilihanmenu

def menuutama1():
    print("MENU UTAMA > 1. Metode Gauss > 1. SIstem Persamaan Linear 3 Variabel")
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
    print("MENU UTAMA > 1. Metode Gauss > 2. SIstem Persamaan Linear 4 Variabel")
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
    print("MENU UTAMA > 1. Metode Gauss > 3. SIstem Persamaan Linear 5 Variabel")
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

def perintah1menu1():
    global a
    global b

    print("Masukkan persamaan 1")
    A1 = int(input("Masukkan koefisien x1 : "))
    B1 = int(input("Masukkan koefisien x2 : "))
    C1 = int(input("Masukkan koefisien x3 : "))
    J1 = int(input("Masukkan konstanta 1: "))

    print("Masukkan persamaan 2")
    A2 = int(input("Masukkan koefisien x1 : "))
    B2 = int(input("Masukkan koefisien x2 : "))
    C2 = int(input("Masukkan koefisien x3 : "))
    J2 = int(input("Masukkan konstanta 2 : "))

    print("Masukkan persamaan 3")
    A3 = int(input("Masukkan koefisien x1 : "))
    B3 = int(input("Masukkan koefisien x2 : "))
    C3 = int(input("Masukkan koefisien x3 : "))
    J3 = int(input("Masukkan konstanta 3 : "))
    a = np.array([[A1, B1, C1], [A2, B2, C2], [A3, B3, C3]])
    b = np.array([J1, J2, J3])

def perintah1menu2():
    global a
    global b

    print("Masukkan persamaan 1")
    A1 = int(input("Masukkan koefisien x1 : "))
    B1 = int(input("Masukkan koefisien x2 : "))
    C1 = int(input("Masukkan koefisien x3 : "))
    D1 = int(input("Masukkan koefisien x4 : "))
    J1 = int(input("Masukkan konstanta 1: "))

    print("Masukkan persamaan 2")
    A2 = int(input("Masukkan koefisien x1 : "))
    B2 = int(input("Masukkan koefisien x2 : "))
    C2 = int(input("Masukkan koefisien x3 : "))
    D2 = int(input("Masukkan koefisien x4 : "))
    J2 = int(input("Masukkan konstanta 2 : "))

    print("Masukkan persamaan 3")
    A3 = int(input("Masukkan koefisien x1 : "))
    B3 = int(input("Masukkan koefisien x2 : "))
    C3 = int(input("Masukkan koefisien x3 : "))
    D3 = int(input("Masukkan koefisien x4 : "))
    J3 = int(input("Masukkan konstanta 3 : "))

    print("Masukkan persamaan 4")
    A4 = int(input("Masukkan koefisien x1 : "))
    B4 = int(input("Masukkan koefisien x2 : "))
    C4 = int(input("Masukkan koefisien x3 : "))
    D4 = int(input("Masukkan koefisien x4 : "))
    J4 = int(input("Masukkan konstanta 4 : "))

    a = np.array([[A1, B1, C1, D1], [A2, B2, C2, D2], [A3, B3, C3, D3], [A4, B4, C4, D4]])
    b = [J1, J2, J3, J4]

def perintah1menu3():
    global a
    global b

    print("Masukkan persamaan 1")
    A1 = int(input("Masukkan koefisien x1 : "))
    B1 = int(input("Masukkan koefisien x2 : "))
    C1 = int(input("Masukkan koefisien x3 : "))
    D1 = int(input("Masukkan koefisien x4 : "))
    E1 = int(input("Masukkan koefisien x5 : "))
    J1 = int(input("Masukkan konstanta 1: "))

    print("Masukkan persamaan 2")
    A2 = int(input("Masukkan koefisien x1 : "))
    B2 = int(input("Masukkan koefisien x2 : "))
    C2 = int(input("Masukkan koefisien x3 : "))
    D2 = int(input("Masukkan koefisien x4 : "))
    E2 = int(input("Masukkan koefisien x5 : "))
    J2 = int(input("Masukkan konstanta 2 : "))

    print("Masukkan persamaan 3")
    A3 = int(input("Masukkan koefisien x1 : "))
    B3 = int(input("Masukkan koefisien x2 : "))
    C3 = int(input("Masukkan koefisien x3 : "))
    D3 = int(input("Masukkan koefisien x4 : "))
    E3 = int(input("Masukkan koefisien x5 : "))
    J3 = int(input("Masukkan konstanta 3 : "))

    print("Masukkan persamaan 4")
    A4 = int(input("Masukkan koefisien x1 : "))
    B4 = int(input("Masukkan koefisien x2 : "))
    C4 = int(input("Masukkan koefisien x3 : "))
    D4 = int(input("Masukkan koefisien x4 : "))
    E4 = int(input("Masukkan koefisien x5 : "))
    J4 = int(input("Masukkan konstanta 4 : "))

    print("Masukkan persamaan 5")
    A5 = int(input("Masukkan koefisien x1 : "))
    B5 = int(input("Masukkan koefisien x2 : "))
    C5 = int(input("Masukkan koefisien x3 : "))
    D5 = int(input("Masukkan koefisien x4 : "))
    E5 = int(input("Masukkan koefisien x5 : "))
    J5 = int(input("Masukkan konstanta 5 : "))

    a = np.array([[A1, B1, C1, D1,E1], [A2, B2, C2, D2,E2], [A3, B3, C3, D3,E3], [A4, B4, C4, D4,E4],[A5, B5, C5, D5,E5]])
    b = [J1, J2, J3, J4, J5]

def perintah2menu1():
    global a
    global b
    global a1
    global b1
    namafile = input("Masukkan nama file untuk input : ")
    file = open(namafile, "r")
    with open(namafile, "r") as file1:
        isifile = file1.read().splitlines()  # readlines()
    l = 0
    a = np.zeros([3, 3])
    b = np.zeros(3)
    for i in range(0, 3):
        for j in range(0, 3):
            a[i][j] = float(isifile[l])
            l = l + 1
    for i in range(0, 3):
        b[i] = float(isifile[l])
        l = l + 1
    file.close()

def perintah2menu2():
    global a
    global b
    global a1
    global b1
    namafile = input("Masukkan nama file untuk input : ")
    file = open(namafile, "r")
    with open(namafile, "r") as file1:
        isifile = file1.read().splitlines()  # readlines()
    l = 0
    a = np.zeros([4, 4])
    b = np.zeros(4)
    for i in range(0, 4):
        for j in range(0, 4):
            a[i][j] = float(isifile[l])
            l = l + 1
    for i in range(0, 4):
        b[i] = float(isifile[l])
        l = l + 1
    file.close()

def perintah2menu3():
    global a
    global b
    global a1
    global b1
    namafile = input("Masukkan nama file untuk input : ")
    file = open(namafile, "r")
    with open(namafile, "r") as file1:
        isifile = file1.read().splitlines()  # readlines()
    l = 0
    a = np.zeros([5,5])
    b = np.zeros(5)
    for i in range (0, 5):
        for j in range (0,5):
            a[i][j] = float(isifile[l])
            l = l+1
    for i in range (0,5):
        b[i]= float(isifile[l])
        l = l+1

    file.close()

def perintah3menu1():
    global a
    global b
    global a1
    global b1
    global x
    global a2
    global b2
    [m, n] = a.shape
    a1 = np.zeros((m, n))
    b1 = np.zeros(m)
    for i in range(0, m):
        for j in range(0, n):
            a1[i, j] = a[i, j] * a[0, 0] * a[1, 0] * a[2, 0] / a[i, 0]
        b1[i] = b[i] * a[0, 0] * a[1, 0] * a[2, 0] / a[i, 0]
    for i in range(1, m):
        for j in range(0, n):
            a1[i, j] = a1[i, j] - a1[0, j]
        b1[i] = b1[i] - b1[0]

    a2 = np.zeros((m, n))
    b2 = np.zeros(m)
    for i in range(0, m):
        for j in range(0, n):
            a2[i, j] = a1[i, j]
        b2[i] = b1[i]

    for i in range(1, m):
        for j in range(0, n):
            a2[i, j] = a1[i, j] * a1[1, 1] * a1[2, 1] / a1[i, 1]
        b2[i] = b1[i] * a1[1, 1] * a1[2, 1] / a1[i, 1]

    for i in range(2, m):
        for j in range(0, n):
            a2[i, j] = a2[i, j] - a2[1, j]
        b2[i] = b2[i] - b2[1]

    x = np.zeros(m)
    x[2] = b2[2] / a2[2, 2]
    x[1] = [b2[1] - x[2] * a2[1, 2]] / a2[1, 1]
    x[0] = [b2[0] - x[2] * a2[0, 2] - x[1] * a2[0, 1]] / a2[0, 0]

    print("Nilai x1 , x2 , x3 adalah = ", x)

def perintah3menu2():
    global a
    global b
    global a1
    global b1
    global x
    global a2
    global b2
    global b3
    global a3

    # langkah 1
    m = 4
    n = 4
    a1 = np.zeros((m, n))
    b1 = np.zeros(m)
    for i in range(0, m):
        for j in range(0, n):
            a1[i, j] = a[i, j] * a[0, 0] * a[1, 0] * a[2, 0] * a[3, 0] / a[i, 0]
        b1[i] = b[i] * a[0, 0] * a[1, 0] * a[2, 0] * a[3, 0] / a[i, 0]
    # langkah 2
    for i in range(1, m):
        for j in range(0, n):
            a1[i, j] = a1[i, j] - a1[0, j]
        b1[i] = b1[i] - b1[0]

    # langkah 3
    a2 = np.zeros((m, n))
    b2 = np.zeros(m)
    for i in range(0, m):
        for j in range(0, n):
            a2[i, j] = a1[i, j]
        b2[i] = b1[i]
    for i in range(1, m):
        for j in range(0, n):
            a2[i, j] = a1[i, j] * a1[1, 1] * a1[2, 1] * a1[3, 1] / a1[i, 1]
        b2[i] = b1[i] * a1[1, 1] * a1[2, 1] * a1[3, 1] / a1[i, 1]
    # langkah 4
    for i in range(2, m):
        for j in range(0, n):
            a2[i, j] = a2[i, j] - a2[1, j]
        b2[i] = b2[i] - b2[1]

    # langkah 5
    a3 = np.zeros((m, n))
    b3 = np.zeros(m)
    for i in range(0, m):
        for j in range(0, n):
            a3[i, j] = a2[i, j]
        b3[i] = b2[i]
    for i in range(2, m):
        for j in range(0, n):
            a3[i, j] = a2[i, j] * a2[2, 2] * a2[3, 2] / a2[i, 2]
        b3[i] = b2[i] * a2[2, 2] * a2[3, 2] / a2[i, 2]
    # langkah 6
    for i in range(3, m):
        for j in range(0, n):
            a3[i, j] = a3[i, j] - a3[2, j]
        b3[i] = b3[i] - b3[2]

    # langkah 7
    x = np.zeros(m)
    x[3] = b3[3] / a3[3, 3]
    x[2] = [b3[2] - a3[2, 3] * x[3]] / a3[2, 2]
    x[1] = [b3[1] - a3[1, 3] * x[3] - a3[1, 2] * x[2]] / a3[1, 1]
    x[0] = [b3[0] - a3[0, 3] * x[3] - a3[0, 2] * x[2] - a3[0, 1] * x[1]] / a3[0, 0]

    print("Nilai x1 , x2 , x3, x4 adalah = ", x)

def perintah3menu3():
    global a
    global b
    global a1
    global b1
    global x
    global a2
    global b2
    global b3
    global a3
    global a4
    global b4

    # langkah 1
    m = 5
    n = 5
    a1 = np.zeros((m, n))
    b1 = np.zeros(m)
    for i in range(0, m):
        for j in range(0, n):
            a1[i, j] = a[i, j] * a[0, 0] * a[1, 0] * a[2, 0] * a[3, 0] * a[4, 0] / a[i, 0]
        b1[i] = b[i] * a[0, 0] * a[1, 0] * a[2, 0] * a[3, 0] * a[4, 0] / a[i, 0]
    # langkah 2
    for i in range(1, m):
        for j in range(0, n):
            a1[i, j] = a1[i, j] - a1[0, j]
        b1[i] = b1[i] - b1[0]

    # Langkah 3
    a2 = np.zeros((m, n))
    b2 = np.zeros(m)
    for i in range(0, m):
        for j in range(0, n):
            a2[i, j] = a1[i, j]
        b2[i] = b1[i]
    for i in range(1, m):
        for j in range(0, n):
            a2[i, j] = a1[i, j] * a1[1, 1] * a1[2, 1] * a1[3, 1] * a1[4, 1] / a1[i, 1]
        b2[i] = b1[i] * a1[1, 1] * a1[2, 1] * a1[3, 1] * a1[4, 1] / a1[i, 1]
    # langkah 4
    for i in range(2, m):
        for j in range(0, n):
            a2[i, j] = a2[i, j] - a2[1, j]
        b2[i] = b2[i] - b2[1]

    # langkah 5
    a3 = np.zeros((m, n))
    b3 = np.zeros(m)
    for i in range(0, m):
        for j in range(0, n):
            a3[i, j] = a2[i, j]
        b3[i] = b2[i]
    for i in range(2, m):
        for j in range(0, n):
            a3[i, j] = a2[i, j] * a2[2, 2] * a2[3, 2] * a2[4, 2] / a2[i, 2]
        b3[i] = b2[i] * a2[2, 2] * a2[3, 2] * a2[4, 2] / a2[i, 2]
    # langkah 6
    for i in range(3, m):
        for j in range(0, n):
            a3[i, j] = a3[i, j] - a3[2, j]
        b3[i] = b3[i] - b3[2]

    # langkah 7
    a4 = np.zeros((m, n))
    b4 = np.zeros(m)
    for i in range(0, m):
        for j in range(0, n):
            a4[i, j] = a3[i, j]
        b4[i] = b3[i]
    for i in range(3, m):
        for j in range(0, n):
            a4[i, j] = a3[i, j] * a3[3, 3] * a3[4, 3] / a3[i, 3]
        b4[i] = b3[i] * a3[3, 3] * a3[4, 3] / a3[i, 3]
    # langkah 8
    for i in range(4, m):
        for j in range(0, n):
            a4[i, j] = a4[i, j] - a4[3, j]
        b4[i] = b4[i] - b4[3]

    # langkah 9
    x = np.zeros(5)
    x[4] = b4[4] / a4[4, 4]
    x[3] = [b4[3] - a4[3, 4] * x[4]] / a4[3, 3]
    x[2] = [b4[2] - a3[2, 4] * x[4] - a3[2, 3] * x[3]] / a4[2, 2]
    x[1] = [b4[1] - a3[1, 4] * x[4] - a3[1, 3] * x[3] - a3[1, 2] * x[2]] / a4[1, 1]
    x[0] = [b4[0] - a3[0, 4] * x[4] - a3[0, 3] * x[3] - a3[0, 2] * x[2] - a3[0, 1] * x[1]] / a4[0, 0]

    print("Nilai x1 , x2 , x3, x4 adalah = ", x)

def perintah4menu1():
    global x
    x = np.zeros(3)
    x[2] = b2[2] / a2[2, 2]
    x[1] = [b2[1] - x[2] * a2[1, 2]] / a2[1, 1]
    x[0] = [b2[0] - x[2] * a2[0, 2] - x[1] * a2[0, 1]] / a2[0, 0]
    x = str(x)
    namafile = input("Tulis nama file : ")
    file = open(namafile, "w+")
    file.write(x)
    file.close()
    print("Beres Bos")

def perintah4menu2():
    global x
    global b3
    global a3

    x = np.zeros(4)
    x[3] = b3[3] / a3[3, 3]
    x[2] = [b3[2] - a3[2, 3] * x[3]] / a3[2, 2]
    x[1] = [b3[1] - a3[1, 3] * x[3] - a3[1, 2] * x[2]] / a3[1, 1]
    x[0] = [b3[0] - a3[0, 3] * x[3] - a3[0, 2] * x[2] - a3[0, 1] * x[1]] / a3[0, 0]
    x = str(x)
    namafile = input("Tulis nama file : ")
    file = open(namafile, "w+")
    file.write(x)
    file.close()
    print("Beres Bos")

def perintah4menu3():
    global x
    global b3
    global a3
    global a4
    global b4

    x = np.zeros(5)
    x[4] = b4[4] / a4[4, 4]
    x[3] = [b4[3] - a4[3, 4] * x[4]] / a4[3, 3]
    x[2] = [b4[2] - a3[2, 4] * x[4] - a3[2, 3] * x[3]] / a4[2, 2]
    x[1] = [b4[1] - a3[1, 4] * x[4] - a3[1, 3] * x[3] - a3[1, 2] * x[2]] / a4[1, 1]
    x[0] = [b4[0] - a3[0, 4] * x[4] - a3[0, 3] * x[3] - a3[0, 2] * x[2] - a3[0, 1] * x[1]] / a4[0, 0]
    x = str(x)
    namafile = input("Tulis nama file : ")
    file = open(namafile, "w+")
    file.write(x)
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
                perintah1menu3()
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