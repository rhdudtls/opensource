import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('hotel_bookings.csv', sep=',')
hotel = df.groupby('arrival_date_month')['number'].nunique()
print(hotel)
hotel.plot()