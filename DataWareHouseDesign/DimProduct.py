import random
import csv
import pandas as pd

num_rows = int(input("Enter the number of rows: "))
csv_file = input("Enter the name of the CSV file (e.g., 'stores.csv'): ")

# Excel file details
excel_file_path_name = "LookupFile.xlsx"

# Sheet and column names
excel_sheet_name_product = 'Raw Product Names'
product_column_name = 'Product Name'

excel_sheet_name_category = 'Product Categories'
category_column_name = "Category Name"

# Load lookup data from Excel
df = pd.read_excel(excel_file_path_name, sheet_name=excel_sheet_name_product)
df_cat = pd.read_excel(excel_file_path_name, sheet_name=excel_sheet_name_category)

# Open CSV for writing
with open(csv_file, mode='w', newline='') as file:
    writer = csv.writer(file)

    # Header
    header = ['ProductName', 'Category', 'Brand', 'UnitPrice']
    writer.writerow(header)

    # Generate and write each row
    for _ in range(num_rows):
        row = [
            df[product_column_name].sample(n=1).values[0],         # random product name
            df_cat[category_column_name].sample(n=1).values[0],    # random category name
            random.choice(['FakeLuxAura', 'FakeUrbanGlow', 'FakeEtheralEdge', 'FakeVelveVista', 'FakeZenithStyle']),
            random.randint(100, 1000)  # random unit price
        ]
        writer.writerow(row)

        print(row)  # Optional: print the generated row
