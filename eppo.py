from helper.html import HTML
from helper.files import PDF, TEXT
import os

os.system("clear")
url = "https://gd.eppo.int"

def main():
	html = HTML.new(url+"/taxon")
	print(filterLinks(html), "\n")
	print("\n\n".join([str(u) for u in getUserInstructions()]), "\n")
	print(apiRequest("BANANA", "xyz"))
		
def filterLinks(html):
	data = ""
	for l in HTML.links(html):
		href = l["href"]
		text = HTML.text(l)
		if "PP" in text or "PM" in text:
			data = "\n".join([data, text, href])
	return data
	
def getUserInstructions():
	text = []
	pdf = PDF.link("https://gd.eppo.int/media/files/general_user-guide.pdf")
	for page in pdf.pages:
		t = TEXT.readline(page.extract_text())
		text.append(t)
	return(text)

def apiRequest(eppoCode, authToken):
	return HTML.get(
		f"https://data.eppo.int/api/rest/1.0/taxon/{eppoCode}?",
		{"authtoken": authToken}
	)

if __name__ == "__main__":
	main()
