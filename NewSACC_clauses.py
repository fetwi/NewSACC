import os
from bs4 import BeautifulSoup

dir_path = os.path.dirname(os.path.realpath(__file__))

# Define the source folder
source_dir = os.path.join(dir_path, "Source")
target_dir = os.path.join(dir_path, "Clauses")


html_files = [f for f in os.listdir(source_dir) if f.endswith('.html')]

for html_file in html_files:
    with open(os.path.join(source_dir, html_file), 'r', encoding='utf-8') as file:
        soup = BeautifulSoup(file, 'html.parser')
        
    language = soup.find('html')
    language = language['lang'] if language else 'N/A'
    effective_date_tag = soup.find('dt', string=lambda x: x in ['Effective Date', 'Date d\'effet '])
    effective_date = effective_date_tag.find_next_sibling('dd').find('span') if effective_date_tag else None
    effective_date = effective_date.text if effective_date else 'N/A'
    id_tag = soup.find('dt', string='ID')
    id = id_tag.find_next_sibling('dd') if id_tag else None
    id = id.text if id else 'N/A'
    
    output_filename = f'{language}~{effective_date}~{id}.txt'

    if language.lower() == "en":
        see_revision_history = "See revision history."
    elif language.lower() == "fr":
        see_revision_history = "Voir l'historique des révisions."

    sacc_item_text_heading = soup.find(id='sacc-item-text-heading')

    if sacc_item_text_heading is None:
        content = see_revision_history
    else:
        sibling_tags = []
        for sibling in sacc_item_text_heading.find_next_siblings():
            if sibling.name != 'abbr':  # Skip 'abbr' tags
                sibling_tags.append(str(sibling))  # Convert tag to string to get minified HTML
        content = ' '.join(sibling_tags)
        if not content:
            content = see_revision_history

    if not content.startswith('<pre>') and not content.endswith('</pre>'):
        content = '<pre>' + content + '</pre>'
    
    with open(os.path.join(target_dir, output_filename), 'w', encoding='utf-8') as file:
        file.write(content)