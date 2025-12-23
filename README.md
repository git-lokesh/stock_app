# Stock Price Time Series Analysis and Forecasting

This project is a Streamlit-based web dashboard for analyzing and forecasting stock prices using classical time series techniques. The application performs exploratory data analysis, stationarity testing, time series decomposition, and forecasting using multiple models.

The dataset used contains historical stock price data from NSE (TATA Global), including Open, High, Low, Close prices and trading volume.

---

## Project Structure

stock_app/
│
├── app.py                # Streamlit dashboard
├── utils.py              # Data processing, models, and visualizations
├── data/
│   └── NSE-TATAGLOBAL.csv
├── requirements.txt
└── README.md

---

## Features

The dashboard provides the following visualizations and analyses:

1. Raw Price Visualizations  
   - Time series plots of Open, High, Low, Close, Volume, and Turnover  

2. Stationarity Analysis  
   - Log transformation and differencing  
   - Rolling mean and rolling standard deviation  
   - Augmented Dickey-Fuller (ADF) test results  

3. Time Series Decomposition  
   - Trend component  
   - Seasonal component  
   - Residual component  

4. Forecasting Models  
   - Moving Average forecasting  
   - Auto ARIMA forecasting  
   - SARIMA forecasting  

Each analysis is separated into clearly labeled sections in the Streamlit dashboard.

---

## Dataset Description

Columns in the dataset:

- Date  
- Open  
- High  
- Low  
- Last  
- Close  
- Total Trade Quantity  
- Turnover (Lacs)  

The Date column is converted to datetime format and used as the index for time series modeling.

---

## Installation

1. Clone the repository

   git clone <repository-url>
   cd stock_app

2. Create and activate a virtual environment (optional but recommended)

   python -m venv venv  
   source venv/bin/activate   (Linux/Mac)  
   venv\Scripts\activate      (Windows)

3. Install dependencies

   pip install -r requirements.txt

---

## Running the Application

Start the Streamlit app using the command below:

   streamlit run app.py

Once started, open the local URL shown in the terminal to access the dashboard in your browser.

---

## Models Used

- Moving Average  
- Auto ARIMA (pmdarima)  
- SARIMA (statsmodels)  

All models are trained on log-transformed data, and predictions are visualized alongside actual values.

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

- This project focuses on classical statistical time series models, not deep learning.
- The code is modular, with all logic separated from the Streamlit interface.
- The application is suitable for academic demonstrations, portfolio projects, and interviews.

---

## License

This project is provided for educational and learning purposes.
