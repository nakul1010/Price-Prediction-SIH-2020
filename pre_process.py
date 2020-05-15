import pylab
import calendar
import numpy as np
import pandas as pd
import seaborn as sn
from scipy import stats
from datetime import datetime
import matplotlib.pyplot as plt
import warnings

daily_Data= pd.read_csv("2014_2019.csv")
daily_Data.head(2)
daily_Data.shape

df=daily_Data.copy()
df.columns

df=df.rename(index=str, columns={"sl_no.": "Sl_no", "Min_Price": "Min_Price","Date":"Price_Date","Modal_price":"Modal_Price"})
df.head()
df.columns

df.Price_Date = pd.to_datetime(df.Price_Date, errors='coerce')
df.head()

df=df.sort_values(by='Price_Date')
df.drop_duplicates('Price_Date', inplace = True)
df.head(20)

df.to_csv("pure_cotton.csv", sep=',')