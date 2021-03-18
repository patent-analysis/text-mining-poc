from pdfminer.pdfparser import PDFParser, PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LAParams, LTTextBox, LTTextLine
import re
from nltk.tokenize import sent_tokenize, word_tokenize
import spacy

nlp = spacy.load('en_core_web_sm')
US9175093 = '../../data/raquel_documents/Pfizer/US9175093.pdf'

def extract_text(path):
    pdf_obj = open(path)
    parser = PDFParser(pdf_obj)
    doc = PDFDocument()
    parser.set_document(doc)
    doc.set_parser(parser)

    doc.initialize('')
    rsrcmgr = PDFResourceManager()
    laparams = LAParams()

    #laparams.char_margin = 1.0
    #laparams.word_margin = 1.0
    device = PDFPageAggregator(rsrcmgr, laparams=laparams)
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    extracted_text = ''

    for page in doc.get_pages():
        interpreter.process_page(page)
        layout = device.get_result()
        for lt_obj in layout:
            if isinstance(lt_obj, LTTextBox) or isinstance(lt_obj, LTTextLine):
                extracted_text += lt_obj.get_text()

    raw_text = extracted_text.encode("utf-8")
    clean_text = re.sub(rb'\n', rb' ', raw_text)
    udata = clean_text.decode("utf-8")

    return udata

def get_word_list(path):
    return word_tokenize(extract_text(path))

def get_sentence_list(path):
    return sent_tokenize(extract_text(path))

def extract_epitope_seq_sentences(path):
    sent_tokens = get_sentence_list(path)
    epitope_seq_sent = []
    for sent in sent_tokens:
        if 'SEQ' in sent and 'epitope' in sent:
            epitope_seq_sent.append(sent)
    return epitope_seq_sent

def extract_entities(sentence):
    doc = nlp(sentence)
    for ent in doc.ents:
        print(ent.text, ent.label_)

def __main__():
    base_path = '/Users/parvinderjit.singh/Desktop/Harvard/CSCI E-599/data/raquel_documents/'
    add_path = 'Pfizer/US9175093.pdf'
    extract_entities(base_path + add_path)

