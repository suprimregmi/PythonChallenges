import pandas as pd
import numpy as np


num_rows = int(input("Enter the mnumber of rosws for orders: "))

#generate the series of data between 2014-2024

date_series = np.random.choice(np.arange(np.datetime64('2014-01-01'),np.datetime64('2024-07-28')),size = num_rows)
#print(date_series)

#converting int

formatted_rows = pd.to_datetime(date_series).strftime('%Y%m%d')
#print(formatted_rows)

data = {
    'DateID':formatted_rows,
    'ProductID':np.random.randint(1,1001,size=num_rows),
    'StoreID':np.random.randint(1,101,size = num_rows),
    'CustomerID':np.random.randint(1,1001,size=num_rows),
    'OrderedAmount':np.random.randint(100,1001,size=num_rows)
    }

#print(data)

df = pd.DataFrame(data)
#print(df)

discount_perc = np.random.uniform(0.02,0.15,size=num_rows)
shipping_cost = np.random.uniform(0.05,0.15,size=num_rows)

#Calculate olumn

df['DiscountAmount'] = df['OrderedAmount'] *discount_perc
df['ShippingCost'] = df['OrderedAmount'] * shipping_cost
df['TotalAmount'] = df['OrderedAmount'] -(df['DiscountAmount']+df['ShippingCost'])
#Add these in df:
print(df)


df.to_csv('factorders.csv',index=False)



