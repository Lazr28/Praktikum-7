dataMhs = {}
def Jdl_Tbl () :
    print("=========================================================================")
    print("| No |     NIM     |       NAMA        |  TUGAS  |  UTS | UAS |  AKHIR  |")
    print("=========================================================================")
def Tambah ():
        nim = input("Masukan NIM          : ")
        nama = input("Masukan Nama         : ")
        tugas = input("Masukan Nilai Tugas  : ")
        if tugas == "":
            tugas = 0
        uts = input("Masukan Nilai UTS    : ")
        if uts == "":
            uts = 0
        uas = input("Masukan Nilai UAS    : ")
        if uas == "":
            uas = 0

        akhir = ((int(tugas) / 100*30) +
                 (int(uts)/100*35) + (int(uas) / 100*35))
        dataMhs[nim] = {"nama": nama, "tugas": tugas,
                        "uts": uts, "uas": uas, "akhir": akhir}
def Lihat ():
    print("Daftar Nilai")
    Jdl_Tbl()
    if len(dataMhs) == 0:
        print("|                         TIDAK ADA DATA                                |")
    else:
        x = 1
        for i, j in dataMhs.items():
            print('| {0:^3}| {1:11} | {2:<17} | {3:7} | {4:4} | {5:3} | {6:7.2f} |'.format(x, i, dataMhs[i]["nama"], dataMhs[i]["tugas"], dataMhs[i]["uts"], dataMhs[i]["uas"], dataMhs[i]["akhir"]))
            x += 1
    print("=========================================================================")
def cariNIM(nim):
        Jdl_Tbl()
        if (dataMhs.get(nim, "kosong") != "kosong"):
            print('| {0:^3}| {1:11} | {2:<17} | {3:7} | {4:4} | {5:3} | {6:6.2f} |'.format(
                1, nim, dataMhs[nim]["nama"], dataMhs[nim]["tugas"], dataMhs[nim]["uts"], dataMhs[nim]["uas"], dataMhs[nim]["akhir"]))
        else:
            print("|                 DATA MAHASISWA DENGAN NO NIM ",
                  nim, "KOSONG / TIDAK ADA     |")
        print("=========================================================================")
def cariNama(nama):
    x,found = 0,0
    Jdl_Tbl()
    for i, j in dataMhs.items():
        x+=1
        
        if ((dataMhs.get(i)).get('nama').startswith(nama)):
            found += 1
            print('| {0:^3}| {1:11} | {2:<17} | {3:7} | {4:4} | {5:3} | {6:6.2f} |'.format(
                1, i, dataMhs[i]["nama"], dataMhs[i]["tugas"], dataMhs[i]["uts"], dataMhs[i]["uas"], dataMhs[i]["akhir"]))
    if (found ==0):
        print("Data tidak ada")
    print("=========================================================================")
def Ubah(nim):
    if (dataMhs.get(nim, "kosong") != "kosong"):
            nama = input("Masukan Nama         : ")
            if nama == "":
                nama = dataMhs[nim]['nama']
            tugas = input("Masukan Nilai Tugas  : ")
            if tugas == "":
                tugas = dataMhs[nim]['tugas']
            uts = input("Masukan Nilai UTS    : ")
            if uts == "":
                uts = dataMhs[nim]['uts']
            uas = input("Masukan Nilai UAS    : ")
            if uas == "":
                uas = dataMhs[nim]['uas']
            akhir = ((int(tugas) / 100*30) +
                     (int(uts)/100*35) + (int(uas) / 100*35))
            dataMhs[nim] = {"nama": nama, "tugas": tugas,
                            "uts": uts, "uas": uas, "akhir": akhir}
            print("Berhasil Mengubah Data")
    else:
            print("Data tidak ditemukan.\nPastikan anda memasukan NIM yang benar ")
            
print("                         Program Input Nilai")
print("=========================================================================")
while True:
    menu = input("(L)ihat, (T)ambah, (U)bah, (H)apus, (C)ari, (K)eluar : ")
    if menu.capitalize() == "T":
        Tambah()
    if menu.capitalize() == "L":
        Lihat()
    if menu.capitalize() == "U":
        print("Mengubah data Mahasiswa")
        nim = input("Masukan NIM          : ")
        Ubah(nim)

    if menu.capitalize() == "H":
        print("Menghapus data Mahasiswa")
        nim = input("Masukan NIM : ")
        if (dataMhs.get(nim, "kosong") != "kosong"):
            dataMhs.pop(nim)
            print("Berhasil menghapus data mahasiswa")
        else:
            print("Data tidak ditemukan.\nPastikan anda memasukan NIM yang benar ")

    if menu.capitalize() == "C":
        print("Mencari Nilai Mahasiswa")
        SearchBy = input("Cari berdasarkan 1. NIM atau 2. Nama :")
        if SearchBy == "1" :
            nim = input("Masukan NIM :")
            cariNIM(nim)
        elif SearchBy == "2" :
            nama = input("Masukan Nama : ")
            cariNama(nama)
            
    if menu.capitalize() == "K":
        print("Keluar dari program..")
        break
    
    elif menu.capitalize() not in ('L', 'T', 'U', 'H', 'C','K'):
        print("Mohon Pilih menu yang benar!")