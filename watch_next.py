# from __future__ import unicode_literals
# import spacy

# nlp = spacy.load("en_core_web_md")

# myfile = open("movies.txt").read()
# NlpRead = nlp(myfile)

# sentence_to_compare = "Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery and trained as a gladiator"

# model_sentences = nlp(sentence_to_compare)

# for sentence in myfile:
#     similarity = nlp(sentence).similarity(model_sentences)
#     print(sentence + "-" + str(similarity))



import spacy
import numpy as np

nlp = spacy.load("en_core_web_md")
tokens = nlp(u'Hulk Superman Batman dragon elf dance musical handsome romance war soldier')

for token in tokens:
    print(token.text, token.has_vector, token.vector_norm, token.is_oov)

labels = [a.text for a in tokens]
print(labels)

M = np.zeros((len(tokens), len(tokens)))
for idx, token1 in enumerate(tokens):
    for idy, token2 in enumerate(tokens):
        M[idx, idy] = token1.similarity(token2)



doc = nlp("Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery and trained as a gladiator")

properNouns = [token.text for token in doc if token.pos_ =='PROPN']
commonNouns = [token.text for token in doc if token.pos_ =='NOUN']
print(properNouns)
# ['Hulk', 'Earth', 'Illuminati', 'Hulk', 'Hulk', 'Hulk', 'Sakaar']
print(commonNouns)
# ['world', 'shuttle', 'space', 'planet', 'peace', 'land', 'planet', 'slavery',

