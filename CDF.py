# import libraries and packages

import numpy as np
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import norm

# set print options
pd.set_option("display.max_rows", None)
pd.set_option("display.max_columns", None)

# Specify the stock ticker
ticker = "TSLA"

# specify ticker and get stock price data
data = yf.download(ticker, start = "2020-01-01", end = None)

# create a dataframe
df = pd.DataFrame(data)
df = df.reset_index()

# Round decimals for closing price 
df['Close'] = df['Close'].round(1)

# Extract columns as numpy arrays to get around indexing issues - and then make a new df
array1 = df['Date'].values
array2 = df['Close'].values
df_new = pd.DataFrame({'Column1' : array1}).rename(columns={'Column1' : 'Date'})
df_new['Close'] = array2

# Develop parameters for a CDF and develop a CDF
mean = np.mean(df_new['Close'])
stdev = np.std(df_new['Close'])
cdf = norm.cdf(df['Close'], loc=mean, scale=stdev)

# Develop plots for closing price and cdf - side by side

plt.suptitle('TSLA Closing Price and CDF of Closing Price (Jan 2020 to Jan 2025)', fontsize=12, fontweight='bold')

plt.subplot(1,2,1)
plt.title("Closing Price for each Day \n Data obtained using python from YFinance API", fontsize=10)
sns.lineplot(x='Date', y='Close', data=df_new, linewidth=1)
plt.xlabel("Year", fontsize=10)
plt.ylabel("Price ($)", fontsize=10)

plt.subplot(1,2,2)
plt.title('CDF of TSLA Closing Price each Day \n for the Last Five Years', fontsize=10)
plt.plot(df['Close'], cdf, linewidth=3/4, color='orangered')
plt.xlabel('Price ($)', fontsize=10)
plt.ylabel('CDF', fontsize=10)
plt.xticks(np.arange(0,501,100))
plt.yticks(np.arange(0, 1.01,0.1))
plt.grid(color='gray', linewidth=1/3, linestyle="--")
plt.tight_layout()

# Save output plot
plt.savefig('Output_Plot3.png', dpi=500)





