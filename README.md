# Sistem Pengelola Nilai Siswa — Python Function Practice

Program ini dibuat untuk latihan penggunaan function pada Python melalui studi kasus nyata: mengelola nilai siswa dalam sebuah kelas. Program ini menggunakan dictionary sebagai tempat penyimpanan data, serta beberapa function untuk menambah, mengubah, mengevaluasi, dan menampilkan data.

---

## ✨ Fitur Utama

- Menambah siswa beserta nilainya
- Mengubah nilai siswa
- Menghitung rata-rata nilai
- Menampilkan siswa dengan nilai tertinggi dan terendah
- Menampilkan semua data secara terurut (highest to lowest)

---

## 🧩 Struktur Function

### 1. `tambah_siswa(nama, nilai)`
Menambahkan siswa baru ke dalam database.
- Jika nama sudah ada → menolak
- Validasi nilai 0–100

### 2. `ubah_nilai(nama, nilai_baru)`
Mengubah nilai siswa yang sudah terdaftar.
- Jika siswa tidak ditemukan → error

### 3. `rata_rata()`
Menghitung dan mengembalikan rata-rata nilai seluruh siswa.
- Jika data kosong → pesan khusus

### 4. `nilai_tertinggi()`
Mengembalikan tuple (nama, nilai) siswa dengan nilai tertinggi.

### 5. `nilai_terendah()`
Mengembalikan tuple (nama, nilai) siswa dengan nilai terendah.

### 6. `tampilkan_semua()`
Menampilkan seluruh data siswa dalam format rapi, diurutkan dari nilai tertinggi.

---

## 📁 Contoh Struktur Data

```python
nilai_siswa = {
    "Andi": 87,
    "Budi": 75,
    "Citra": 95
}
```

---

## 📌 Contoh Penggunaan

```python
tambah_siswa("Andi", 90)
tambah_siswa("Budi", 75)
tambah_siswa("Citra", 95)

print("Rata-rata nilai:", rata_rata())
print("Nilai tertinggi:", nilai_tertinggi())
print("Nilai terendah:", nilai_terendah())

tampilkan_semua()
```

---

## 🧪 Contoh Output

```
Citra — 95
Andi — 90
Budi — 75
```

---

## 🎯 Tujuan Pembelajaran

Project ini dibuat untuk melatih:
- Pembuatan function Python
- Penggunaan parameter & return value
- Pengelolaan data dengan dictionary
- Percabangan (if/elif/else)
- Formatting output
- Penyelesaian kasus nyata dalam coding

---

## 🔧 Pengembangan Lanjutan

Fitur tambahan yang bisa ditambahkan:
- Hapus siswa
- Ekspor data ke file
- Input interaktif (CLI)
- Validasi input lebih ketat
- Versi OOP menggunakan class

---

**“Setiap baris kode adalah jejak kecil menuju versi dirimu yang lebih kuat dan lebih pintar.”**
