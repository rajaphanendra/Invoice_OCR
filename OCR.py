from pdf2image import convert_from_path
import pytesseract

from PIL import Image
Image.MAX_IMAGE_PIXELS = 1000000000

# Path to the PDF file
pdf_file_path = "C:\\Users\\rajap\\Documents\\OCR_Project\\sample-2.pdf"

# Convert PDF to images
pages = convert_from_path(pdf_file_path, 1200)  # Adjust DPI as needed

# Initialize pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract\tesseract.exe'

# Extract text from each page
text = ""
for page in pages:
    text += pytesseract.image_to_string(page)

# Print or do further processing with the extracted text
print(text)

output_file_path = "C:\\Users\\rajap\\Documents\\OCR_Project\\output_text.txt"

# Open the file in write mode and save the text
with open(output_file_path, 'w', encoding='utf-8') as file:
    file.write(text)

print(f"Text successfully saved to {output_file_path}")