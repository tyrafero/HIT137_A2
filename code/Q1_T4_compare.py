import spacy
import torch
from transformers import AutoTokenizer, AutoModel

# Load the spaCy model
nlp_sci_sm = spacy.load('en_core_web_sm')

# Load the BioBERT model
model_name = "dmis-lab/biobert-base-cased-v1.1"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModel.from_pretrained(model_name)

# Read the text file
file_path = "output/test.txt"
with open(file_path, 'r', encoding='utf-8') as file:
    text = file.read()

# Truncate the text if it exceeds the maximum sequence length
max_sequence_length = 512
truncated_text = text[:max_sequence_length]

# Extract disease entities using en_core_sci_sm
doc_sci_sm = nlp_sci_sm(truncated_text)
diseases_sci_sm = [ent.text for ent in doc_sci_sm.ents if ent.label_ == 'DISEASE']

# Encode the truncated text
inputs = tokenizer.encode_plus(truncated_text, return_tensors='pt')
input_ids = inputs['input_ids']
attention_mask = inputs['attention_mask']

# Adjust the input_ids and attention_mask if they exceed the maximum sequence length
if input_ids.shape[1] > max_sequence_length:
    input_ids = input_ids[:, :max_sequence_length]
    attention_mask = attention_mask[:, :max_sequence_length]

# Pass the adjusted inputs to the model
outputs = model(input_ids, attention_mask=attention_mask)
predicted_labels = torch.argmax(outputs.last_hidden_state, dim=-1)[0]
predicted_entities = [tokenizer.decode(input_ids[0][i]) for i, label in enumerate(predicted_labels) if label.item() == 1]

# Filter out disease and drug entities from BioBERT predictions
diseases_biobert = [entity for entity in predicted_entities if entity in diseases_sci_sm]
drugs_biobert = [entity for entity in predicted_entities if entity not in diseases_sci_sm]

# Compare the results
total_entities_sci_sm = len(diseases_sci_sm)
total_entities_biobert = len(predicted_entities)
common_entities = set(diseases_sci_sm) & set(predicted_entities)

print("Total disease entities detected by en_core_sci_sm:", total_entities_sci_sm)
print("Total disease and drug entities detected by BioBERT:", total_entities_biobert)
print("Number of common entities detected by both models:", len(common_entities))
print("Most common disease and drug entities:", common_entities)