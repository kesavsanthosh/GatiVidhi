import docx
import PyPDF2
import nltk
import re

import docx
from collections import Counter
import string


from nltk.corpus import stopwords

nltk.download('stopwords')
# Function to preprocess and tokenize the text
def preprocess_text(text):
    # Remove punctuation and convert to lowercase
    translator = str.maketrans('', '', string.punctuation)
    text = text.translate(translator).lower()

    # Tokenize the text by splitting on whitespace
    tokens = text.split()

    return tokens

# Function to extract important keywords from the Word document

def extract_keywords_from_docx(docx_file, num_keywords=10):
    doc = docx.Document(docx_file)
    text = " ".join(para.text for para in doc.paragraphs)
    words = re.findall(r'\b\w+\b', text.lower())
    stopwords_set = set(stopwords.words("english"))
    keywords = [word for word in words if word not in stopwords_set and word.isalpha()]
    keyword_counter = Counter(keywords)
    return keyword_counter.most_common(num_keywords)



if __name__ == "__main__":
    docx_path = r"C:\Users\Harshenee_CB\Documents\new\out.docx"
    keywords_count = 10
    most_common_keywords = extract_keywords_from_docx(docx_path, keywords_count)
    print("Most common keywords:")
    for keyword, count in most_common_keywords:
        print(f"{keyword}: {count} occurrences")

docx_path=r"C:\Users\Harshenee_CB\Documents\new\out.docx" 
# Extract 10 important keywords from the Word document
important_keywords = extract_keywords_from_docx(docx_path)

# Print the extracted important keywords
print("Important Keywords:")
for idx, keyword in enumerate(important_keywords, start=1):
    print(f"{idx}. {keyword}")



def extract_text_from_mapped_keywords(pdf_path, mapped_keywords):
    extracted_text = []

    with open(pdf_path, 'rb') as pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)

        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            page_text = page.extract_text()
            
            if isinstance(page_text, list):
                page_text = "".join(page_text)

            # Ensure that page_text is a string
            if isinstance(page_text, str):
                # Search for mapped keywords in the page text
                for keyword in mapped_keywords:
                    if keyword.lower() in page_text.lower():
                        # Extract the text around the keyword (adjust the context as needed)
                        start_index = page_text.lower().find(keyword.lower())
                        end_index = start_index + len(keyword)
                        context_text = page_text[max(start_index - 100, 0): min(end_index + 100, len(page_text))]
                        extracted_text.append(context_text)

    return extracted_text

pdf_path=r'C:\Users\Harshenee_CB\Documents\HackerX\mv1.pdf'
extract_text_from_mapped_keywords(pdf_path, important_keywords)


