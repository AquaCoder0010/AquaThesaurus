import requests 
from bs4 import BeautifulSoup
import time

class AquaThesaurus:
	text = "";
	URL = "";

	def __init__(self):
		self.text = "";
		self.URL = "https://www.thesaurus.com/browse/";

	def getSynonyms(self, word):
		self.text = word;
		self.URL = "https://www.thesaurus.com/browse/" + self.text;

		page = requests.get(self.URL);
		soup = BeautifulSoup(page.content, "html.parser");

		synonymsUl = soup.find(id="meanings").find_all("ul")[0].find_all("li");
		synonymsList = [];

		for synonyms in synonymsUl:
			aContainer = synonyms.find("a");
			synonymsList.append(aContainer.text);

		self.URL = "https://www.thesaurus.com/browse/";
		time.sleep(0.6);

		return synonymsList;

	def getAntonyms(self, word):
		self.text = word;
		self.URL = "https://www.thesaurus.com/browse/" + self.text;

		page = requests.get(self.URL);
		soup = BeautifulSoup(page.content, "html.parser");

		antonymsUl = soup.find(id="antonyms").find_all("ul")[0].find_all("li");
		antonymsList = [];

		for antonyms in antonymsUl:
			aContainer = antonyms.find("a");
			antonymsList.append(aContainer.text);

		self.URL = "https://www.thesaurus.com/browse/";
		time.sleep(0.6);
		
		return antonymsList;