import docx
import fitz
import pytesseract
from PIL import Image
import io

def ocr_image(image):
    return pytesseract.image_to_string(image, lang='eng')

def scanned_pdf_to_word(pdf_path, output_path):
    try:
        # Create a new Word document
        doc = docx.Document()

        # Open the scanned PDF file using PyMuPDF (fitz)
        with fitz.open(pdf_path) as pdf_document:
            # Get the number of pages in the PDF
            num_pages = pdf_document.page_count

            # Process each page
            for page_num in range(num_pages):
                page = pdf_document[page_num]

                # Render the page as an image
                image = page.get_pixmap()
                img = Image.frombytes("RGB", [image.width, image.height], image.samples)

                # Perform OCR on the image to extract text
                text = ocr_image(img)

                # Split the text into paragraphs based on double line breaks
                paragraphs = text.split('\n\n')

                # Add each paragraph as a new paragraph in the Word document
                for paragraph in paragraphs:
                    doc.add_paragraph(paragraph)

                # Add a page break after each page to maintain page separation
                if page_num < num_pages - 1:
                    doc.add_page_break()

        # Save the Word document to the specified output path
        doc.save(output_path)

        print(f"Scanned PDF converted to Word and saved to: {output_path}")
    except Exception as e:
        print(f"Error while converting the scanned PDF: {e}")

# Replace 'path/to/your/scanned_document.pdf' with the actual path of your scanned PDF
pdf_path = 'C:\\Users\\Harshenee_CB\\Documents\\HackerX\\pet.pdf'

# Replace 'path/to/your/output/document.docx' with the desired output path for the Word document
output_path = 'C:\\Users\\Harshenee_CB\\Documents\\HackerX\\pet.docx'

scanned_pdf_to_word(pdf_path, output_path)

import os
import win32com.client as win32

def convert_docx_to_pdf(docx_path, pdf_path):
    try:
        # Create an instance of the Word application
        word_app = win32.Dispatch("Word.Application")
        word_app.Visible = False

        # Open the Word document
        doc = word_app.Documents.Open(os.path.abspath(docx_path))

        # Save the document as PDF
        doc.SaveAs(pdf_path, FileFormat=17)  # FileFormat 17 is for PDF

        # Close the Word document and the application
        doc.Close()
        word_app.Quit()

        print(f"Conversion successful. PDF saved to: {pdf_path}")
    except Exception as e:
        print(f"Error while converting the Word document to PDF: {e}")

# Replace 'path/to/your/document.docx' with the actual path of your Word document
docx_path = 'C:\\Users\\Harshenee_CB\\Documents\\HackerX\\pet.docx'

# Replace 'path/to/your/output/document.pdf' with the desired output path for the PDF
pdf_path = 'C:\\Users\\Harshenee_CB\\Documents\\HackerX\\pet1.pdf'

# Convert the Word document to PDF
convert_docx_to_pdf(docx_path, pdf_path)

import PyPDF2

def extract_paragraphs_with_keyword(pdf_path, keyword):
    paragraphs = []
    search_phrase = ' '.join(keywords).lower()
    
    try:
        # Open the PDF file
        with open(pdf_path, 'rb') as pdf_file:
            pdf_reader = PyPDF2.PdfReader(pdf_file)
            
            # Read each page in the PDF
            for page_num in range(len(pdf_reader.pages)):
                page = pdf_reader.pages[page_num]
                
                # Extract the text from the page
                page_text = page.extract_text()
                
                # Split the text into paragraphs
                page_paragraphs = page_text.split('\n\n')
                
                # Check each paragraph for the keyword
                for paragraph in page_paragraphs:
                    if any(keyword.lower() in paragraph.lower() for keyword in keywords):
                        paragraphs.append(paragraph.strip())
    
    except Exception as e:
        print(f"Error while processing the PDF: {e}")
    
    return paragraphs

# Replace 'path/to/your/pdf_file.pdf' with the actual path to your PDF file
pdf_path = 'C:\\Users\\Harshenee_CB\\Documents\\HackerX\\pet1.pdf'

# Replace 'your_keyword' with the specific keyword you want to search for
keywords = ['Applicant','submit']

# Extract paragraphs containing the keyword
result_paragraphs = extract_paragraphs_with_keyword(pdf_path, keywords)

# Print the extracted paragraphs
for idx, paragraph in enumerate(result_paragraphs, start=1):
    print(f"Paragraph {idx}: {paragraph}")

from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

def create_paragraphs_pdf(output_pdf, extracted_text):
    doc = SimpleDocTemplate(output_pdf, pagesize=letter)
    Story = []

    styles = getSampleStyleSheet()
    paragraph_style = styles['Normal']

    # Split the extracted text into paragraphs and create Paragraph objects
    for paragraph in extracted_text.split('\n\n'):
        p = Paragraph(paragraph, paragraph_style)
        Story.append(p)
        Story.append(Spacer(1, 12))  # Add spacer between paragraphs

    doc.build(Story)

# Replace 'path/to/output/extracted_paragraphs.pdf' with the desired output path for the PDF
output_pdf = 'C:\\Users\\Harshenee_CB\\Documents\\HackerX\\pet2.pdf'

# Create a PDF file with the extracted paragraphs
create_paragraphs_pdf(output_pdf, result_paragraphs)

print(f"PDF with extracted paragraphs created and saved to: {output_pdf}")

