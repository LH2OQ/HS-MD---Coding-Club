from openai import OpenAI
from helper.files import PATH

base_url = "BITTE_HIER_base_url_EINFÜGEN",
api_key = "BITTE_HIER_api_key_EINFÜGEN"


DEFAULT_SYSTEM_PROMPT = """
		Du bist ein hilfreicher Assistent.
		Deine Aufgabe ist es, Anfragen so klar und verständlich wie möglich zu beantworten.
		Die zur Anfrage relevante Information soll so ausgegeben werden,
		dass eine Person mit dem Bildungshintergrund einer deutschen Hauptschule diese nachvollziehen,
		interpretieren und lösungsorientiert anwenden kann.
		Dabei ist es wichtig, einfache und kurze Sätze zu wählen,
		auf komplizierte Fachwörter zu verzichten, bzw. diese zu beschreiben oder Synonyme zu benutzen.
	"""
MAX_TOKENS = 150

def getClient():
	# openai client request
	client = OpenAI(
		base_url = base_url,
		api_key = api_key
		)
	client.models.list()
	return client

def askLLM(client, prompt: str, system_prompt: str = DEFAULT_SYSTEM_PROMPT):
	# prompt the llm and get a response
	response = client.chat.completions.create(
		model = "LLama-4-Scout",
		messages = [{
			"role": "system",
			"content": system_prompt
		},
		{
			"role": "user",
			"content": prompt
		}],
		max_tokens = MAX_TOKENS
	).choices[0].message.content
	# save the conversation as a textfile in a subdirectory => current_directory/LLM
	folder = PATH.mkdir(PATH.cwd() + "/LLM")
	# n is the number of files that already exist in that directory (in case of multiple saves, 0 if empty)
	n = len([name for name in os.listdir(folder) if os.path.isfile(name)])
	# format prompt and response (+ max_tokens) as text, then write to file 
	text = f"PROMPT:\n\n{prompt}\n\nRESPONSE({MAX_TOKENS}):\n\n{response}"
	PATH.write(folder + f"/text_{n}", text)
	print(response)
	return response
