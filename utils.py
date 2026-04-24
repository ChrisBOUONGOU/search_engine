import re

STOP_WORDS = {
    "i", "you", "the", "a", "an", "we", "they", "he",
    "she", "my", "mine", "myself", "us", "our", "ours", "ourselves",
    "your", "yours", "yourself", "yourselves", "him", "his", "himself",
    "her", "hers", "herself", "it", "its", "it's", "itself", "them", 
    "their", "theirs", "themself", "themselves", "one", "ones", "thou",
    "thee", "thy", "thine", "thyself"
}

def clean_text(text):
    clean = text.lower()
    clean = re.sub(r"[^\w\s]", "", text)
    words = clean.split() #To separate
    words = [w for w in words if w not in STOP_WORDS] #if the word is not in the list
    return words