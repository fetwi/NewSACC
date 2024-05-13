from bs4 import BeautifulSoup
import os
import codecs

dir_path = os.path.dirname(os.path.realpath(__file__))

source = os.path.join(dir_path, 'enContent.html')

# Open the HTML file and parse it
with open(source, 'r') as f:
    soup = BeautifulSoup(f, 'html.parser')

# Find all summary tags
summary_tags = soup.find_all('summary')

# For each summary tag
for tag in summary_tags:
    # Get the data-url attribute value
    data_url = tag['data-url']
    # Construct the corresponding .txt file path
    txt_file_path = os.path.join('clauses', data_url)
    # Open the .txt file and read its content as HTML
    with open(txt_file_path, 'r', encoding='utf-8') as txt_file:
        content = BeautifulSoup(txt_file.read(), 'html.parser')
    # Append the content after the summary tag
    tag.insert_after(content)

# Save the modified HTML back to a file in UTF-8 encoding
with codecs.open('new_enContent.html', 'w', 'utf-8') as f:
    f.write(str(soup))