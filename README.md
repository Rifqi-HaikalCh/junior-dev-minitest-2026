# 🚀 Python Developer Assessment - Mini Test

Repositori ini berisi solusi teknikal untuk *Mini Test Assessment* posisi **Junior Software Developer**. Proyek ini dikerjakan dengan fokus pada pemecahan masalah logis, integrasi API yang aman (*Security Best Practices*), *Error Handling*, dan *User Experience (UX)* melalui antarmuka *Command Line* (CLI) yang interaktif.

---

## 📂 Struktur Proyek

Proyek ini terbagi menjadi dua program utama:
1. `main.py` : Solusi untuk Task 1 (Logika Sekuensial & Algoritma Prima).
2. `cuaca.py`: Solusi untuk Task 2 (Integrasi RESTful API OpenWeatherMap).

---

## 🛠️ Task 1:
**File Utama:** `main.py`

Program ini adalah pengembangan dari tes logika fundamental (variasi FizzBuzz dengan filter Bilangan Prima). 

**Fitur & Arsitektur Logika:**
* **Optimasi Algoritma Prima:** Menggunakan metode *Trial Division* teroptimasi ($O(\sqrt{n})$) dibandingkan dengan iterasi linear biasa.
* **Open-Closed Principle:** Logika translasi teks menggunakan metode *string concatenation* yang mudah dikembangkan (contoh: menambahkan kelipatan 7 tanpa merusak *nested if* yang ada).
* **Analytical Post-Output:** Memberikan penjabaran metrik data setelah hasil ditampilkan kepada pengguna.

### 📸 Bukti Eksekusi (Screenshot)
![Task 1 - Tampilan Awal & Input](./image/screenshot_task1%20(1).png.png)
*Tampilan awal interaktif dan pemrosesan deret angka.*

![Task 1 - Penjelasan Analitik](./image/screenshot_task1%20(2).png.png)
*Fitur tambahan berupa Penjelasan Output untuk membedah statistik data.*

---

## 🌦️ Task 2:
**File Utama:** `cuaca.py`

Sistem pemantauan cuaca yang terintegrasi dengan **OpenWeatherMap API**. 

**Fitur & Arsitektur Logika:**
* **API Chaining Architecture:** Untuk mematuhi aturan pengujian *"No Paid Account"*, sistem ini menghindari pemakaian *endpoint OneCall 3.0* dan menggunakan metode 2 tahap: *Geocoding API* (mencari titik koordinat) dilanjutkan dengan *Forecast API 2.5* (menarik data).
* **Data Aggregation:** Karena API gratis memberikan data per 3 jam, sistem menggunakan `collections.defaultdict` untuk mengelompokkan data berdasarkan hari dan mengkalkulasi nilai suhu rata-rata (*mean*) demi memenuhi aturan *"Only show one temperature per day"*.
* **Security & Credential Management:** API Key tidak di-*hardcode* di dalam skrip, melainkan dikelola secara aman menggunakan **Environment Variables** (`.env`).

### 📸 Bukti Eksekusi (Screenshot)
![Task 2 - Pencarian Data API](./image/screenshot_task2%20(1).png.png)
*Sistem memproses pencarian lokasi melalui Geocoding dan menampilkan kalkulasi suhu 5 hari ke depan.*

![Task 2 - Penjelasan Sistem](./image/screenshot_task2%20(2).png.png)
*Penjelasan arsitektur logika dan ekstraksi data ekstrem untuk memberikan added-value analisis bisnis.*

---

## ⚙️ Panduan Instalasi & Eksekusi

Bagi peninjau (*reviewer*), silakan ikuti langkah berikut untuk menjalankan proyek ini di lingkungan lokal Anda:

### 1. Kloning Repositori
```bash
git clone <URL_REPOSITORY_ANDA>
cd mini-test
```

### 2. Persiapan Virtual Environment & Dependencies
Dianjurkan untuk menggunakan *virtual environment*.
```bash
pip install -r requirements.txt
```
*(Dependencies utama: `requests` dan `python-dotenv`)*

### 3. Konfigurasi Environment Variables (Sangat Penting)
Demi keamanan, API Key tidak disertakan dalam repositori ini. Anda harus membuat file `.env` di direktori *root* (sejajar dengan file `.py`) dan memasukkan kunci API OpenWeatherMap milik Anda:
```env
OPENWEATHER_API_KEY=masukkan_api_key_anda_disini
```

### 4. Menjalankan Program
Gunakan terminal untuk mengeksekusi masing-masing program:
```bash
# Menjalankan Task 1
python main.py

# Menjalankan Task 2
python cuaca.py
```

---
*Dikerjakan oleh **Rifqi Haikal Chairiansyah** | Juni 2026*
