
datanama = {}

#------------------------------------------FUNCTION---------------------------------------------------

##-------------------------------------- Function 1 (tambah nama siswa)

def addname():
    nama = input("Masukkan nama siswa : ")
    clear() 
    if nama in datanama :
        print(f" '{nama}' sudah ada dalam database")
    
        
    else :
        datanama[nama] = []
        print(f" '{nama}' telah ditambahkan ke database")
        
    
##------------------------------------- Function 2 (tambah nilai siswa)

def addnilai() :
   print("============================================================")
   print("Daftar Siswa:")
   print(", ".join(datanama.keys()))
   print("============================================================")
   
   nama = input("Masukkan nama siswa : ")
   clear() 
   if nama not in datanama :
        print(f" '{nama}' tidak ditemukan dalam database")
        return
   
   else :
        nilaisiswa = input(f"Masukkan nilai '{nama}' : ")
        if nilaisiswa == ""  :
            print("INPUT SALAH! Nilai tidak boleh kosong.")
            return
        
        elif  not nilaisiswa.isdigit():
            print("INPUT SALAH! Nilai harus berupa angka antara 0 hingga 100.")
            return
        
        else:
            nilaisiswa = int(nilaisiswa)

            if nilaisiswa >= 0 and nilaisiswa <= 100 :
            
                datanama[nama].append(nilaisiswa)
                print(f"Nilai '{nilaisiswa}' telah ditambahkan untuk '{nama}'")
            

            else :
                print("INPUT SALAH! Nilai harus antara 0 hingga 100.")
            

##---------------------------- Function 3 (tampil nilai siswa)

def nampilnilai() :
    print("============================================================")
    print("Daftar Siswa:")
    print(", ".join(datanama.keys()))
    print("============================================================")

    namasiswa = input("Masukkan nama siswa yang ingin ditampilkan nilainya: ")
    clear() 
    if namasiswa not in datanama :
        print(f" '{namasiswa}' tidak ditemukan dalam database")
        return 
    
    else :
        if datanama[namasiswa] == [] :
            print(f" '{namasiswa}' belum memiliki nilai.")
            return
        
        else :
            
            print("Nilai ", *{namasiswa}, ":" , *datanama[namasiswa])

##----------------------------- Function 4 (Rata-rata nilai siswa)
def ratnilai() :
    print("============================================================")
    print("Daftar Siswa:")
    print(", ".join(datanama.keys()))
    print("============================================================")

    namasiswa = input("Masukkan nama siswa yang ingin ditampilkan rata-rata nilainya: ")
    clear() 
    if namasiswa not in datanama :
        print(f" '{namasiswa}' tidak ditemukan dalam database")
        return
    
    elif namasiswa == "" :
        print("INPUT SALAH! Nama siswa gaboleh kosong.")
        return
    
    else :
        if datanama[namasiswa] == [] :
            print(f" '{namasiswa}' belum memiliki nilai.")
            return
        else :
            ratarata = sum(datanama[namasiswa]) / len(datanama[namasiswa])
            print(f"Rata-rata nilai  '{namasiswa}' adalah : {ratarata}")
            
        
##---------------------------------- Fumction 5 (Hapus data siswa)

def hapusdtsiswa() :
    print("============================================================")
    print("Daftar Siswa:")
    print(", ".join(datanama.keys()))
    print("============================================================")

    nama = input("Masukkan nama siswa yang ingin dihapus dari database: ")
    clear()
    if nama in datanama :
        print("ingin menghapus siswa atau nilai siswa?(s/n)")
        hps = input()
        if hps == "n" :
            if datanama[nama] == [] :
                print(f" '{nama}' belum memiliki nilai.")
                return
            else :
                indexhapus = int(input(f"Masukkan urutan nilai yang ingin dihapus dari '{nama}' (mulai dari 0): "))
                if indexhapus < 0 or indexhapus >= len(datanama[nama]):
                    print("INPUT SALAH! Urutan nilai tidak valid.")
                    return
                else :
                    del datanama[nama][indexhapus]
                    print(f"Nilai ke-{indexhapus} untuk '{nama}' telah dihapus.")
        
        elif hps == "s" :
            del datanama[nama]
            print(f" '{nama}' telah dihapus dari database")  

            
    
    else :
        print(f" '{nama}' tidak ditemukan dalam database")
        return   
    
