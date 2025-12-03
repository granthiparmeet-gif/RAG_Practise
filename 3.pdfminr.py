from pdfminer.high_level import extract_text


text = extract_text("/Users/parmeetsingh/Desktop/RAG_Practise/Train to Pakistan PDF.pdf")

with open("pdfminer_output.txt",'w',encoding="utf-8") as f:
    f.write(text)