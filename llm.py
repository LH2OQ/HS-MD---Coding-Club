from openai import OpenAI
from helper.files import PATH

base_url = "BITTE_HIER_base_url_EINFÜGEN",
api_key = "BITTE_HIER_api_key_EINFÜGEN"


DEFAULT_SYSTEM_PROMPT = """
		Du bist ein hilfreicher Assistent - deine Aufgabe ist es, Anfragen so klar und verständlich wie möglich zu beantworten.
		Dabei ist es wichtig, einfache und kurze Sätze zu wählen, auf komplizierte Fachwörter zu verzichten, bzw. diese zu beschreiben oder Synonyme zu benutzen, und die zur Anfrage relevante Information so auszugeben, dass eine jugendliche Person mit dem Bildungshintergrund einer deutschen Hauptschule diese nachvollziehen, interpretieren und lösungsorientiert anwenden kann.
	"""
MAX_TOKENS = 150

def getClient():
	client = OpenAI(
		base_url = base_url,
		api_key = api_key
		)
	client.models.list()
	return client

def askLLM(client, prompt: str, system_prompt: str = DEFAULT_SYSTEM_PROMPT):
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
	
	# Ich halte es für sinnvoll, den Dialog in Textdateien zu speichern,
	# da so schon einmal hilfreich beantworte Anfrag nicht erneut gestellt werden müssen.
	# Das spart Strom, etc ...
	folder = PATH.mkdir(PATH.cwd() + "/LLM")
	n = len([name for name in os.listdir(folder) if os.path.isfile(name)])
	text = f"PROMPT:\n\n{prompt}\n\nRESPONSE({MAX_TOKENS}):\n\n{response}"
	PATH.write(folder + f"/text_{n}", text)
	print(response)
	return response


