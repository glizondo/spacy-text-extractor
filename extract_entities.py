import spacy

# Load the large English NLP model
nlp = spacy.load('en_core_web_sm')

# The text we want to examine
text = """London is the capital and most populous city of England and
the United Kingdom.  Standing on the River Thames in the south east
of the island of Great Britain, London has been a major settlement
for two millennia. It was founded by the Romans, who named it Londinium.
"""

# text = ("Portland, Oregon’s boosters highlight miles of bike lanes and light rail, an urban growth boundary that "
#         "prevents sprawl and protects farmland, walkable 20-minute neighborhoods, year- round farmers markets, "
#         "and an increasingly complex network of green infrastructure. Scholars and the popular press alike portray "
#         "Portland as a leader in sustainability and livability (Berke and Conroy, 2000; Dyckhoff, 2012; Portney, "
#         "2005; SustainLane, 2008). Echoing the “win-win-win” discourse that typifies mainstream definitions of "
#         "sustainability, municipal greening efforts lie at the center of the city’s economic development strategy. A "
#         "2008 proclamation by Tom Potter, Mayor of Portland from 2005 to 2009, invokes such a promise: Portland’s "
#         "support of local farmers and farmers markets, its explosion of green buildings and commitment to renewable "
#         "energy, and its emphasis on mass transportation, including light rail and bicycles, shows that a city can "
#         "not only be kind to the earth, but also flourish economically and grow by being green (SustainLane, "
#         "2008). In step with a global trend (While, Jonas, and Gibbs, 2004), Portland’s sustainability prowess has "
#         "translated to a viable development approach, and policymakers and planners from around the world look to "
#         "emulate the Portland model (Slavin and Snyder, 2011).")

# Parse the text with spaCy. This runs the entire pipeline.
doc = nlp(text)

# 'doc' now contains a parsed version of text. We can use it to do anything we want!
# For example, this will print out all the named entities that were detected:
for entity in doc.ents:
    print(f"{entity.text} ({entity.label_})")
