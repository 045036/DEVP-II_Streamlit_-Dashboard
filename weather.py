import streamlit as st
import pandas as pd
import plotly.express as px

# Load the dataset
weather_data = pd.read_csv('weather.csv')

# Set up Streamlit page
st.title("Weather Data Dashboard")

# Plot 1: Pie Chart for Wind Gust Direction
fig1 = px.pie(weather_data, names='WindGustDir', title='Wind Gust Direction Distribution')

# Plot 2: Trend Line for Maximum Temperature over Time
# Assuming there's a date or time column, replace 'DateColumn' with the actual date column name
# weather_data['DateColumn'] = pd.to_datetime(weather_data['DateColumn'])
# fig2 = px.line(weather_data, x='DateColumn', y='MaxTemp', title='Max Temperature Trend Over Time')

# Plot 3: Bar Chart for Average Maximum Temperature by Wind Gust Direction
avg_temp_by_wind_dir = weather_data.groupby('WindGustDir')['MaxTemp'].mean().reset_index()
fig3 = px.bar(avg_temp_by_wind_dir, x='WindGustDir', y='MaxTemp', 
              title='Average Max Temperature by Wind Gust Direction')

# Plot 4: Box Plot for Humidity
fig4 = px.box(weather_data, y='Humidity3pm', title='Humidity Box Plot')

# Plot 5: Scatter Plot for Temperature vs. Humidity
fig5 = px.scatter(weather_data, x='MaxTemp', y='Humidity3pm', title='Max Temperature vs. Humidity')

# Plot 6: Histogram for Rainfall
fig6 = px.histogram(weather_data, x='Rainfall', title='Rainfall Distribution')

# Layout for side-by-side graphs
col1, col2 = st.columns(2)
col1.plotly_chart(fig1)
col2.plotly_chart(fig3)

col1, col2 = st.columns(2)
col1.plotly_chart(fig4)
col2.plotly_chart(fig5)

col1, col2 = st.columns(2)
col1.plotly_chart(fig6)

# Uncomment and adjust the line plot (fig2) once you confirm the date column in your dataset
# col1, col2 = st.columns(2)
# col1.plotly_chart(fig2)
