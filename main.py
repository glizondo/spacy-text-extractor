import spacy
import textacy.extract
import redact_text

nlp = spacy.load('en_core_web_sm')


def extract_entities_function(text):
    doc = nlp(text)
    for entity in doc.ents:
        print(f"{entity.text} ({entity.label_})")


def redact_text_function(text):
    print(redact_text.scrub(text))


def extract_facts_function(text, key_word):
    doc = nlp(text)
    statements = textacy.extract.semistructured_statements(doc, entity=key_word, cue="be")
    print(f"Here are the things I know about {key_word}:")
    for statement in statements:
        subject, verb, fact = statement
        print(f" - {fact}")


def extract_noun_chunks_function(text):
    doc = nlp(text)
    noun_chunks = textacy.extract.noun_chunks(doc, min_freq=3)
    noun_chunks = map(str, noun_chunks)
    noun_chunks = map(str.lower, noun_chunks)
    for noun_chunk in set(noun_chunks):
        if len(noun_chunk.split(" ")) > 1:
            print(noun_chunk)


def main_loop():
    while True:
        answer = int(input('\n0: Exit\n1: Extract Entities\n2: Redact Text\n3: Extract Facts\n4: Extract Noun Chunks\n'))
        if answer == 0:
            print("Bye!!")
            break
        print("Enter a text (Type END when you are done entering the text):\n")
        text_lines = []
        while True:
            line = input()
            if line == 'END':
                break
            text_lines.append(line)
        text = " ".join(text_lines)
        print('\n')
        if answer == 1:
            extract_entities_function(text)
        elif answer == 2:
            redact_text_function(text)
        elif answer == 3:
            key_word = input("What is the entity that you want to extract the facts from?\n")
            extract_facts_function(text, key_word)
        elif answer == 4:
            extract_noun_chunks_function(text)
        else:
            return 'Wrong Input'


main_loop()
