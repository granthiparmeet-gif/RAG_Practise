from docx import Document

doc = Document("/Users/parmeetsingh/Desktop/RAG_Practise/sample.docx")

text = ""

for para in doc.paragraphs:
    text += para.text + "\n"

with open("output_docx.txt","w", encoding="utf-8") as f:
    f.write(text)

print("Operation Completed")