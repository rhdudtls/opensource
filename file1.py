import pandas as pd

df = pd.read_csv('hotel_bookings.csv', sep=',')
print(df.groupby(['hotel', 'is_canceled'])['lead_time'].mean())
