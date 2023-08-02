import docx
import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.probability import FreqDist
from nltk.tokenize import PunktSentenceTokenizer
from heapq import nlargest

nltk.download('punkt')
nltk.download('stopwords')



def extract_text_from_word(docx_path):
    try:
        doc = docx.Document(docx_path)
        full_text = []
        for paragraph in doc.paragraphs:
            full_text.append(paragraph.text)
        return '\n'.join(full_text)
    except Exception as e:
        print(f"Error while extracting text: {e}")
        return ""
    
def clean_text(text):
    # Remove unnecessary whitespaces and newlines
    text = re.sub(r'\s+', ' ', text).strip()
    text = text.replace(',', '')
    # Convert text to lowercase
    text = text.lower()
    return text

def preprocess_word(docx_path):
    try:
        with open(docx_path, 'rb'):
            pass
        # Step 1: Extract text from the Word document
        text = extract_text_from_word(docx_path)

        # Step 2: Clean the text
        cleaned_text = clean_text(text)

        # Step 3: Additional preprocessing steps if required

        return cleaned_text
    except FileNotFoundError:
        print("File not found.")
        return ""
    except Exception as e:
        print(f"Error: {e}")
        return ""

# Call the preprocess_word function
preprocessed_text = preprocess_word("C:\\Users\\Harshenee_CB\\Documents\\HackerX\\ws.docx")
#print(preprocessed_text)


def summarize_text(text, num_sentences=3):
    # Tokenize the text into sentences
    sentences = sent_tokenize(text)

    # Calculate the frequency of each word
    word_freq = FreqDist(word_tokenize(text))

    # Remove common stop words from word frequency
    stop_words = set(stopwords.words('english'))
    word_freq = {word: freq for word, freq in word_freq.items() if word.lower() not in stop_words}

    # Calculate the importance score for each sentence
    sentence_scores = {}
    for sentence in sentences:
        for word in word_tokenize(sentence.lower()):
            if word in word_freq:
                if sentence not in sentence_scores:
                    sentence_scores[sentence] = word_freq[word]
                else:
                    sentence_scores[sentence] += word_freq[word]

    # Get the top N sentences with highest scores
    summary_sentences = nlargest(num_sentences, sentence_scores, key=sentence_scores.get)

    return ' '.join(summary_sentences)

# Call the preprocess_word function
preprocessed_text = preprocess_word("C:\\Users\\Harshenee_CB\\Documents\\HackerX\\ws.docx")

# Summarize the text with important keywords
summary = summarize_text(preprocessed_text, num_sentences=3)
print("Summary:")
print(summary)



