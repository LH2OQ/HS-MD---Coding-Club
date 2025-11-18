import requests
from bs4 import BeautifulSoup as bs

class HTML:
	def new(url: str, text: bool = False):
		response = requests.get(url)
		html = bs(response.content, "html.parser")
		if text:	
			return getText(html)
		return html
	
	def text(html):
		return "\n".join(html.stripped_strings)
	
	def links(html):
		return html.find_all("a", attrs = {"href": True})
		
	def hasId(html, _id, tag = "div"):
		return html.find(tag, attrs = {"id": _id})
	
	def haveClass(html, _class, tag = "div"):
		return html.find_all(tag, attrs = {"class": _class})
