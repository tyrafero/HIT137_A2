import csv
from collections import Counter

def count_words_in_text(text_file, csv_file):
    print("Initializing .. \n")
    with open(text_file, 'r') as file:
        print("Reading Text File ..")
        text = file.read()
    words = text.split()
    word_counts = Counter(words)
    top_30_words = word_counts.most_common(30)
    with open(csv_file, 'w', newline='') as file:
        print("Analyzing words ..")
        writer = csv.writer(file)
        writer.writerow(['Word', 'Count'])
        writer.writerows(top_30_words)

text_file = 'output/output.txt'
csv_file = 'output/word_counts.csv'
count_words_in_text(text_file, csv_file)