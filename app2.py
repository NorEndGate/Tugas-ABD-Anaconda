import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os  

# Konfigurasi halaman
st.set_page_config(page_title="Visualisasi Mitra Bank Sampah", page_icon="♻️", layout="wide")

# Judul & deskripsi
st.title("Dashboard Lokasi Mitra Bank Sampah ♻️")
st.write("Visualisasi data mitra Bank Sampah dengan berbagai jenis grafik dan peta.")

# Data dummy 10 lokasi mitra
data = pd.DataFrame({
    "Nama Mitra": [
        "Bank Sampah Melati",
        "Bank Sampah Kenanga",
        "Bank Sampah Bougenville",
        "Bank Sampah Anggrek",
        "Bank Sampah Sakura",
        "Bank Sampah Teratai",
        "Bank Sampah Mawar",
        "Bank Sampah Flamboyan",
        "Bank Sampah Kamboja",
        "Bank Sampah Sedap Malam"
    ],
    "Kota": [
        "Jakarta", "Surabaya", "Bandung", "Medan", "Makassar",
        "Yogyakarta", "Denpasar", "Samarinda", "Balikpapan", "Malang"
    ],
    "Total Sampah (kg)": [1200, 950, 800, 700, 650, 500, 450, 400, 350, 300],
    "Jumlah Nasabah": [150, 130, 110, 100, 95, 80, 75, 70, 65, 60],
    "lat": [-6.2, -7.25, -6.9, 3.6, -5.14, -7.8, -8.65, -0.5, -1.27, -7.98],
    "lon": [106.8, 112.75, 107.6, 98.67, 119.42, 110.37, 115.22, 117.15, 116.83, 112.63]
})

st.subheader("📋 Data Mitra Bank Sampah")
st.dataframe(data)

st.markdown("---")

# Dropdown untuk memilih jenis visualisasi
tipe_chart = st.selectbox(
    "Pilih jenis visualisasi:",
    ["Bar Chart", "Line Chart", "Area Chart", "Pie Chart", "Map"]
)

# Pilih metrik yang mau divisualisasikan (untuk selain map)
if tipe_chart != "Map":
    metrik = st.radio(
        "Pilih metrik yang ingin divisualisasikan:",
        ["Total Sampah (kg)", "Jumlah Nasabah"],
        horizontal=True
    )

    data_plot = data.set_index("Nama Mitra")[[metrik]]

# Tampilkan visualisasi berdasarkan pilihan
if tipe_chart == "Bar Chart":
    st.subheader(f"📊 Bar Chart - {metrik}")
    st.bar_chart(data_plot)

elif tipe_chart == "Line Chart":
    st.subheader(f"📈 Line Chart - {metrik}")
    st.line_chart(data_plot)

elif tipe_chart == "Area Chart":
    st.subheader(f"📉 Area Chart - {metrik}")
    st.area_chart(data_plot)

elif tipe_chart == "Pie Chart":
    st.subheader(f"🧁 Pie Chart - {metrik}")
    fig, ax = plt.subplots()
    ax.pie(
        data[metrik],
        labels=data["Nama Mitra"],
        autopct="%1.1f%%",
        startangle=90
    )
    ax.axis("equal")
    st.pyplot(fig)

elif tipe_chart == "Map":
    st.subheader("🗺️ Peta Lokasi Mitra Bank Sampah")
    st.map(data[["lat", "lon"]])

st.subheader("🖼️ Detail Mitra & Foto Lokasi")

# Mapping nama mitra ke file gambar (nanti kamu isi file-nya)
# Saran: buat folder `images` di sebelah main.py, lalu taruh gambar di sana.
image_files = {
    "Bank Sampah Melati": "BS1.jpg",
    "Bank Sampah Kenanga": "BS2.jpg",
    "Bank Sampah Bougenville": "BS3.jpg",
    "Bank Sampah Anggrek": "BS4.jpg",
    "Bank Sampah Sakura": "BS5.jpg",
    "Bank Sampah Teratai": "BS6.jpg",
    "Bank Sampah Mawar": "BS7.jpg",
    "Bank Sampah Flamboyan": "BS8.jpg",
    "Bank Sampah Kamboja": "BS9.jpg",
    "Bank Sampah Sedap Malam": "BS10.jpg"
}

mitra_pilihan = st.selectbox("Pilih mitra untuk melihat detail & foto:", data["Nama Mitra"])

row = data[data["Nama Mitra"] == mitra_pilihan].iloc[0]

col1, col2 = st.columns([1, 1.5])

with col1:
    st.markdown(f"**Nama Mitra:** {row['Nama Mitra']}")
    st.markdown(f"**Kota:** {row['Kota']}")
    st.markdown(f"**Total Sampah:** {row['Total Sampah (kg)']} kg")
    st.markdown(f"**Jumlah Nasabah:** {row['Jumlah Nasabah']} orang")

with col2:
    img_path = image_files.get(mitra_pilihan, None)
    if img_path and os.path.exists(img_path):
        st.image(img_path, caption=f"Lokasi {row['Nama Mitra']} - {row['Kota']}", use_container_width=True)
    else:
        st.info("Belum ada gambar untuk mitra ini. Silakan tambahkan file gambar ke folder `images`.")

st.markdown("---")


# Penjelasan singkat
st.markdown("""
### ℹ️ Penjelasan
- **Total Sampah (kg)**: Perkiraan jumlah sampah yang berhasil dikumpulkan oleh setiap mitra Bank Sampah.  
- **Jumlah Nasabah**: Perkiraan jumlah nasabah aktif yang menyetorkan sampah ke masing-masing mitra.  
- **Map**: Menampilkan titik lokasi mitra Bank Sampah berdasarkan koordinat lat dan lon.
""")
