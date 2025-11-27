from helper.html import HTML
from helper.files import PATH, PDF, TEXT
from llm import getClient, askLLM

def filterLinks(html):
	# find specific links to database
	data = ""
	for l in HTML.links(html):
		href = l["href"]
		text = HTML.text(l)
		if "PP" in text or "PM" in text:
			data = "\n".join([data, text, href])
	return data
	
def getUserInstructions():
	# get the user-manual-pdf as text (list)
	text = []
	pdf = PDF.link("https://gd.eppo.int/media/files/general_user-guide.pdf")
	for page in pdf.pages:
		t = TEXT.readline(page.extract_text())
		text.append(t)
	return(text)

def getFirstAid():
	# use the llm => get strategical knowledge, code, whatever helpful text to develop an application
	html = HTML.new("https://gd.eppo.int/taxon")
	cwd = PATH.cwd()
	prompt = f"""
		Es existiert eine Datenbank auf der Internetseite "www.eppo.int"
		Folgende Liste zeigt Links für den Zugriff auf verschiedene Bereiche der Datenbank, auf der Pflanzenkrankheiten und Symptome beschrieben sind:
		
		[{filterLinks(html)}]
		
		und dies ist der Inhalt der Benutzeranweisungen:
		
		{getUserInstructions()}
		
		Ich möchte ein Programm in Pythoncode schreiben, das je nach Benutzeranfrage auf die Datenbank zugreifen kann und entsprechende Informationen zu Pflanzen, Krankheiten, Symptomen, etc ausgibt.
		Dazu existieren schon folgende Skripte:
		
			### MAINSCRIPT(eppo.py):
			{PATH.read(cwd+"/eppo.py")}
		
			### HELPERSCRIPT(eppo_first_aid.py):
			{PATH.read(cwd+"/eppo_first_aid.py")}
			
			### HELPERSCRIPT(llm.py):
			{PATH.read(cwd+"/llm.py")}
			
			### HELPERSCRIPT(html.py):
			{PATH.read(cwd+"/helper/html.py")}
			
			### HELPERSCRIPT(text.py):
			{PATH.read(cwd+"/helper/files.py")}
			
			### HELPERSCRIPT(files.py):
			{PATH.read(cwd+"/helper/files.py")}
			
		Bitte hilf mir dabei, dieses Programm zu entwickeln.
		Danke.
	"""
	askLLM(getClient(), prompt)
