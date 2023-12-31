from transformers import AutoTokenizer
from collections import Counter

def count_unique_tokens(text_file, top_n=30):
    tokenizer = AutoTokenizer.from_pretrained("dmis-lab/biobert-base-cased-v1.2")

    with open(text_file, 'r') as file:
        text = file.read()

    tokens = tokenizer.tokenize(text)

    token_counts = Counter(tokens)

    top_tokens = token_counts.most_common(top_n)

    return top_tokens

text_file = 'output/test.txt'

top_30_tokens = count_unique_tokens(text_file, top_n=30)

for token, count in top_30_tokens:
    print(f"Token: {token}, Count: {count}")