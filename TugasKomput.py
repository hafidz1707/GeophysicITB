def awal():
    print("*************************************************************************************************")
    print("* SOFTWARE KALKULATOR PERHITUNGAN NUMERIK *")
    print("*************************************************************************************************")
    print("Programer    :  ")
    print("1. Rifky Ramadan                 12318032")
    print("2. Syaiful Apri Kurniawan        12318044")
    print("3. Ziyad Fakhri Kunadi           12318060")

    print("Versi          : 1.0")
    print("Last Update    : 26 November 2019")
    print("*************************************************************************************************")
    print("* contact : kurniawansyaiful3@gmail.com*")
    print("*************************************************************************************************")
    try:
        input("Press enter to continue")
    except SyntaxError:
        pass

def menu():
    print("=================================================================================================")
    print("WELCOME TO KALGI")
    print("=================================================================================================")
    print("MENU UTAMA   ")
    print("-------------------------------------------------------------------------------------------------")
    print("1. Metode Gauss")
    print("2. Metode Trapezoidal")
    print("3. Metode Regresi Kuadrat Terkecil")
    print("4. Metode Interpolasi Newton")
    print("5. Tentang Program")
    print("0. Keluar")
    print("-------------------------------------------------------------------------------------------------")
    perintah = int(input("Masukkan menu untuk melanjutkan : "))
    print("=================================================================================================")
    return perintah

def callback():
    perintah = 0
    while type(perintah) is int:
        perintah = int(menu())
        if perintah == 1:
            import Gauss3 as gs3
            perintah = gs3.callback()
        if perintah == 2:
            import Trapezoid as mtp
            perintah = mtp.callback()
        if perintah == 4:
            import Interpolasi as ipn
            perintah == ipn.callback()
        if perintah == 5 :
            import TentangProgram as ttg
            perintah == ttg.callback()
        elif perintah == 3:
            import Regresi as rgs
            perintah == rgs.callback()
awal()
callback()