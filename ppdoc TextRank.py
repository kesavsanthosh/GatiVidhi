import docx
import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer
import networkx as nx

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

def textrank_summarize(text, num_sentences=3):
    # Tokenize the text into sentences
    sentences = sent_tokenize(text)

    # Preprocess the sentences and remove stopwords
    stop_words = set(stopwords.words('english'))
    preprocessed_sentences = [
        ' '.join([word for word in sent.split() if word not in stop_words])
        for sent in sentences
    ]

    # Create a graph using sentence similarity (TextRank algorithm)
    graph = nx.Graph()
    for i, sent1 in enumerate(preprocessed_sentences):
        for j, sent2 in enumerate(preprocessed_sentences):
            if i == j:
                continue
            similarity = calculate_sentence_similarity(sent1, sent2)
            graph.add_edge(i, j, weight=similarity)

    # Apply PageRank algorithm on the graph to get sentence ranks
    ranks = nx.pagerank(graph)

    # Get the top N sentences with highest ranks
    ranked_sentences = sorted(ranks, key=ranks.get, reverse=True)[:num_sentences]

    # Form the summary using the top-ranked sentences
    summary = [sentences[idx] for idx in ranked_sentences]

    return ' '.join(summary)

def calculate_sentence_similarity(sent1, sent2):
    # Implement your sentence similarity calculation here
    # For example, you can use cosine similarity or other metrics
    # Make sure the similarity value is between 0 and 1
    # Return the similarity value
    return 0.0 

# Call the preprocess_word function
docx_path = "C:\\Users\\Harshenee_CB\\Documents\\HackerX\\ws.docx"
preprocessed_text = preprocess_word(docx_path)

# Generate the TextRank summary
summary = textrank_summarize(preprocessed_text, num_sentences=100)
print("TextRank Summary:")
print(summary)

