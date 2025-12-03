from bs4 import BeautifulSoup


with open("hello.html", "r", encoding = 'utf-8') as f:
    html=f.read()

soup = BeautifulSoup(html,"html.parser")

for script in soup(["script","style"]):
    script.decompose

text = soup.get_text(separator="\n")

with open("html.txt","w",encoding="utf-8") as out:
    out.write(text)

print("HTML ingested succesfully")