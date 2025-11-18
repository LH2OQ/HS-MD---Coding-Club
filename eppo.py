from helper.html import HTML
from helper.files import PDF, TEXT
import os

os.system("clear")
url = "https://gd.eppo.int"

def main():
	root = HTML.new(url+"/taxon")
	for l in HTML.links(root):
		href = l["href"]
		text = HTML.text(l)
		for i in range(1, 4):
			if "PP" + str(i) in text:
				process(text, href)
		for i in range(1, 11):
			if "PM" + str(i) in text:
				process(text, href)
	pdf = userInstructions()

def process(text, href):
	print(text, "\n", href, "\n")
	
def userInstructions():
	text = []
	pdf = PDF.link("https://gd.eppo.int/media/files/general_user-guide.pdf")
	for page in pdf.pages:
		t = TEXT.readline(page.extract_text())
		text.append(t)
	for t in text:
		for l in t:
			print(l)
		print()
	return(text)

if __name__ == "__main__":
	main()
