import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from math import ceil
from statsmodels.tsa.stattools import adfuller
from statsmodels.tsa.seasonal import seasonal_decompose
from pmdarima.arima import auto_arima
from statsmodels.tsa.statespace.sarimax import SARIMAX

# ------------------ DATA LOADING ------------------

def load_data(path):
    df = pd.read_csv(path)
    df["Date"] = pd.to_datetime(df["Date"])
    df = df.iloc[::-1]
    df.set_index("Date", inplace=True)
    return df


# ------------------ EDA VISUALS ------------------

def plot_price_columns(df):
    figs = []
    for col in df.columns:
        fig, ax = plt.subplots(figsize=(6, 4))
        ax.plot(df.index, df[col])
        ax.set_title(f"{col} vs Date")
        ax.set_xlabel("Date")
        ax.set_ylabel(col)
        figs.append(fig)
    return figs


# ------------------ STATIONARITY ------------------

def adf_test(series):
    series = np.log(series).diff().dropna()
    result = adfuller(series)
    return {
        "ADF Statistic": result[0],
        "p-value": result[1],
        "lags": result[2],
        "observations": result[3],
        "critical": result[4],
    }


def plot_stationarity(series):
    series = np.log(series).diff().dropna()
    fig, ax = plt.subplots(figsize=(6, 4))
    ax.plot(series, label="Log Differenced")
    ax.plot(series.rolling(12).mean(), label="Rolling Mean")
    ax.plot(series.rolling(12).std(), label="Rolling Std")
    ax.legend()
    ax.set_title("Stationarity Check")
    return fig


# ------------------ DECOMPOSITION ------------------

def decompose_series(series):
    result = seasonal_decompose(series, model="multiplicative", period=30)
    fig = result.plot()
    fig.set_size_inches(8, 5)
    return fig


# ------------------ MOVING AVERAGE ------------------

def moving_average_forecast(df):
    data = np.log(df["Open"])
    split = ceil(len(data) * 0.9)
    train, valid = data[:split], data[split:]

    preds = []
    for i in range(len(valid)):
        preds.append(train[-len(valid):].mean())

    fig, ax = plt.subplots(figsize=(6, 4))
    ax.plot(train, label="Train")
    ax.plot(valid, label="Actual")
    ax.plot(valid.index, preds, label="Prediction")
    ax.set_title("Moving Average Forecast")
    ax.legend()

    return fig


# ------------------ AUTO ARIMA ------------------

def auto_arima_forecast(df):
    data = np.log(df["Open"])
    split = ceil(len(data) * 0.9)
    train, valid = data[:split], data[split:]

    model = auto_arima(train, seasonal=True, trace=False)
    preds = model.predict(n_periods=len(valid))

    fig, ax = plt.subplots(figsize=(6, 4))
    ax.plot(train, label="Train")
    ax.plot(valid, label="Actual")
    ax.plot(valid.index, preds, label="Prediction")
    ax.set_title("Auto ARIMA Forecast")
    ax.legend()

    return fig


# ------------------ SARIMA ------------------

def sarima_forecast(df):
    data = np.log(df["Open"])
    split = ceil(len(data) * 0.9)
    train, valid = data[:split], data[split:]

    model = SARIMAX(train, order=(1,1,1), seasonal_order=(1,1,1,12))
    res = model.fit(disp=False)

    forecast = res.get_forecast(len(valid))
    preds = forecast.predicted_mean

    fig, ax = plt.subplots(figsize=(8, 4))
    ax.plot(train, label="Train")
    ax.plot(valid, label="Actual")
    ax.plot(valid.index, preds, label="Prediction")
    ax.set_title("SARIMA Forecast")
    ax.legend()

    return fig
