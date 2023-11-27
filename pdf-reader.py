from PyPDF2 import PdfReader

def pdf_to_text(pdf_path, txt_path):
    # Open the PDF file
    with open(pdf_path, 'rb') as pdf_file:
        # Create a PDF reader object
        pdf_reader = PdfReader(pdf_file)

        # Initialize an empty string to store the text
        text = ""

        # Iterate through all pages in the PDF
        for page_num in range(len(pdf_reader.pages)):
            # Get the page
            page = pdf_reader.pages[page_num]

            # Extract text from the page
            text += page.extract_text()

    # Write the extracted text to a new text file
    with open(txt_path, 'w', encoding='utf-8') as txt_file:
        txt_file.write(text)

if __name__ == "__main__":
    # Replace 'input.pdf' with the path to your PDF file
    pdf_path = 'arquivo.pdf'

    # Replace 'output.txt' with the desired path for the new text file
    txt_path = 'output.txt'

    # Call the function to convert PDF to text and save to a new file
    pdf_to_text(pdf_path, txt_path)

    print(f"Conversion complete. Text saved to {txt_path}")
