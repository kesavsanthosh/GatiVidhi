import nltk

# Download the missing resources using the NLTK Downloader
nltk.download('punkt')

from nltk.corpus import wordnet
from nltk.tokenize import word_tokenize

def get_synonyms(word):
    synonyms = set()
    for syn in wordnet.synsets(word):
        for lemma in syn.lemmas():
            synonyms.add(lemma.name())
    return list(synonyms)

def paraphrase_sentence(sentence):
    tokens = word_tokenize(sentence)
    paraphrased_tokens = []

    for token in tokens:
        synonyms = get_synonyms(token)
        if synonyms:
            paraphrased_tokens.append(synonyms[0])  # Use the first synonym as a simple paraphrase
        else:
            paraphrased_tokens.append(token)

    return ' '.join(paraphrased_tokens)

# Example usage
input_sentence = "The quick brown fox jumps over the lazy dog."
paraphrased_sentence = paraphrase_sentence(input_sentence)
print("Original Sentence:", input_sentence)
print("Paraphrased Sentence:", paraphrased_sentence)

import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

def negate_sentence(sentence):
    # Tokenize the sentence
    tokens = word_tokenize(sentence)
    
    # POS tag the tokens
    tagged_tokens = pos_tag(tokens)
    
    # List of negation words
    negation_words = ['not', 'no', 'never', 'nobody', 'nowhere', 'neither', 'nor', 'none', 'doesn\'t', 'do', 'cannot']
    
    # Rewrite the sentence by adding negation words
    negated_tokens = []
    for i, (word, pos) in enumerate(tagged_tokens):
        if pos.startswith('VB'):  # Verbs
            # Handle subject-verb agreement for third person singular
            if i > 0 and tagged_tokens[i - 1][1] in ['NN', 'NNS']:
                word = word + 's'
            if word.lower() in ['does', 'do', 'can']:
                negated_tokens.append(word + ' not')
            else:
                negated_tokens.append('not ' + word)
        elif pos.startswith('RB') and word.lower() not in negation_words:  # Adverbs except negation words
            negated_tokens.append('not ' + word)
        else:
            negated_tokens.append(word)
    
    # Reconstruct the negated sentence
    negated_sentence = ' '.join(negated_tokens)
    
    return negated_sentence

# Example usage:
sentence = "He does his work diligently and cannot ignore his responsibilities."
negated_sentence = negate_sentence(sentence)
print("Original sentence:", sentence)
print("Negated sentence:", negated_sentence)




