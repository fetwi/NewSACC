import os
import csv
from bs4 import BeautifulSoup

dir_path = os.path.dirname(os.path.realpath(__file__))

# Define the source folder
source_folder = os.path.join(dir_path, "Source")

# Define the output CSV file
output_file =  os.path.join(dir_path, "output.csv")

# Define the headers
headers = ['Effective Date', 'ID', 'H1 Title', 'Language']

# Open the CSV file in write mode
with open(output_file, 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(headers)

    # Iterate over all HTML files in the source folder
    for filename in os.listdir(source_folder):
        if filename.endswith('.html'):
            with open(os.path.join(source_folder, filename), 'r', encoding='utf-8') as html_file:
                soup = BeautifulSoup(html_file, 'html.parser')

                # Extract the required data
                effective_date_tag = soup.find('dt', string=lambda x: x in ['Effective Date', 'Date d\'effet '])
                effective_date = effective_date_tag.find_next_sibling('dd').find('span') if effective_date_tag else None
                effective_date = effective_date.text if effective_date else 'N/A'

                id_tag = soup.find('dt', string='ID')
                id = id_tag.find_next_sibling('dd') if id_tag else None
                id = id.text if id else 'N/A'

                h1_title = soup.find('h1')
                h1_title = h1_title.text if h1_title else 'N/A'
                
                language = soup.find('html')
                language = language['lang'] if language else 'N/A'

                # Write the data to the CSV file
                writer.writerow([effective_date, id, h1_title, language])