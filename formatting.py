import docx

def format_first_two_lines(docx_file):
    # Load the Word document
    doc = docx.Document(docx_file)

    # Get the first two paragraphs
    first_two_paragraphs = doc.paragraphs[:1]

    # Iterate through the first two paragraphs and apply formatting
    for paragraph in first_two_paragraphs:
        # Set the entire paragraph to bold
        for run in paragraph.runs:
            run.bold = True

        # Set the entire paragraph text to uppercase
        paragraph.text = paragraph.text.upper()

    # Save the modified document
    doc.save("formatted_document.docx")

if __name__ == "__main__":
    input_docx = r"C:\Users\Harshenee_CB\Documents\new\out.docx"  # Replace with the path to your input Word document
    format_first_two_lines(input_docx)
    print("First two lines made bold and uppercase, and saved to 'formatted_document.docx'.")
