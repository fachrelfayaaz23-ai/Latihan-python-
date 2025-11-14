# Latihan-python-
Buat latihan
Berikut README yang rapi, jelas, dan cocok buat GitHub. Bahasa santai tapi tetap profesional.

⸻

Aplikasi Cek Ongkos Kirim Sederhana 🚚

Program ini adalah studi kasus sederhana untuk latihan function di Python.
Tujuannya adalah menghitung ongkos kirim berdasarkan jarak dan jenis layanan.

Program ini cocok untuk pemula yang ingin memahami bagaimana function bekerja, bagaimana menerima parameter, memproses data, dan mengembalikan nilai.

⸻

📌 Fitur Program

Program dapat menghitung ongkir berdasarkan dua jenis layanan:

1. Reguler
Biaya: Rp 2.000 per km

2. Kilat
Biaya: Rp 3.500 per km

⸻

🧠 Cara Kerja

Kamu hanya perlu memanggil function berikut:

def hitung_ongkir(jarak, layanan):
    if layanan == "reguler":
        return jarak * 2000
    elif layanan == "kilat":
        return jarak * 3500
    else:
        return "Layanan tidak valid"

Function menerima:
• jarak (int/float) → jarak tempuh dalam kilometer
• layanan (str) → “reguler” atau “kilat”

Kemudian mengembalikan total ongkir sesuai jenis layanan.

⸻

📍 Contoh Penggunaan

jarak = 10
layanan = "kilat"

total = hitung_ongkir(jarak, layanan)
print("Total ongkir:", total)

Output:

Total ongkir: 35000


⸻

📂 Tujuan Pembelajaran

Studi kasus ini membantu kamu memahami:

• Cara membuat function di Python
• Cara kerja input parameter
• Penggunaan percabangan (if/elif/else)
• Cara mengembalikan nilai (return)
• Cara menggunakan function di program utama

⸻

📬 Catatan

Program ini bisa dikembangkan menjadi lebih lengkap, misalnya dengan menambah:

• Estimasi waktu pengiriman
• Validasi input
• Tarif layanan tambahan
• Menu interaktif

Kalau mau, aku bisa bantu buat versi lanjutannya.

⸻

“Kode yang bagus bukan yang rumit, tapi yang membuat pembacanya merasa pintar.”
