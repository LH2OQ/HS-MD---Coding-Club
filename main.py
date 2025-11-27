from helper.html import HTML
from helper.files import PATH, PDF, TEXT
from helper.eppo_first_aid import getFirstAid

def main():
	# prompt the llm for help
	getFirstAid()
	
def apiRequest(eppoCode, authToken):
	# make an api-request to www.eppo.int to find information by specific token (eppoCode)
	return HTML.get(
		f"https://data.eppo.int/api/rest/1.0/taxon/{eppoCode}?",
		{"authtoken": authToken}
	)

if __name__ == "__main__":
	main()
