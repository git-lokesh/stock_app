# Stock Price Time Series Analysis and Forecasting

This project is a Streamlit-based web dashboard for analyzing and forecasting stock prices using classical time series techniques. The application performs exploratory data analysis, stationarity testing, time series decomposition, and forecasting using multiple statistical models.

The dataset contains historical stock price data from NSE (TATA Global), including Open, High, Low, Close prices and trading volume.

---

## Project Structure

```text
stock_app/
├── app.py
├── utils.py
├── requirements.txt
├── README.md
└── data/
    └── NSE-TATAGLOBAL.csv
```

---

## Features

### 1. Raw Price Visualizations
- Time series plots of Open, High, Low, Close prices
- Trading volume and turnover trends

### 2. Stationarity Analysis
- Log transformation and differencing
- Rolling mean and rolling standard deviation
- Augmented Dickey-Fuller (ADF) test results

### 3. Time Series Decomposition
- Trend component
- Seasonal component
- Residual component

### 4. Forecasting Models
- Moving Average forecasting
- Auto ARIMA forecasting
- SARIMA forecasting

Each analysis is separated into clearly labeled sections in the Streamlit dashboard and can be selected using the sidebar.

---

## Dataset Description

The dataset contains the following columns:

- Date  
- Open  
- High  
- Low  
- Last  
- Close  
- Total Trade Quantity  
- Turnover (Lacs)

The `Date` column is converted to datetime format and used as the index for all time series modeling and analysis.

---

## Installation

1. Clone the repository

```bash
git clone <repository-url>
cd stock_app
```

2. Install dependencies

```bash
pip install -r requirements.txt
```

---

## Running the Application

Start the Streamlit application using:

```bash
streamlit run app.py
```

Open the local URL shown in the terminal to access the dashboard.

---

## Models Used

- Moving Average  
- Auto ARIMA (pmdarima)  
- SARIMA (statsmodels)  

All models operate on log-transformed data, and predictions are visualized alongside actual values for comparison.

---

## Technologies Used

- Python  
- Streamlit  
- Pandas  
- NumPy  
- Matplotlib  
- Statsmodels  
- pmdarima  

---

## Notes

- This project focuses on classical statistical time series models rather than deep learning approaches.
- The codebase is modular, with analytical logic separated from the Streamlit UI.





