print("==========Silahkan Masukkan Sandi Dan Kata Sandi Untuk Login==========")
data_kamus = {
    "Safril": "Safril072","Gatshu": "Gatshu1143","Ido": "Ido1123","Ilham": "Ilham4536","Salwan": "Salwan0706",
    "Agung": "Agung237","Desstito": "Desstito6784","Nabil": "Nabil12098","Mujaddid": "Mujaddid8543","Amir": "Amir1563"
}

def login():
    username = input("Nama Pengguna: ")
    kata_sandi = input("Kata Sandi: ")

    if username in data_kamus and kata_sandi == data_kamus[username]:
        print("Selamat Datang!")
    else:
        print("Mohon masukkan data Anda dengan benar!")

login()