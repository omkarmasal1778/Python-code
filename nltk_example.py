import nltk
nltk.download('all')        # Download tokenizer dataset

from nltk import word_tokenize

# Sample sentence
sentence = "The quick brown fox jumps over the lazy dog."

# Tokenize the sentence into words
tokens = word_tokenize(sentence)

# Perform POS tagging
# tagged_words = pos_tag(tokens)

# Output the tagged words
print(tokens)