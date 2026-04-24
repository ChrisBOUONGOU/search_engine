import json
from utils import clean_text

def load_index():
    with open("index.json", "r", encoding="utf-8") as f:
        return json.load(f)
    
def levenshtein(a, b):
    if len(a) < len(b):
        return levenshtein(b, a)

    if len(b) == 0:
        return len(a)

    previous_row = range(len(b) + 1)
    for i, c1 in enumerate(a):
        current_row = [i + 1]
        for j, c2 in enumerate(b):
            insertions = previous_row[j + 1] + 1
            deletions = current_row[j] + 1
            substitutions = previous_row[j] + (c1 != c2)
            current_row.append(min(insertions, deletions, substitutions))
        previous_row = current_row

    return previous_row[-1]

def fuzzy_match(word, index_words):
    matches = []
    for w in index_words:
        if levenshtein(word, w) <= 1:
            matches.append(w)
    return matches


def search(query, page=1, per_page=5):
    index = load_index()
    words = clean_text(query)

    scores = {}

    for word in words:
        matched_words = fuzzy_match(word, index.keys())

        for mw in matched_words:
            for doc, score in index[mw].items():
                scores[doc] = scores.get(doc, 0) + score

    results = sorted(scores.items(), key=lambda x: x[1], reverse=True)

    # pagination
    start = (page - 1) * per_page
    end = start + per_page

    return results[start:end]