import os
import fileinput

# Define the directory
dir_path = os.path.dirname(os.path.realpath(__file__))
clauses_dir = os.path.join(dir_path, "clauses")

# Define the lines to prepend and append
line_to_prepend = "<button class=\"print-clause btn btn-default mrgn-tp-sm mrgn-rght-sm pull-right\"><span class=\"glyphicon glyphicon-print\"></span><span class=\"wb-inv\">Print</span></button><div>\n"
line_to_append = "\n</div>"

# Get all text files in the directory
txt_files = [f for f in os.listdir(clauses_dir) if f.endswith('.txt')]

# Prepend and append lines to each text file
for txt_file in txt_files:
    try:
        with fileinput.FileInput(os.path.join(clauses_dir, txt_file), inplace=True, backup='.bak') as file:
            for line in file:
                if fileinput.isfirstline():
                    print(line_to_prepend + line, end='')
                else:
                    print(line, end='')
            print(line_to_append)
    except RuntimeError as e:
        print(f"Error modifying file {txt_file}: {e}")
