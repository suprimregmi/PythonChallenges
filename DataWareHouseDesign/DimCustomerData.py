import random
import csv
from faker import Faker

fake = Faker()
num_rows = int(input("Enter the num of rows to generate " ))


with open('fake_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    
    # Optional: Write header row
    writer.writerow([
        "First Name", "Last Name", "Gender", "Date",
        "Email", "Phone", "Address", "City", "State",
        "Postcode", "Country", "Rating"
    ])
    
    for _ in range(num_rows):
        row = [
            fake.first_name(),
            fake.last_name(),
            random.choice(['M', 'F', 'Others', 'Not Specified']),
            fake.date(),
            fake.email(),
            fake.phone_number(),
            fake.address().replace(",", " ").replace("\n", " "),
            fake.city(),
            fake.state(),
            fake.postcode(),
            fake.country(),
            random.randint(1, 5)
        ]
        writer.writerow(row)
