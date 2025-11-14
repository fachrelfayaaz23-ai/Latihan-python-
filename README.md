Siap bro, ini README yang rapi, kek buat GitHub, bahasa santai tapi tetap profesional. Tinggal lu copy saja ke repo lu.

---

# **📘 Sistem Pengelolaan Nilai Siswa (Python Project)**

Project ini dibuat sebagai latihan untuk memahami konsep **function** di Python melalui studi kasus sederhana mengenai sistem pengelolaan nilai siswa. Program ini memungkinkan pengguna untuk menambah siswa, menambah nilai, menghitung rata-rata, menentukan status kelulusan, hingga menampilkan laporan lengkap.

---

## **🚀 Fitur Utama**

Program ini memiliki beberapa fitur utama yang semuanya diimplementasikan menggunakan function:

### **1. Menambah Siswa**

Menambahkan nama siswa baru ke dalam database.

### **2. Menambah Nilai Siswa**

Memasukkan nilai (0–100) ke dalam daftar nilai siswa tertentu.

### **3. Menghitung Rata-rata Nilai**

Mengembalikan nilai rata-rata dari seorang siswa.

### **4. Menentukan Status Kelulusan**

Jika nilai rata-rata ≥ 75 → *Lulus*, jika tidak → *Tidak Lulus*.

### **5. Menampilkan Laporan Semua Siswa**

Menampilkan nama siswa, nilai, rata-rata, dan status kelulusannya.

---

## **✨ Fitur Tambahan (Opsional)**

Program ini juga bisa dilengkapi dengan fitur tambahan seperti:

* **Mencari siswa berdasarkan keyword**
* **Menghapus siswa**
* **Mengubah nilai tertentu**

---

## **🧠 Struktur Data Utama**

Program ini menggunakan satu dictionary sebagai database:

```python
database = {
    "NamaSiswa": [list_nilai]
}
```

---

## **📌 Daftar Function yang Harus Ada**

Program ini dibangun menggunakan function berikut:

* `tambah_siswa(nama)`
* `tambah_nilai(nama, nilai)`
* `hitung_rata(nama)`
* `status_siswa(nama)`
* `laporan()`

Fitur opsional:

* `cari_siswa(keyword)`
* `hapus_siswa(nama)`
* `update_nilai(nama, indeks, nilai_baru)`

---

## **🧪 Skenario Testing**

Sistem diuji dengan langkah berikut:

1. Menambahkan siswa: **Andi**, **Budi**, **Citra**
2. Menambah nilai:

   * Andi → 80, 75, 90
   * Budi → 60, 55
   * Citra → 100, 95
3. Menampilkan laporan
4. Menampilkan status kelulusan semua siswa
5. Mencari siswa dengan keyword `"i"`

---

## **📤 Contoh Output**

```
Nama: Andi
Nilai: [80, 75, 90]
Rata-rata: 81.67
Status: Lulus
-------------------------
Nama: Budi
Nilai: [60, 55]
Rata-rata: 57.50
Status: Tidak Lulus
-------------------------
Nama: Citra
Nilai: [100, 95]
Rata-rata: 97.50
Status: Lulus
-------------------------
Pencarian 'i': ['Andi', 'Citra']
```

---

## **📎 Tujuan Pembelajaran**

Project ini dirancang untuk membantu mahasiswa memahami:

* Cara membuat function modular yang terorganisir
* Cara mengolah data menggunakan dictionary
* Struktur program Python yang rapi dan mudah diperluas
* Cara menerapkan logika sederhana pada kasus dunia nyata

---

## **🧑‍💻 Catatan**

Program ini masih sederhana dan ditujukan sebagai latihan dasar. Ke depannya bisa dikembangkan menjadi:

* Versi **OOP (Class Siswa & Class Sistem)**
* Sistem **berbasis file (JSON/CSV)**
* Sistem **berbasis menu CLI**
* Integrasi **GUI (Tkinter/PyQt)**

---

Kalau lu mau, gua bisa buatin:

* versi OOP
* versi yang ada menu (CLI interaktif)
* atau gua rapihin kodingan lu buat dimasukin ke GitHub

Tinggal bilang bro.
