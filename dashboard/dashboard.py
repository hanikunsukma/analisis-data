import pandas  as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency

sns.set(style='dark')

st.title("Dashboard Bike Sharing Dataset")

main_data_df = pd.read_csv("main_data.csv")

# Menampilkan pertanyaan 1
st.header("Pertanyaan 1: Apakah lebih banyak orang menggunakan sepeda pada hari kerja atau hari libur?")

# Menghitung rata-rata penggunaan sepeda
workingday_bike_usage = main_data_df.groupby(by='workingday').agg({'cnt': 'mean'})

# Menampilkan grafik
fig1, ax1 = plt.subplots()
workingday_bike_usage.plot(kind='bar', color=['skyblue', 'lightgreen'], ax=ax1)
ax1.set_title('Rata-rata Penggunaan Sepeda: Hari Kerja vs Hari Libur')
ax1.set_xlabel('Working Day (0: Hari Libur, 1: Hari Kerja)')
ax1.set_ylabel('Jumlah Pengguna Sepeda')
ax1.set_xticklabels(['Hari Libur', 'Hari Kerja'], rotation=0)

# Menampilkan grafik di Streamlit
st.pyplot(fig1)

# Kesimpulan
st.write("""
**Kesimpulan:** Dari data yang diberikan, rata-rata penggunaan sepeda pada hari kerja adalah 193.21 dan pada hari libur adalah 181.41. 
Ini menunjukkan bahwa sedikit lebih banyak orang menggunakan sepeda pada hari kerja dibandingkan hari libur, 
meskipun perbedaannya tidak terlalu signifikan. Mungkin karena orang masih menggunakan sepeda sebagai alat transportasi utama meski bekerja.
""")

# Kolom 2: Pertanyaan 2
st.header("Pertanyaan 2: Apakah suhu yang lebih tinggi membuat lebih banyak orang menggunakan sepeda?")

# Menampilkan grafik korelasi
plt.figure(figsize=(8, 6))
sns.heatmap(main_data_df[['temp', 'cnt']].corr(), annot=True, cmap='coolwarm', vmin=-1, vmax=1)
plt.title('Korelasi antara Suhu dan Jumlah Pengguna Sepeda')

# Menampilkan grafik di Streamlit
st.pyplot(plt)

# Kesimpulan
st.write("""
**Kesimpulan:** Dari tabel korelasi, terdapat korelasi positif sebesar 0.40 antara suhu dan jumlah pengguna sepeda. 
Ini berarti ada hubungan moderat antara suhu yang lebih tinggi dengan peningkatan penggunaan sepeda. 
Ketika suhu meningkat, lebih banyak orang cenderung menggunakan sepeda, meskipun faktor ini bukan satu-satunya yang memengaruhi keputusan pengguna.
""")