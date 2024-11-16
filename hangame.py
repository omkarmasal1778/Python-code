import nltk
nltk.download('punkt')  # Download necessary dataset
from nltk.tokenize import word_tokenize

text = "NLTK is a powerful Python library."
tokens = word_tokenize(text)
print(tokens)
