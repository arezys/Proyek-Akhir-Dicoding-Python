import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Load data
df_day = pd.read_csv('./Bike Sharing Dataset/day.csv')

# Set page title
st.title('Bike Sharing Analysis Dashboard')

# Sidebar untuk filter data
st.sidebar.title('Filter Data')
season_filter = st.sidebar.selectbox('Select Season', options=df_day['season'].unique())
weather_filter = st.sidebar.selectbox('Select Weather', options=df_day['weathersit'].unique())

# Filter data based on sidebar selection
filtered_data = df_day[(df_day['season'] == season_filter) & (df_day['weathersit'] == weather_filter)]

# Show correlation heatmap
st.subheader('Correlation between Numeric Variables')
correlation_matrix = filtered_data.corr()
st.plotly_chart(px.imshow(correlation_matrix))

# Show histograms for numeric variables
st.subheader('Distribution of Numeric Variables')
numeric_cols = ['temp', 'atemp', 'hum', 'windspeed', 'casual', 'registered', 'cnt']
for col in numeric_cols:
    st.plotly_chart(px.histogram(filtered_data, x=col, title=f'Distribution of {col}'))

# Show boxplots for categorical variables
st.subheader('Boxplots for Categorical Variables')
boxplot_cols = ['season', 'holiday', 'workingday', 'weathersit']
for col in boxplot_cols:
    fig = px.box(filtered_data, x=col, y='cnt', title=f'Boxplot of {col} vs. Count')
    st.plotly_chart(fig)

# Show scatter plot for temperature vs count
st.subheader('Scatter Plot: Temperature vs Count')
scatter_fig = px.scatter(filtered_data, x='temp', y='cnt', title='Scatter Plot: Temperature vs Count')
st.plotly_chart(scatter_fig)

# Show bar chart for casual and registered bike rentals on working days
st.subheader('Bike Rentals on Working Days')
working_day_data = df_day[df_day["workingday"] == 1]
fig = go.Figure()
fig.add_trace(go.Bar(
    x=working_day_data["weekday"],
    y=working_day_data["registered"],
    name="Registered",
    marker_color='rgb(102, 0, 204)'
))
fig.add_trace(go.Bar(
    x=working_day_data["weekday"],
    y=working_day_data["casual"],
    name="Casual",
    marker_color='rgb(255, 128, 0)'
))
fig.update_layout(
    title="Bike Rentals on Working Days",
    xaxis_title="Weekday",
    yaxis_title="Count",
    barmode='group'
)
st.plotly_chart(fig)

# Show bar chart for bike rentals based on weather conditions
st.subheader('Bike Rentals based on Weather Conditions')
weather_bar_fig = px.bar(filtered_data, x="weathersit", y="cnt", title="Bike Rentals based on Weather Conditions")
weather_bar_fig.update_xaxes(title="Weather Condition (weathersit)")
weather_bar_fig.update_yaxes(title="Count")
st.plotly_chart(weather_bar_fig)
