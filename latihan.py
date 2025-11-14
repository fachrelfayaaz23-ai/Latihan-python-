datanama = {}
datanilai = []

#----------------------------FUNCTION--------------------------------
def addname():
    nama = input("Masukkan nama siswa : ")

    if nama in datanama :
      print(f"Nama '{nama}' sudah ada dalam database")

    else :
       datanama[nama] = []
       print(f"nama '{nama}' telah ditambahkan")

def addnilai() :
   siswanilai = input("Masukkan nama siswa yang akan dinilai: ")
   if siswanilai not in datanama :
      print(f"Nama '{siswanilai}' tidak ditemukan dalam database")

   else :
      nilaisiswa = int(input(f"Masukkan nilai '{siswanilai}' : "))

      if nilaisiswa < 0 or nilaisiswa > 100 :
         print("INPUT ERROR")

      else :
         
         print("Nilai sudah masuk")
         

addname()

addnilai()
      
