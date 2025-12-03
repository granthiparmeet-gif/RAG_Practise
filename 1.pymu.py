import fitz

pdf = fitz.open("sample_table_20rows.pdf")

text = ""
for page in pdf:
    text = text + page.get_text()

with open("output4.txt", "w", encoding="utf-8") as f:
    f.write(text)

print("Completed")
