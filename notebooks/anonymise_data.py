from faker import Faker
import csv
import os
import pandas as pd
from random import shuffle
fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        first_name = fake.first_name()
        last_name = fake.last_name()
        address = fake.address().replace("\n", " ")
        date_of_birth = fake.date_of_birth(minimum_age=18, maximum_age=90).strftime("%d-%m-%Y")
        data.append([first_name, last_name, address, date_of_birth])
    return data

def write_to_csv(data, filename):
    with open(filename, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(['first_name', 'last_name', 'address', 'date_of_birth'])
        csv_writer.writerows(data)

def word_scrambler(word):
    word = list(word)
    shuffle(word)
    return ''.join(word).lower().capitalize()

if __name__ == "__main__":
    num_records = 10  # Change this to the desired number of records
    data_folder = os.path.join('..', 'data')
    original_filename = os.path.join(data_folder, "generated_data.csv")
    anonymized_filename = os.path.join(data_folder, "anonymized_data.csv")

    # Create 'data' folder if it doesn't exist
    os.makedirs(data_folder, exist_ok=True)

    original_data = generate_fake_data(num_records)
    #print(original_data)
    write_to_csv(original_data, original_filename)

    # Read the generated CSV file into a pandas DataFrame
    df = pd.read_csv(original_filename)
    # Anonymize First_name,Last_Name and Address Field
    df['first_name'] = df.first_name.apply(word_scrambler)
    df['last_name'] = df.last_name.apply(word_scrambler)
    df['address'] = df.address.apply(word_scrambler)

    # Keep only the required columns in the anonymized DataFrame
    #anonymized_df = df[['first_name', 'last_name', 'address', 'date_of_birth']]
    df.to_csv(anonymized_filename, index=False)

    print(f"Anonymized data saved to '{anonymized_filename}'")