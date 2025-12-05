from PIL import Image
import pytesseract

img =Image.open("/Users/parmeetsingh/Desktop/RAG_Practise/scanned_image.jpeg")

text = pytesseract.image_to_string(img)

with open("ocr_output.txt", "w", encoding="utf-8") as f:
    f.write(text)

print("Operation completed")