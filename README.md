# Fake Data Generator and Anonymizer

This script generates fake data for first name, last name, address, and date of birth using the Faker library. It then anonymizes the data by applying a word scrambler to first names, last names, and addresses.


## Introduction

This script generates synthetic data and anonymizes it for testing or other purposes. It utilizes the Faker library to create realistic fake data and a word scrambler for anonymization.

## Prerequisites

Ensure you have the following prerequisites installed:

- Python (version 3.x.x)
- Faker library (`pip install faker`)
- Other dependencies (if any)

## Installation

Clone the repository and install dependencies:

```bash
git clone https://github.com/tinkle21/anonymise-data.git
cd anonymise-data
pip install -r requirements.txt

## Usage
#Directly Running in Codespaces Jupyter
Open the Jupyter notebook in your Codespaces environment.
Open the anonymise_data.ipynb notebook.
Execute the cells in the notebook to generate and anonymize data.

#Running as a Script
Generate fake data, anonymize, and save the results:

python anonymise_data.py



## File Structure

.
├── data/
│   ├── generated_data.csv
│   └── anonymized_data.csv
├── anonymise_data.py
├── anonymise_data.ipynb
├── README.md
├── requirements.txt
└── other_files...

## Result :

Result save under data folder 
1) sample data generated through faker library store in as filename generated_data.csv
2) anonymised data generated through scarambling word stored in anonymized_data.csv 