##----------------------------- Function 6 (mengubah nilai siswa)

def ubahnilai() :
    print("============================================================")
    print("Daftar Siswa:")
    print(", ".join(datanama.keys()))
    print("============================================================")

    nama = input("Masukkan nama siswa yang ingin ditampilkan rata-rata nilainya: ")
    clear()
    if nama not in datanama :
        print(f" '{nama}' tidak ditemukan dalam database")
        return 
    
    elif nama == "" :
        print("INPUT SALAH! Nama siswa gaboleh kosong.")
        return

    else :
        if datanama[nama] == [] :
            print(f" '{nama}' belum memiliki nilai.")
            return
        else :
            print("Nilai ", *{nama}, ":" , *datanama[nama])
            indexnilai = int(input(f"Masukkan urutan nilai yang ingin diubah untuk '{nama}' (mulai dari 0): "))
            if indexnilai < 0 or indexnilai >= len(datanama[nama]):
                print("INPUT SALAH! Urutan nilai tidak valid.")
                return
            else :
                changenilai = int(input(f"Masukkan nilai baru untuk '{nama}': "))
                if changenilai < 0 or changenilai > 100 :
                    print("INPUT SALAH! Nilai harus antara 0 hingga 100.")
                    return
            
                else :
                    datanama[nama][indexnilai] = changenilai
                    print(f"Nilai ke-{indexnilai} untuk '{nama}' telah diubah menjadi {changenilai}.")

##------------------------------------- Function 7 (status kelulusan siswa)
def statuskelulusan() :
    print("============================================================")
    print("Daftar Siswa:")
    print(", ".join(datanama.keys()))
    print("============================================================")

    nama = input("Masukkan nama siswa yang ingin ditampilkan rata-rata nilainya: ")
    clear()
    if nama not in datanama :
        print(f" '{nama}' tidak ditemukan dalam database")
        return
    
    elif nama == "" :
        print("INPUT SALAH! Nama siswa gaboleh kosong.")
        return
    else :
        bataskelulusan = int(input("Masukkan nilai KKM: "))
        if bataskelulusan >= 0 and bataskelulusan <= 100 :
            if datanama[nama] == [] :
                print(f" '{nama}' belum memiliki nilai.")
                return
            else :
                ratarata = sum(datanama[nama]) / len(datanama[nama])
                if ratarata >= bataskelulusan :
                    print(f"'{nama}' dinyatakan LULUS dengan rata-rata nilai {ratarata}")
                else :
                    print(f"'{nama}' dinyatakan TIDAK LULUS dengan rata-rata nilai {ratarata}")
           
        else :
            print("INPUT SALAH! nilai KKM harus antara 0 hingga 100.")
            return
            

## --------------------------------------Function 8 (tampil semua data siswa)

def tampilallsiswa() :
    if datanama == {} :
        print("Database siswa kosong.")

    else :
        if datanama == [] :
            print(f" '{nama}' belum memiliki nilai.")
            return
        else :
            for nama, nilai in datanama.items() :
                nilaistr = ", ".join(map(str, nilai))
                
                if nilai == [] :
                    print("============================================================")
                    print(f"siswa: {nama} \nNilai: Belum ada nilai yang ditambahkan.")
                    continue
                else :
                    print("============================================================")
                    print(f"Siswa: {nama} \nNilai: {nilaistr}")
                    ratarata = sum(nilai) / len(nilai)
                    print(f"Rata-rata nilai: {ratarata}")


## --------------------------------------Function (Laporan Akhir)

