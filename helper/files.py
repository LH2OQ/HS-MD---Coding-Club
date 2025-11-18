import os
import requests
import urllib.request as req
from pypdf import PdfReader as pdf
from io import BytesIO as byio

class PATH:
	def cwd():
		return os.getcwd()
	
	def exists(path: str):
		return os.path.exists(path)
	
	def mkdir(path: str):
		if not os.path.exists(path):
			os.makedirs(path)
		return path
	
	def read(path: str):
		with open(path, "r") as f:
			return f.read()
	
	def write(path: str, data, read: bool = False):
		with open(path, "rw") as f:
			f.write(data)
			return f.read() if read else path
	
	def download(link: str, path: str):
		response = requests.get(link)
		with open(path, "wb") as f:
			f.write(response.content)
		return path

class PDF:
	def text(path: str):
		text = []
		for page in pdf(path).pages:
			text.append(TEXT.readline(page.extract_text()))
		return text
	
	def link(url: str):
		request = req.Request(url)
		remoteFile = req.urlopen(request).read()
		remoteFileBytes = byio(remoteFile)
		data = pdf(remoteFileBytes)
		return data

class TEXT:
	def readline(text):
		return text.split("\n")
			
