import pandas as pd
import matplotlib.pyplot as plt

# 1. Load Data
df = pd.read_csv('sales_data.csv')
df['tanggal'] = pd.to_datetime(df['tanggal'])

# 2. Kalkulasi Pendapatan
df['total_pendapatan'] = df['jumlah_terjual'] * df['harga_satuan']

# 3. Analisis Bulanan
df['bulan'] = df['tanggal'].dt.to_period('M')
laporan_bulanan = df.groupby('bulan')['total_pendapatan'].sum().reset_index()

# 4. Analisis Triwulan
df['triwulan'] = df['tanggal'].dt.to_period('Q')
laporan_triwulan = df.groupby('triwulan')['total_pendapatan'].sum().reset_index()

# 5. Output ke Terminal
print("--- Laporan Bulanan ---")
print(laporan_bulanan)
print("\n--- Laporan Triwulan ---")
print(laporan_triwulan)

# 6. Simpan hasil ke file CSV
laporan_bulanan.to_csv('hasil_bulanan.csv', index=False)
laporan_triwulan.to_csv('hasil_triwulan.csv', index=False)

# 7. Visualisasi (Diagram Lingkaran)
plt.figure(figsize=(8, 6))

# Mengonversi kolom triwulan ke string agar kompatibel dengan matplotlib
labels = laporan_triwulan['triwulan'].astype(str)

plt.pie(laporan_triwulan['total_pendapatan'], 
        labels=labels, 
        autopct='%1.1f%%', 
        startangle=140, 
        colors=['#ff9999','#66b3ff','#99ff99'])

plt.title('Distribusi Pendapatan Penjualan per Triwulan (2026)')
plt.axis('equal') 

# Simpan SEBELUM menampilkan (agar file benar-benar terbuat)
plt.savefig('grafik_triwulan.png') 
print("\nFile 'grafik_triwulan.png' telah berhasil dibuat.")

# Tampilkan jendela grafik
plt.show()