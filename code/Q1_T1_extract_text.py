import os
import csv

def extract_text_from_csv(csv_folder, output_file):
    output_text = ""
    for filename in os.listdir(csv_folder):
        if filename.endswith('.csv'):
            with open(os.path.join(csv_folder, filename), 'r') as file:
                data = file.read().split('\n')

            for x in range(1, len(data)):
                row = data[x].split(',')
                for column in row:
                    output_text += column + "\n"

    with open(output_file, 'w') as output_file:
        output_file.write(output_text)

csv_folder = 'csv'
output_file = 'output/output.txt'

extract_text_from_csv(csv_folder, output_file)