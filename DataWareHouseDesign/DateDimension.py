import pandas as pd

#Start and edn date
start_date = '2014-01-01'
end_date = '2024-12-31'
# generate series of date in between
date_range = pd.date_range(start = start_date, end = end_date)
print(date_range)
#Convert date to df

date_dimension = pd.DataFrame(date_range, columns = ['Date'])

# add columns in df

date_dimension['DayofWEeek'] = date_dimension['Date'].dt.dayofweek

date_dimension['Month'] = date_dimension['Date'].dt.month
date_dimension['quarter'] = date_dimension['Date'].dt.quarter
date_dimension['year'] = date_dimension['Date'].dt.year
date_dimension['Isweeknd'] = date_dimension['Date'].dt.dayofweek.isin([5,6])
date_dimension['DateID'] = date_dimension['Date'].dt.strftime('%Y%m%d').astype(int)


print(date_dimension)
#Ew-order column
cols = ['DateID'] + [col for col in date_dimension.columns if col != 'DateID']
date_dimension = date_dimension[cols]
#wxport to csv
print(cols)


date_dimension.to_csv('DimDate.csv', index = False)
