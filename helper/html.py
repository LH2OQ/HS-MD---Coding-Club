import requests
from bs4 import BeautifulSoup as bs

class HTML:
	def new(url: str, text: bool = False):
		# get html-content from website (url)
		response = requests.get(url)
		html = bs(response.content, "html.parser")
		if text:
			return getText(html)
		return html
	
	def text(html):
		# get only text
		return "\n".join(html.stripped_strings)
	
	def links(html):
		# get only links
		return html.find_all("a", attrs = {"href": True})
		
	def hasId(html, _id, tag = "div"):
		# find element by id
		return html.find(tag, attrs = {"id": _id})
	
	def haveClass(html, _class, tag = "div"):
		# find elements by classname
		return html.find_all(tag, attrs = {"class": _class})
	
	def get(url: str, params = {}):
		# api-request 'GET'
		response = requests.get(url = url, params = params)
		return response.json()
		
	def post(url: str, data = {}):
		# api-request 'POST'
		response = requests.post(url = url, data = data)
		return response.text
