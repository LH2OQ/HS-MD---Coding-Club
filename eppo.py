from helper.html import HTML
from helper.files import PATH, PDF, TEXT
from eppo_first_aid import getFirstAid

def main():
	getFirstAid()
	
def apiRequest(eppoCode, authToken):
	return HTML.get(
		f"https://data.eppo.int/api/rest/1.0/taxon/{eppoCode}?",
		{"authtoken": authToken}
	)

if __name__ == "__main__":
	main()
