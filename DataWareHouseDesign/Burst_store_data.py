# Every Night store will send sale file of the day --> We Load them overnight using a batch process
import pandas as pd
import numpy as np
import os
Dateid ='20240728'
#directory = "
for i in  range(1,101):
    num_rows = np.random.randint(100,1000)
    data = {
        'DateID':[Dateid] * num_rows,
        'ProductID':np.random.randint(1,1001,size=num_rows),
        'StoreID':[i]*num_rows,
        'CustomerID':np.random.randint(1,1001,size=num_rows),
        'OrderedAmount':np.random.randint(100,1001,size=num_rows)
        }

    df = pd.DataFrame(data)
    discount_perc = np.random.uniform(0.02,0.15,size=num_rows)
    shipping_cost = np.random.uniform(0.05,0.15,size=num_rows)

    #Calculate olumn
    df['DiscountAmount'] = df['OrderedAmount'] *discount_perc
    df['ShippingCost'] = df['OrderedAmount'] * shipping_cost
    df['TotalAmount'] = df['OrderedAmount'] -(df['DiscountAmount']+df['ShippingCost'])
    #Add these in df:
    print(df)
    file_name = f'Store_{i}_{Dateid}.csv'
    #if file exists remove:
    if os.path.exists(file_name):
        os.remove(file_path)
    df.to_csv(file_name, index=False)





