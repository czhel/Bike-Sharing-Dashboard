# **BIKE SHARING DASHBOARD**

## 📌**Deskripsi Proyek**
Proyek ini bertujuan untuk menganalisis data penyewaan sepeda pada dataset Bike Sharing Dataset, dan fokus menggunakan satu berkas, yaitu berkas "day.csv". Setelah itu membangun dashboard interaktif dengan Streamlit, dan analisis dataset Bike Sharing ini fokus pada pola penggunaan berdasarkan waktu, cuaca, suhu, hari, dan tipe pengguna. 

## **Struktur Direktori**
- Submission
  - dashboard
    - main_data.csv
    - dashboard.py
  - data
    - day.csv
  - notebook.ipynb
  - README.md
  - requirements.txt
  - url.txt

## **Proses Analisis Data**
Seluruh proses analisis dilakukan pada file notebook.ipynb, yang mencangkup:
- Memuat dataset day.csv
- Data Wrangling (Gathering, Assessing, dan Cleaning)
- Exploratory Analysis Data (EDA)
- Visualization dan Explanatory
- Analisis Lanjutan
- Conclusion
Hasil dari proses diatas menghasilkan dataset yang siap digunakan untuk visualisasi pada dashboard (main_data.csv).

## **Insight Utama**
- Pengguna registered mendominasi jumlah penyewaan dibandingkan casual
- Kondisi cuaca sangat mempengaruhi jumlah penyewaan
- Suhu memiliki pengaruh terhadap tingkat penggunaan sepeda
- Pola penyewaan berbeda pada hari kerja, akhir pekan, dan libur nasional
- Pengguna casual cenderung meningkat pada waktu tertentu (seperti akhir pekan).

## **Fitur Dashboard**
Dashboard yang dibangun menggunakan Streamlit memiliki fitur:
- Filter rentang waktu
- Statistik rata-rata penyewaan
- Proporsi pengguna (casual vs registered)
- Analisis berdasarkan:
  - Cuaca
  - Suhu
  - Hari dalam seminggu
- Perbandingan penggunaan casual dan registered

## **Cara Menjalankan**
1. Install Depedencies -> pip install -r requirements.txt
2. Jalankan Dashboard -> streamlit run dashboard.py

## **Teknologi yang Digunakan**
- Python
- Pandas
- Matplotlib
- Seaborn
- Streamlit

## **Author**
- **Nama**             : Cicilia Beladina
- **Learning Path**    : Data Scientist
- **Cohort**           : CDC-33

Proyek ini dibuat sebagai bagian dari submission untuk modul "Fundamental Analisis Data".