def Laporan():
    print("============================================================")
    print("LAPORAN AKHIR DATA NILAI SISWA")
    if datanama == {} :
        print("Database siswa kosong.")

    else :
        pilihan = input("Ingin menampilkan laporan untuk semua siswa atau siswa tertentu? (semua/tertentu): ")
        clear()
        if pilihan == "semua" :
            KKM = int(input("Masukkan nilai KKM: "))
            for nama, nilai in datanama.items() :
                nilaistr = ", ".join(map(str, nilai))

                if nilai == [] :
                    print("============================================================")
                    print(f"siswa: {nama} \nNilai: Belum ada nilai yang ditambahkan.")
                    continue
                else :
                    print("============================================================")
                    print(f"Siswa: {nama} \nNilai: {nilaistr}")
                    ratarata = sum(nilai) / len(nilai)
                    print(f"Rata-rata nilai: {ratarata}")
                    if ratarata >= KKM :
                        print(f"Status Kelulusan: LULUS")
                    else :
                        print(f"Status Kelulusan: TIDAK LULUS")

        elif pilihan == "tertentu" :
            nama = input("Masukkan nama siswa yang ingin ditampilkan laporannya: ")
            clear()
            if nama not in datanama :
                print(f" '{nama}' tidak ditemukan dalam database")
                return
            
            elif nama == "" :
                print("INPUT SALAH! Nama siswa gaboleh kosong.")
                return
            else :
                KKM = int(input("Masukkan nilai KKM: "))
                if datanama[nama] == [] :
                    print(f" '{nama}' belum memiliki nilai.")
                    return
                else :
                    nilaistr = ", ".join(map(str, datanama[nama]))
                    print("============================================================")
                    print(f"Siswa: {nama} \nNilai: {nilaistr}")
                    ratarata = sum(datanama[nama]) / len(datanama[nama])
                    print(f"Rata-rata nilai: {ratarata}")
                    if ratarata >= KKM :
                        print(f"Status Kelulusan: LULUS")
                    else :
                        print(f"Status Kelulusan: TIDAK LULUS")
                                    
                
##------------------------------------------------------------END OF FUNCTION-------------------------------------------------

##-----------------------------------------------------------Shortcut------------------------------------------------------------
## --------------------------------------Function buat Clear Screen
def clear():
    print("\n" * 20)

## --------------------------------------function penutup
def closing():
    print(ok, "\n", "Terima kasih telah menggunakan program ini!:D")
