import random
import csv
from faker import Faker
import pandas as pd

# Initialize Faker
fake = Faker()

# User input
num_rows = int(input("Enter the number of rows: "))
csv_file = input("Enter the name of the CSV file (e.g., 'stores.csv'): ")

# Excel file details
excel_file_path_name = "LookupFile.xlsx"
excel_sheet_name = "Store Name Data"
adjective_column_name = "Adjectives"
noun_column_name = "Nouns"

# Load lookup data from Excel
df = pd.read_excel(excel_file_path_name, sheet_name=excel_sheet_name)

# Open CSV for writing
with open(csv_file, mode='w', newline='') as file:
    writer = csv.writer(file)

    # Header
    header = [
        'StoreName', 'StoreType', 'StoreOpeningDate', 'Address',
        'City', 'State', 'Country', 'Region', 'Manager Name'
    ]
    writer.writerow(header)  # Corrected from csv.writerow

    # Generate and write each row
    for _ in range(num_rows):
        # Random adjective and noun for store name
        random_adjective = df[adjective_column_name].sample(n=1).values[0]
        random_noun = df[noun_column_name].sample(n=1).values[0]
        store_name = f"The {random_adjective} {random_noun}"

        row = [
            store_name,
            random.choice(['Exclusive', 'MBO', 'SMB', 'Outlet Stores',]),
            fake.date(),
            fake.address().replace("\n", " ").replace(","," "),
            fake.city(),
            fake.state(),
            fake.country(),
            random.choice(['North', 'South', 'East', 'West',]),
            fake.first_name()
        ]
        writer.writerow(row)

        print(store_name)  # Optional: Print generated store names to console
