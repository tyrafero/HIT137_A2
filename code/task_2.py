import spacy
from spacy.language import Language
import pathlib

file_name = "output/test.txt"
nlp = spacy.load("en_core_web_sm")
text = pathlib.Path(file_name).read_text(encoding="utf-8")
nlp.max_length = len(text)

about_doc = nlp(text)
sentences = list(about_doc.sents)

for sentence in sentences:
    print(f"{sentence[:11]}...")

for token in about_doc:
    print(f"{str(token.text_with_ws):22}"
        f"{str(token.is_alpha):15}"
          )

# @Language.component("set_custom_boundaries")

# def set_custom_boundaries(doc):
#     for token in doc[:-1]:
#         if token.text == "...":
#             doc[token.i + 1].is_sent_start = True

#     return doc
# print(set_custom_boundaries(about_doc)  ) 

# introduction_doc = nlp(
#     text
# )

# print(type(introduction_doc))

# print([token.text for token in introduction_doc])

