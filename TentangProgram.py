import numpy as np

def callback():
    print(" Tentang Program:")
    print("Program KALGI 1.0(Kalkulator Digital) ini adalah program yang menjadi alat bantu hitung,")
    print( "yang dapat membantu pengguna dalam perhitungan beberapa operasi matematika.")
    print("Program ini dapat menyelesaikan beberapa operasi matematika, antara lain ")
    print("Metode Gauss, Metode Trapezoidal, Metode Regresi Kuadrat Terkecil, dan Metode Interpolasi Polinom Newton.")
    print("Program ini memberikan beberapa fitur agar pengguna dapat memasukkan secara manual data yang akan diselesaikan ataupun menginput dari data yang telah ada.")
    print("Perhitungan solusi akan dilakukan setelah memasukkan soal pada program. ")
    print("Solusi dari perhitungan tersebut dapat dilihat secara manual pada program, atau dapat disimpan dalam bentuk file jika solusi ingin dilihat di kemudian hari.")
    try:
        input("Press enter to continue")
    except SyntaxError:
        pass