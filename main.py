# pip install streamlit fbprophet yfinance plotly
import streamlit as st
from datetime import date
import emoji
import os

import yfinance as yf
from fbprophet import Prophet
from fbprophet.plot import plot_plotly
from plotly import graph_objs as go

import logging
from time import gmtime, strftime

START = "2015-01-01"
TODAY = date.today().strftime("%Y-%m-%d")

emoj = emoji.emojize(':blue_heart:')
emojj = emoji.emojize(':winking_face:')

st.title('Stock '+ emoj +' Prediction ' + emojj  )
#====================================================================================================
# stocks = ('MDB', 'ADXS', 'ZOM', 'AEI', 'CRDL', 'SNDL', 'ZOM', 'XELA', 'CRDL', 'FAMI', 'TSLA', 'AMWL')

def convert_to_tuple(list):
    return tuple(list)

def Convert_to_list(string):
    li = list(string.split())
    return li

t = open("/local_stock_names.txt", "r")
reading_file = t.read()

#converting string to list
lis = Convert_to_list(reading_file)

#can add custom stock names to list
lis2 = ['SPY','DOGE-USD', 'BSV-USD', 'BCH-USD', 'ETC-USD', 'AMP-USD', 'RLY-USD', 'CHZ-USD', 'CTSI-USD'] #list

combined_list = lis + lis2

lists= list(set(combined_list))
# stocks = ('MDB', 'ADXS', 'ZOM', 'AEI', 'CRDL', 'SNDL', 'ZOM', 'XELA', 'CRDL', 'FAMI', 'TSLA', 'AMWL')

#converting list to tuple
stocks = convert_to_tuple(lists)

# stocks = tup

#====================================================================================================
selected_stock = st.selectbox('Select dataset for prediction', sorted(stocks))

n_years = st.slider('Years of prediction:', 1, 4)
period = n_years * 365


@st.cache
def load_data(ticker):
    data = yf.download(ticker, START, TODAY)
    data.reset_index(inplace=True)
    return data

	
data_load_state = st.text('Loading data...')
data = load_data(selected_stock)
data_load_state.text('Loading data... done!')

st.subheader('Raw data')
st.write(data.tail())

# Plot raw data
def plot_raw_data():
	fig = go.Figure()
	fig.add_trace(go.Scatter(x=data['Date'], y=data['Open'], name="stock_open"))
	fig.add_trace(go.Scatter(x=data['Date'], y=data['Close'], name="stock_close"))
	fig.layout.update(title_text='Time Series data with Rangeslider', xaxis_rangeslider_visible=True)
	st.plotly_chart(fig)
	
plot_raw_data()

# Predict forecast with Prophet.
df_train = data[['Date','Close']]
df_train = df_train.rename(columns={"Date": "ds", "Close": "y"})

m = Prophet()
m.fit(df_train)
future = m.make_future_dataframe(periods=period)
forecast = m.predict(future)
#================================================================================
print(type(forecast))

# Show and plot forecast
st.subheader('Forecast data')
st.write(forecast.tail())
    
st.write(f'Forecast plot for {n_years} years')
fig1 = plot_plotly(m, forecast)
st.plotly_chart(fig1)

st.write("Forecast components")
fig2 = m.plot_components(forecast)
st.write(fig2)


# log_dir_path = '/local'
# filename= os.path.join(log_dir_path, 'robin_py_script.log')

# print (filename)


# logger = logging.getLogger(__name__)
# logger.setLevel(logging.INFO)

# file_handler = logging.FileHandler(filename)
# file_handler.setLevel(logging.INFO)

# fmt='%(asctime)s - %(levelname)s -%(message)s'
# current_time = strftime("%a, %d %b %Y %I:%M:%S +0000")
# print(current_time)
# file_handler.setFormatter(logging.Formatter(fmt, current_time))
# logger.addHandler(file_handler)

# def do_logging():
# 	logger.info('last run')

# do_logging()