ok = """

⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⣷⣄⠀⠀⠀⣀⣤⣤⣤⡀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣶⠏⠀⠀⣿⠀⢀⡾⠛⠋⠀⣾⣿⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⡏⠀⠀⠀⣿⢀⣾⠁⠀⣰⠆⢹⡿⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠃⣧⠀⠀⢠⡟⢸⡇⠀⣰⠟⠀⣼⠃⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣹⣆⢀⣸⣇⣸⠃⢠⡏⠀⣸⠋⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣤⣴⣶⣶⣶⠾⠟⠛⠉⠉⠉⠈⠉⠉⠛⠁⢾⠁⣴⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣤⣤⣶⣶⠾⠟⠛⠛⣻⣿⣙⡁⠀⠀⢾⣶⣾⣷⣿⣶⣄⠀⠀⠀⠀⠰⢿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢀⣀⣀⣀⣠⣴⣶⣶⠾⠟⠛⠉⠉⠉⠀⠀⠀⠀⠀⣿⣻⣟⣻⣿⡦⠀⠘⣿⣿⣛⡿⢶⡇⠀⠀⠀⠀⠀⠀⢻⣆⠀⠀⠀⠀⠀⠀⠀⠀
⣠⣶⣶⣶⣾⣿⣿⣿⣿⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡟⠙⣿⣿⡗⠀⠀⠿⠉⣿⣿⣿⣶⠀⠀⠀⠀⠀⠀⠈⢿⠀⠀⠀⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠳⣄⣿⡿⠁⠀⠀⠘⢦⣿⣿⠇⠟⠁⠀⠀⠀⠀⠀⠀⣸⡇⠀⠀⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⡇⠀⠀⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣇⠀⠀⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⠀⠀⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡏⠀⠀⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀
⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣇⡇⠀⠀⠀⠀⠀⠀⠀
⠀⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢤⣤⡀⠀⠀⠀⠀⠀⠀⠀⣿⡇⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠈⠙⢿⣿⣿⣿⣿⣿⣿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣤⡾⠟⠛⠆⠀⠀⠀⠀⠀⢀⢻⡇⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠈⠙⠿⣿⣭⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣴⣶⠾⠟⠋⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣾⠇⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠙⠛⠷⠶⢶⣶⣦⣤⣴⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣌⣿⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠙⠛⠛⠛⠃⠀⠀⠀⠀⠀⠀⠀⣤⣴⣾⣿⣿⣿⣓⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣼⣿⣷⣦⣄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣠⣤⣶⣾⣟⣯⣽⠟⠋⠀⠉⠳⣄⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⢇⠀⠉⠛⠷⣮⣍⣩⡍⢻⡟⠉⣉⢹⡏⠉⣿⣹⣷⣦⣿⠿⠟⠉⠀⠀⠀⠀⠀⠀⠙⣆⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⠏⢸⠇⠀⠀⠀⠀⠀⠉⠉⠛⠛⠛⠛⠛⠛⠛⠋⠉⠉⠀⠀⠀⠀⠀⢠⣠⡶⠀⠀⠀⠀⠘⣧⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⡿⠀⣸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠟⠁⠀⠀⠀⠀⠀⠘⣆⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⠃⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣇⡀⠀⠀⠀⠀⠀⠀⢹⡆⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣾⠀⣾⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣥⢠⣤⠼⠇⠀⠀⠘⣿⡄
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣽⡄⠈⢿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⠿⠾⠷⠄⠀⠀⠀⢀⣿⠁
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣧⠀⠸⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⣾⠋⠀⠀⠀⠀⠀⠀⢰⣾⡿⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣦⣠⣿⣿⣶⣶⣤⣤⣄⣀⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣠⣴⣿⣇⠀⠀⠀⠀⠀⠀⠀⣸⡟⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢻⣿⠀⠉⠛⢿⣿⣯⣿⡟⢿⠻⣿⢻⣿⢿⣿⣿⣿⣿⣿⠿⠟⠹⣟⢷⣄⠀⠀⠀⢀⣼⠟⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣄⠀⠀⠘⢷⣌⡻⠿⣿⣛⣿⣟⣛⣛⣋⣉⣉⣉⣀⡀⠀⠀⠈⠻⢿⣷⣶⣶⢛⣧⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣏⠀⠀⠀⠀⠹⢯⣟⣛⢿⣿⣽⣅⣀⡀⠀⣀⡀⠀⠀⠀⠠⢦⣀⠰⡦⠀⢸⠀⣏⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⡀⠀⠀⠀⠀⠀⠀⠈⠉⢻⣿⡟⠛⠉⠉⠁⠀⠀⠀⠀⠀⠀⠈⠛⠷⠀⣸⠀⣿⡀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣧⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⣿⡇⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⢿⠀⠀⢦⡀⡀⠀⠀⠀⠀⢹⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡄⡏⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡄⠀⠈⠳⣝⠦⢄⠀⠀⠀⣟⣷⠀⠀⠀⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⣿⡇⡇⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣄⣷⡀⠀⠀⠈⠙⠂⠀⠀⠀⢸⣿⡄⠀⠀⠘⢦⡙⢦⡀⠀⠀⠀⠀⢰⣷⣷⡇⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⡿⢧⣤⣀⡀⠀⠀⠀⠀⠀⠀⢿⣷⣄⠀⠀⠀⠁⠋⠀⠀⠀⠀⠀⢸⣿⣿⣇⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣷⡀⠈⠉⠛⠛⠛⠛⠛⠛⠛⠛⢿⡍⠛⠳⠶⣶⣤⣤⣤⣤⣤⣤⠼⠟⡟⢿⡇⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠰⣾⡇⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣤⣴⣿⣷⣶⣶⣶⣶⣶⣶⣦⣀⣀⣀⣻⡀⠀⠀⠀⣀⣀⠀⡀⠀⠀⠀⢀⣼⣿⠇⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⠟⠉⠁⠀⠀⠈⠻⣿⡆⢹⣯⣽⣿⣿⠟⠋⠙⣿⣶⣿⣿⣿⣿⣾⣿⣿⣿⣟⠋⠉⣇⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⡀⠀⠀⠀⠈⢻⣆⣿⠀⠀⠀⢁⣶⣿⠿⠟⠛⠷⣶⣽⣿⣿⣻⣏⠙⠃⣴⢻⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣷⣀⠀⠀⠉⠀⠀⠀⠀⠀⢹⣿⠀⣀⣴⣿⠋⠀⠀⠀⠀⠀⠀⠉⠻⣿⣧⣿⢀⣰⣿⣿⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢿⣶⣶⣤⣤⣤⣤⣤⣤⣾⣿⣟⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣅⣾⢿⣵⠇⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠛⠛⠛⠛⠛⠛⠛⠉⠉⠉⠁⢹⣜⠷⠦⠤⠤⠤⠤⠤⠴⠶⠛⣉⣱⠿⠁⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠛⠿⠷⣦⣤⣤⣄⣠⣤⣤⡶⠟⠁⠀⠀⠀⠀⠀⠀⠀

"""
    

