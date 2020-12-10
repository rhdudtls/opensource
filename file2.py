import pandas as pd

df = pd.read_csv('hotel_bookings.csv', sep=',')
print(df.groupby('arrival_date_month')['number'].nunique())
