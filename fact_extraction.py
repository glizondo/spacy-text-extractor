import spacy
import textacy.extract
from pathlib import Path

# Load the large English NLP model
nlp = spacy.load('en_core_web_sm')

# The text we want to examine
# text = Path("Portland.txt").read_text()
text = open("Portland.txt", encoding="utf8").read()

# Parse the document with spaCy
doc = nlp(text)

# Extract semi-structured statements
#original book statement
#statements = textacy.extract.semistructured_statements(doc, "London")

#for accuarte calls check documentation page https://textacy.readthedocs.io/en/0.11.0/api_reference/extract.html#textacy.extract.triples.semistructured_statements
statements = textacy.extract.semistructured_statements(doc, entity="Portland", cue="be")


# Print the results
print("Here are the things I know about Portland:")

for statement in statements:
    subject, verb, fact = statement
    print(f" - {fact}")

