# Pantau Hutan — Studi Kasus AI dan Peringatan Deforestasi

Dashboard pembelajaran yang terinspirasi dari materi kuliah **“Attributing Direct Drivers to Deforestation Alerts with Satellite Imagery and AI”**.

## Tujuan studi kasus

Menampilkan dan membandingkan kategori penyebab gangguan hutan tropis (pertanian skala kecil/besar, pertambangan, penebangan selektif, kebakaran, dan gangguan alami) berdasarkan wilayah dan tanggal. Dashboard membantu pembaca memahami bagaimana label peringatan dapat diringkas menjadi informasi yang lebih mudah dibaca.

## Teknologi

- Python
- Flask untuk backend web
- Pandas untuk pengolahan data
- HTML dan CSS untuk antarmuka
- Chart.js untuk grafik interaktif

## Struktur file

```text
Studi_Kasus_Deforestasi_AI/
├── app.py
├── data_alert_deforestasi.csv
├── requirements.txt
├── README.md
├── LAPORAN_STUDI_KASUS.md
├── .gitignore
└── templates/
    └── index.html
```

## Cara menjalankan di komputer

Pastikan Python 3.10 atau lebih baru telah terpasang.

1. Ekstrak file ZIP.
2. Buka terminal di folder proyek.
3. Buat lingkungan virtual (opsional tetapi disarankan):

   Windows:
   ```bash
   py -m venv .venv
   .venv\Scripts\activate
   ```

   macOS/Linux:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

4. Instal pustaka:
   ```bash
   pip install -r requirements.txt
   ```
5. Jalankan aplikasi:
   ```bash
   python app.py
   ```
6. Buka `http://127.0.0.1:5000` di browser.

Grafik memakai Chart.js dari CDN, jadi koneksi internet diperlukan agar grafik dapat dimuat. Tabel dan ringkasan tetap berasal dari backend Python.

## Mengunggah ke GitHub

1. Buat repositori baru di GitHub, misalnya `studi-kasus-deforestasi-ai`. Untuk proyek tugas, pilih **Public** jika ingin dosen dapat melihatnya.
2. Buka terminal di folder proyek dan jalankan:

   ```bash
   git init
   git add .
   git commit -m "Tambah studi kasus pemantauan deforestasi"
   git branch -M main
   git remote add origin https://github.com/USERNAME/studi-kasus-deforestasi-ai.git
   git push -u origin main
   ```

3. Ganti `USERNAME` dengan nama akun GitHub milikmu. Jika Git meminta autentikasi, ikuti instruksi GitHub.

**Catatan:** perintah di atas menyiapkan langkah unggah, tetapi repositori belum dibuat atau diunggah otomatis ke akun GitHub.

## Batasan proyek

Dataset CSV di sini adalah **data simulasi untuk pembelajaran**, bukan data resmi Sentinel atau Global Forest Watch. Proyek ini belum memproses citra satelit dan belum melatih CNN. Kolom `penyebab` merupakan label contoh yang sudah tersedia. Untuk sistem nyata, diperlukan citra Sentinel-1/Sentinel-2, data label yang tervalidasi, pipeline geospasial, pelatihan dan evaluasi model, serta verifikasi lapangan.
