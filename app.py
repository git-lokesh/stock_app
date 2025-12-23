import streamlit as st
from utils import *

st.set_page_config(page_title="Stock Forecast Dashboard", layout="wide")

st.title("Stock Price Time Series Dashboard")

data = load_data("data/NSE-TATAGLOBAL.csv")

# ------------------ SIDEBAR ------------------

section = st.sidebar.radio(
    "Select Visualization",
    [
        "Raw Price Visualizations",
        "Stationarity Analysis",
        "Time Series Decomposition",
        "Moving Average Forecast",
        "Auto ARIMA Forecast",
        "SARIMA Forecast",
    ],
)

# ------------------ DASHBOARD ------------------

if section == "Raw Price Visualizations":
    st.header("Price and Volume Trends")
    figs = plot_price_columns(data)
    for fig in figs:
        st.pyplot(fig)

elif section == "Stationarity Analysis":
    st.header("Stationarity Check")
    st.pyplot(plot_stationarity(data["Open"]))
    st.json(adf_test(data["Open"]))

elif section == "Time Series Decomposition":
    st.header("Trend and Seasonality Decomposition")
    st.pyplot(decompose_series(data["Open"]))

elif section == "Moving Average Forecast":
    st.header("Moving Average Model")
    st.pyplot(moving_average_forecast(data))

elif section == "Auto ARIMA Forecast":
    st.header("Auto ARIMA Model")
    st.pyplot(auto_arima_forecast(data))

elif section == "SARIMA Forecast":
    st.header("SARIMA Model")
    st.pyplot(sarima_forecast(data))
