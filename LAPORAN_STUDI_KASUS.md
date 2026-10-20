# Laporan Studi Kasus
## Pantau Hutan: Dashboard Peringatan Deforestasi Berdasarkan Penyebab Langsung

### 1. Latar belakang

Pemantauan kehilangan tutupan hutan tidak cukup hanya menunjukkan lokasi terjadinya perubahan. Informasi mengenai penyebab langsung—misalnya pertanian, pertambangan, penebangan selektif, kebakaran, atau gangguan alami—dapat membantu pengelola kawasan menentukan prioritas pemeriksaan. Materi kuliah membahas pendekatan yang menggabungkan citra Sentinel-1 (radar), Sentinel-2 (optik), dan deep learning untuk mengklasifikasikan penyebab gangguan hutan.

### 2. Rumusan masalah

Data peringatan deforestasi dapat memiliki banyak kategori, tanggal, dan wilayah. Jika hanya disajikan sebagai tabel mentah, pola utama sulit terlihat. Bagaimana menyusun dashboard sederhana agar pengguna dapat memfilter data dan membandingkan penyebab gangguan hutan?

### 3. Tujuan

1. Membuat dashboard berbasis Python untuk meringkas peringatan deforestasi.
2. Menampilkan perbandingan kategori penyebab dan wilayah dalam bentuk grafik.
3. Memungkinkan pengguna menyaring data berdasarkan wilayah dan penyebab.
4. Menunjukkan keterbatasan interpretasi hasil klasifikasi otomatis.

### 4. Rancangan solusi

Aplikasi menggunakan Flask sebagai backend, Pandas untuk membaca serta mengolah CSV, HTML/CSS sebagai antarmuka, dan Chart.js untuk menggambar grafik. Pengguna memilih wilayah dan kategori penyebab. Backend menyaring data lalu menghitung jumlah baris, total luas gangguan, rata-rata keyakinan model, serta agregasi untuk grafik.

### 5. Alur sistem

1. Pengguna membuka halaman dashboard.
2. Python membaca `data_alert_deforestasi.csv`.
3. Pengguna memilih filter wilayah dan/atau penyebab.
4. Flask dan Pandas menyaring data.
5. Backend menghitung ringkasan dan menyiapkan data grafik.
6. Halaman menampilkan kartu ringkasan, grafik, dan tabel rincian.

### 6. Implementasi

- `app.py`: rute Flask, filter data, agregasi, dan perhitungan ringkasan.
- `templates/index.html`: layout dashboard, form filter, tabel, serta grafik.
- `data_alert_deforestasi.csv`: data contoh untuk tiga wilayah dan beberapa kategori penyebab.
- `requirements.txt`: daftar pustaka yang diperlukan.

### 7. Interpretasi hasil

Dashboard dapat digunakan untuk melihat kategori mana yang memiliki jumlah alert lebih banyak pada dataset simulasi, membandingkan wilayah, dan memeriksa catatan setiap baris. Nilai keyakinan model ditampilkan sebagai informasi pendukung, bukan bukti bahwa suatu label pasti benar. Kasus seperti kebakaran dan gangguan alami perlu diverifikasi karena dapat memiliki pola yang mirip, sebagaimana dibahas dalam materi.

### 8. Hubungan dengan materi kuliah

Materi kuliah menjelaskan penggunaan CNN untuk mengenali penyebab langsung dari citra satelit. Proyek ini berada pada tahap visualisasi dan eksplorasi data setelah label tersedia. Dengan demikian, proyek ini menerapkan bagian pengolahan dan penyajian informasi, bukan mereplikasi keseluruhan sistem CNN atau pipeline citra satelit.

### 9. Keterbatasan

1. Data yang digunakan merupakan simulasi, bukan data satelit nyata.
2. Model CNN tidak dilatih di dalam proyek ini.
3. Tidak ada pemrosesan raster atau citra Sentinel-1/Sentinel-2.
4. Grafik memerlukan koneksi internet untuk mengambil Chart.js dari CDN.
5. Hasil dashboard tidak boleh digunakan untuk mengambil keputusan penegakan hukum atau tindakan lapangan tanpa validasi data dan verifikasi ahli.

### 10. Pengembangan lanjutan

- Mengganti data simulasi dengan data resmi yang memiliki lisensi dan dokumentasi jelas.
- Menambahkan peta menggunakan koordinat dan data geospasial tervalidasi.
- Mengintegrasikan citra Sentinel-1 dan Sentinel-2, lalu melatih serta mengevaluasi CNN dengan data berlabel.
- Menyajikan metrik evaluasi seperti precision, recall, F1-score, dan confusion matrix.
- Menambahkan mekanisme validasi lapangan dan catatan ketidakpastian.

### 11. Kesimpulan

Dashboard Pantau Hutan memperlihatkan bagaimana data peringatan deforestasi yang sudah diberi label dapat diringkas menjadi informasi visual yang lebih mudah dipahami. Python dan Flask digunakan untuk pengolahan data, sedangkan HTML/CSS dan grafik digunakan untuk menyajikan informasi. Agar dapat dipakai untuk pemantauan nyata, sistem masih memerlukan data satelit resmi, model yang diuji, dan validasi lapangan.
