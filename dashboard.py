import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

st.set_page_config(page_title="Bike Sharing Dashboard", layout="wide")

def load_data():
    df = pd.read_csv("main_data.csv")
    df['dteday'] = pd.to_datetime(df['dteday'])
    return df

day_df = load_data()

st.sidebar.header("Filter Data")
try:
    start_date, end_date = st.sidebar.date_input(
        "Rentang Waktu",
        [day_df['dteday'].min(), day_df['dteday'].max()],
        min_value=day_df['dteday'].min(),
        max_value=day_df['dteday'].max()
    )
except ValueError:
    st.error("Pilih rentang waktu yang valid")
    st.stop()

main_df = day_df[(day_df['dteday'] >= pd.to_datetime(start_date)) & 
                 (day_df['dteday'] <= pd.to_datetime(end_date))]

st.title("Bike Sharing Dashboard")
st.markdown("---")

col1, col2, col3 = st.columns(3)
with col1:
    avg_total = int(main_df['cnt'].mean()) if not main_df.empty else 0
    st.metric("Rata-rata Penyewaan", value=f"{avg_total:,}")
with col2:
    avg_reg = int(main_df['registered'].mean()) if not main_df.empty else 0
    st.metric("Rata-rata Registered", value=f"{avg_reg:,}")
with col3:
    avg_cas = int(main_df['casual'].mean()) if not main_df.empty else 0
    st.metric("Rata-rata Casual", value=f"{avg_cas:,}")

st.markdown("---")

st.subheader("1. Proporsi Pengguna (%)")
total_casual = main_df['casual'].sum()
total_registered = main_df['registered'].sum()

col_l, col_m, col_r = st.columns([1, 1, 1])
with col_m:
    fig1, ax1 = plt.subplots(figsize=(4, 4))
    ax1.pie(
        [total_casual, total_registered], 
        labels=['Casual', 'Registered'], 
        autopct='%1.1f%%', 
        colors=['#72BCD4', '#D3D3D3'],
        startangle=90,
        explode=(0.1, 0)
    )
    st.pyplot(fig1)

st.markdown("---")

st.subheader("2. Faktor yang Mempengaruhi Permintaan Ekstrem")
main_df['kategori_suhu'] = pd.cut(
    main_df['temp'] * 41 if main_df['temp'].max() <= 1 else main_df['temp'], 
    bins=[0, 10, 20, 30, 50], 
    labels=['Dingin', 'Sejuk', 'Hangat', 'Panas']
)

data_plots = [
    main_df.groupby('weathersit')['cnt'].mean().sort_values(ascending=False),
    main_df.groupby('kategori_suhu', observed=True)['cnt'].mean(),
    main_df.groupby('weekday')['cnt'].mean().reindex(['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'])
]
titles = ['Kondisi Cuaca', 'Kelompok Suhu', 'Hari dalam Seminggu']

fig2, ax2 = plt.subplots(1, 3, figsize=(20, 6))
for i, data in enumerate(data_plots):
    data = data.dropna()
    colors = ['#72BCD4' if (val == data.max()) else '#D3D3D3' for val in data]
    data.plot(kind='bar', color=colors, ax=ax2[i], rot=45 if i==2 else 0)
    ax2[i].set_title(f"Per {titles[i]}", fontsize=15)
    ax2[i].set_xlabel(None)
st.pyplot(fig2)

st.markdown("---")

st.subheader("3. Rata-rata Penyewaan: Registered vs Casual")
day_type_avg = main_df.groupby('day_type')[['casual', 'registered']].mean().reindex(['Workingday', 'Weekend', 'Holiday']).reset_index()

fig3, ax3 = plt.subplots(figsize=(12, 5))
sns.lineplot(data=day_type_avg, x='day_type', y='casual', marker='o', label='Casual', color='#72BCD4', linewidth=4)
sns.lineplot(data=day_type_avg, x='day_type', y='registered', marker='o', label='Registered', color='#D3D3D3', linewidth=4)
ax3.set_ylabel("Rata-rata Penyewaan")
ax3.set_xlabel(None)
ax3.grid(axis='y', linestyle='--', alpha=0.5)
st.pyplot(fig3)

st.markdown("---")

st.subheader("4. Komposisi Pengguna Berdasarkan Kategori Hari")
day_types = ['Workingday', 'Weekend', 'Holiday']
fig4, ax4 = plt.subplots(1, 3, figsize=(18, 6))

for i, dtype in enumerate(day_types):
    filtered_data = main_df[main_df['day_type'] == dtype]
    if not filtered_data.empty:
        sums = [filtered_data['casual'].sum(), filtered_data['registered'].sum()]
        ax4[i].pie(sums, labels=['Casual', 'Registered'], autopct='%1.1f%%', colors=['#72BCD4', '#D3D3D3'], startangle=90)
        ax4[i].set_title(dtype, fontsize=14)
    else:
        ax4[i].text(0.5, 0.5, f"No Data\n{dtype}", ha='center', va='center')

st.pyplot(fig4)

st.caption("Copyright © Sharing Bike - 2026")