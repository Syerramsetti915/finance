# Stock Prediction Application

## Overview
This repository contains a Streamlit web application that predicts stock prices using historical data from Yahoo Finance. Utilizing the powerful time-series forecasting algorithm from Facebook's Prophet, users can select from a variety of stocks and cryptocurrencies to view past performance and future predictions.

![Stock Prediction App Screenshot](https://github.com/Syerramsetti915/finance/blob/main/Images/1.png)
![Overview of Stock Prediction App](https://github.com/Syerramsetti915/finance/blob/main/Images/2_2.png)
## Features
- Selection of various stocks and cryptocurrencies for analysis.
- Interactive time-series plots with a rangeslider for examining historical data.
- Forecasting feature to predict future stock prices for a user-defined period (1 to 4 years).
- Visualization of forecast data and components including trend, weekly, and yearly seasonality.

![Feature Interactive Plots](https://github.com/Syerramsetti915/finance/blob/main/Images/3.png)
![Overview of Stock Prediction App](https://github.com/Syerramsetti915/finance/blob/main/Images/2.png)

## Installation

To run this application on your local machine, you need to have Python installed. If you don't have Python installed, you can download it from [python.org](https://www.python.org/downloads/).

After installing Python, you can clone this repository and install the required dependencies.

```bash
git clone https://github.com/your-username/stock-prediction-app.git
cd stock-prediction-app
pip install -r requirements.txt
```

## Running the Application
To start the application, run the following command in your terminal:

```bash
streamlit run main.py
```
The application will start and you can view it in your web browser at http://localhost:8501.



## Usage
Select a stock or cryptocurrency from the dropdown menu.
Choose the number of years you would like to predict forward.
View the raw historical data, the interactive plot, and the prediction results.

Explore the forecast components to gain insights into the model's behavior.
