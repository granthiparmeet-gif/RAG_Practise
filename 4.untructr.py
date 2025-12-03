from unstructured.partition.auto import partition

elements = partition(filename="/Users/parmeetsingh/Desktop/RAG_Practise/Train to Pakistan PDF.pdf")

with open("untrucrd_output.txt", "w", encoding="utf-8") as f:
    for element in elements:
        text = element.text or ""
        f.write(text + "\n")

print("completed")
