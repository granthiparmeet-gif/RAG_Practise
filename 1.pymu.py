import fitz

pdf = fitz.open("Train to Pakistan PDF.pdf")

text = ""
for page in pdf:
    text = text + page.get_text()

with open("output4.txt", "w", encoding="utf-8") as f:
    f.write(text)

print("Completed")
