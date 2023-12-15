import spacy
import pathlib

file_name = "output/test.txt"
nlp = spacy.load("en_core_web_sm")
text = pathlib.Path(file_name).read_text(encoding="utf-8")
nlp.max_length = len(text)

about_doc = nlp(text)
sentences = list(about_doc.sents)

for sentence in sentences:
    print(f"{sentence[:10]}...")

# introduction_doc = nlp(
#     text
# )

# print(type(introduction_doc))

# print([token.text for token in introduction_doc])

