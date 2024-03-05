import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# LOAD DATA
@st.cache_data
def load_data():
    data = pd.read_csv("./Bike Sharing Dataset/day.csv")
    return data

data = load_data()

# TITLE DASHBOARD
st.title("Proyek Akhir Dicoding Bike Share")

# SIDEBAR
st.sidebar.image("BikeShare.png", use_column_width=True)
st.sidebar.title("Information:")
st.sidebar.markdown("**• Nama: Ahmad Fahrezy Sanny**")
st.sidebar.markdown("**• Email: [rezy.sanny@gmail.com](rezy.sanny@gmail.com)**")

st.sidebar.title("Dataset Bike Share")
if st.sidebar.checkbox("Show Dataset"):
    st.subheader("Dataset Bike Share")
    st.write(data)

st.sidebar.markdown("[Download Dataset](https://drive.google.com/file/d/1RaBmV6Q6FYWU4HWZs80Suqd7KQC34diQ/view?usp=sharing)")

# VISUALIZATION
# create a layout with two columns
col1, col2 = st.columns(2)

with col1:
    season_mapping = {1: "spring", 2: "summer", 3: "fall", 4: "winter"}
    data["season_label"] = data["season"].map(season_mapping)
    season_count = data.groupby("season_label")["cnt"].sum().reset_index()
    fig_season_count = px.bar(season_count, x="season_label", y="cnt", title="Jumlah Penyewaan Sepeda Pada Tiap Musim")
    st.plotly_chart(fig_season_count, use_container_width=True, height=400, width=600)

with col2:
    weather_count = data.groupby("weathersit")["cnt"].sum().reset_index()
    fig_weather_count = px.bar(weather_count, x="weathersit", y="cnt", title="Jumlah Penyeewaan Sepeda Pada Tiap Cuaca")
    st.plotly_chart(fig_weather_count, use_container_width=True, height=400, width=800)

fig_wind_speed_chart = px.scatter(data, x="windspeed", y="cnt", title="Pengaruh Kecepatan Angin Pada Penyewaan Sepeda")
st.plotly_chart(fig_wind_speed_chart)

fig_temp_chart = px.scatter(data, x="temp", y="cnt", title="Pengaruh Suhu Pada Penyewaan Sepeda")
st.plotly_chart(fig_temp_chart, use_container_width=True, height=400, width=800)

filtered_data = data[data["workingday"] == 1]

fig_new = go.Figure()

fig_new.add_trace(go.Bar(
    x=filtered_data["weekday"],
    y=filtered_data["registered"],
    name="Registered",
))

fig_new.add_trace(go.Bar(
    x=filtered_data["weekday"],
    y=filtered_data["casual"],
    name="Casual",
))

fig_new.update_layout(
    title="Jumlah Sewa Sepeda Casual dan Terdaftar pada Hari Kerja",
    xaxis_title="Hari Kerja",
    yaxis_title="Jumlah Sewa Sepeda",
    barmode='group'
)

st.plotly_chart(fig_new)
