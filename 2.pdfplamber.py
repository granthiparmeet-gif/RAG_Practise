import pdfplumber

pdf = pdfplumber.open('/Users/parmeetsingh/Desktop/RAG_Practise/sample_table_20rows.pdf')

text = ""
for z in pdf.pages:
    text = text + z.extract_text()

with open("pdf_plumber_output_1.txt","w",encoding = "utf-8") as f:
    f.write(text)

print("Done with PDF Plumber")