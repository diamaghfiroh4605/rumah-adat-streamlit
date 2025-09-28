Berikut adalah contoh file README untuk project kamu agar orang lain mudah memahami aplikasi simulasi rumah adat yang kamu buat dengan Streamlit:

````markdown name=README.md
# Simulasi Dinamika Rumah Adat Indonesia 🏠🌏

Aplikasi ini memodelkan **rumah adat Indonesia** sebagai sistem osilator teredam satu derajat kebebasan (SDOF) terhadap input gempa sederhana. Web ini dibuat menggunakan [Streamlit](https://streamlit.io/) dan dapat diakses secara interaktif.

## Fitur Utama

- **Pilih Material Rumah Adat**: Kayu atau Bambu
- **Input Parameter Gempa**: Gaya gempa, frekuensi, dan durasi simulasi
- **Simulasi Respons Waktu**: Perpindahan rumah adat terhadap gempa
- **Spektrum Frekuensi**: Analisis frekuensi respons rumah
- **Kurva Resonansi**: Menunjukkan amplitudo maksimum pada berbagai frekuensi input
- **Info Frekuensi Resonansi**: Frekuensi resonansi dan amplitudo maksimum

## Cara Menjalankan di Lokal

1. Pastikan sudah menginstal Python (minimal versi 3.8)
2. Install library yang diperlukan:
   ```
   pip install streamlit numpy matplotlib scipy
   ```
3. Jalankan aplikasi dengan perintah:
   ```
   streamlit run app.py
   ```
4. Buka browser dan akses [http://localhost:8501](http://localhost:8501)

## Deploy ke Streamlit Community Cloud

1. Upload repo ini ke GitHub (public).
2. Deploy melalui [Streamlit Community Cloud](https://streamlit.io/cloud).

## Struktur Kode

- `app.py`: Kode utama aplikasi Streamlit

## Kontributor

- diamaghfiroh4605

## Lisensi

Proyek ini menggunakan lisensi MIT.
````
