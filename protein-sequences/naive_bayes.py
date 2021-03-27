import json
import re
from nltk.tokenize import sent_tokenize, word_tokenize
import spacy

data = None
raw_sentences = {}
sentences = {}
nlp = spacy.load("en_core_web_trf")

with open("/Users/parvinderjit.singh/Desktop/Harvard/CSCI E-599/Patent_Visualization_Project/text-mining-poc/protein-sequences/test_data.json", "r") as read_file:
    data = json.load(read_file)
for patent in data:
    raw_sentences[patent["patentid"]] = []
    raw_sentences[patent["patentid"]] += sent_tokenize(patent['abstract'])
    raw_sentences[patent["patentid"]] += sent_tokenize(patent['claims'])
    raw_sentences[patent["patentid"]] += sent_tokenize(patent['description'])
for k in raw_sentences.keys():
    sentences[k] = []
    for s in raw_sentences[k]:
        if re.search('SEQ ID', s, re.IGNORECASE):
            sentences[k].append(s)
for k in sentences.keys():
    print(k, len(sentences[k]))