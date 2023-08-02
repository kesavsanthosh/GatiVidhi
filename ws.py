import fitz  # PyMuPDF
import pytesseract
from PIL import Image

def extract_text_from_scanned_pdf(pdf_path):
    text = ""
    try:
        pdf_document = fitz.open(pdf_path)
        for page_num in range(pdf_document.page_count):
            page = pdf_document.load_page(page_num)
            image_list = page.get_images(full=True)

            for img_info in image_list:
                xref = img_info[0]
                base_image = pdf_document.extract_image(xref)
                img_data = base_image["image"]
                image = Image.open(img_data)
                text += pytesseract.image_to_string(image)

        pdf_document.close()
    except Exception as e:
        print(f"Error while extracting text from scanned PDF: {e}")
    return text

def convert_scanned_pdf_to_normal_pdf(scanned_pdf_path, output_pdf_path):
    text_from_scanned_pdf = extract_text_from_scanned_pdf(scanned_pdf_path)
    
    try:
        pdf_document = fitz.open()
        pdf_document.insert_page(0, width=200, height=200)
        page = pdf_document[0]
        page.insert_text((10, 10), text_from_scanned_pdf)
        pdf_document.save(output_pdf_path)
        pdf_document.close()
    except Exception as e:
        print(f"Error while converting scanned PDF to normal PDF: {e}")

# Replace 'path/to/your/scanned_pdf.pdf' with the actual path to your scanned PDF
scanned_pdf_path = r'C:\Users\Harshenee_CB\Documents\new\petition.pdf'

# Replace 'path/to/your/output_pdf.pdf' with the desired output path for the normal PDF
output_pdf_path = r'C:\Users\Harshenee_CB\Documents\new\petition1'

# Convert the scanned PDF to a normal PDF
convert_scanned_pdf_to_normal_pdf(scanned_pdf_path, output_pdf_path)

print(f"Scanned PDF converted to normal PDF and saved to: {output_pdf_path}")






