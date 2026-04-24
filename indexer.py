import os
import json
import math
import glob
from utils import clean_text

def build_index(folder_path):
    inverted_index = {}
    doc_count = 0
    documents = {}
    fichiers = glob.glob(os.path.join(folder_path, '*.txt'))

    for filename in fichiers:
        if filename.endswith(".txt"):
            doc_count += 1

            with open(filename, "r", encoding="utf-8") as f:
                words = clean_text(f.read())

            documents[filename] = words

            word_freq = {}
            for word in words:
                word_freq[word] = word_freq.get(word, 0) + 1

            for word, freq in word_freq.items():
                if word not in inverted_index:
                    inverted_index[word] = {}

                inverted_index[word][filename] = freq
        
        tfidf_index = {}

    for word, docs in inverted_index.items():
        df = len(docs)
        idf = math.log(doc_count / (1 + df))

        tfidf_index[word] = {}
        for doc, tf in docs.items():
            tfidf = tf * idf
            tfidf_index[word][doc] = tfidf

    
    with open("index.json", "w", encoding="utf-8") as f:
        json.dump(tfidf_index, f, indent=4)

    return tfidf_index