##---------------------------------------------------------------------------------------------------------------------------------    
    


















#--------------------------------------------------MAIN MENU--------------------------------------------------------------
while True :
    print("\n========================== MENU DATA NILAI SISWA ===========================")
    print("sistem manajemen data siswa patch 2.0")
    print("Pilih menu berikut:")
    print("1. Tambah Nama Siswa")
    print("2. Tambah Nilai Siswa")
    print("3. Tampilkan Nilai Siswa")
    print("4. Rata-rata Nilai SSiswa")
    print("5. Hapus Data Siswa")
    print("6. Ubah Nilai Siswa")
    print("7. Cek Status Kelulusan Siswa")
    print("8. Laporan Siswa")
    print("9. Show database")
    print("10. Keluar")

    pilihan = input("Pilih menu (1-10): ")

    if pilihan == "1" :
        clear() 
        addname()
        print("============================================================")
        balik = input("kembali ke menu?(y/n): ")
        if balik == "y" :
            continue
        elif balik == "n" :
            closing()
            break
        else :
            print("Pilihan tidak valid. Kembali ke menu utama.")
            continue
    
    elif pilihan == "2" :
        clear() 
        addnilai()
        print("============================================================")
        balik = input("kembali ke menu?(y/n): ")
        if balik == "y" :
            continue
        elif balik == "n" :
            closing()
            break
        else :
            print("Pilihan tidak valid. Kembali ke menu utama.")
            continue
    
    elif pilihan == "3" :
        clear() 
        nampilnilai()
        print("============================================================")
        balik = input("kembali ke menu?(y/n): ")
        if balik == "y" :
            continue
        elif balik == "n" :
            closing()
            break
        else :
            print("Pilihan tidak valid. Kembali ke menu utama.")
            continue
    
    elif pilihan == "4" :
        clear() 
        ratnilai()
        print("============================================================")
        balik = input("kembali ke menu?(y/n): ")
        if balik == "y" :
            continue
        elif balik == "n" :
            closing()
            break
        else :
            print("Pilihan tidak valid. Kembali ke menu utama.")
            continue
    
    elif pilihan == "5" :
        clear() 
        hapusdtsiswa()
        print("============================================================")
        balik = input("kembali ke menu?(y/n): ")
        if balik == "y" :
            continue
        elif balik == "n" :
            closing()
            break
        else :
            print("Pilihan tidak valid. Kembali ke menu utama.")
            continue

    elif pilihan == "6" :
        clear() 
        ubahnilai()
        print("============================================================")
        balik = input("kembali ke menu?(y/n): ")
        if balik == "y" :
            continue
        elif balik == "n" :
            closing()
            break
        else :
            print("Pilihan tidak valid. Kembali ke menu utama.")
            continue

    elif pilihan == "7" :
        clear() 
        statuskelulusan()
        print("============================================================")
        balik = input("kembali ke menu?(y/n): ")
        if balik == "y" :
            continue
        elif balik == "n" :
            closing()
            break
        else :
            print("Pilihan tidak valid. Kembali ke menu utama.")
            continue
    
    elif pilihan == "8" :
        clear() 
        Laporan()
        print("============================================================")
        balik = input("kembali ke menu?(y/n): ")
        if balik == "y" :
            continue
        elif balik == "n" :
            closing()
            break
        else :
            print("Pilihan tidak valid. Kembali ke menu utama.")
            continue
    
    elif pilihan == "9" :
        clear() 
        tampilallsiswa()
        print("============================================================")
        balik = input("kembali ke menu?(y/n): ")
        if balik == "y" :
            continue
        elif balik == "n" :
            closing()
            break
        else :
            print("Pilihan tidak valid. Kembali ke menu utama.")
            continue


    elif pilihan == "10" :
        closing()
        break
    
    else :
        print("Pilihan tidak valid. Silakan pilih menu antara 1 hingga 10.")












