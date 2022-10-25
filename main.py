import random
from bs4 import BeautifulSoup
import re
import urllib.request
import platform
import os

# something else

def uwuify(strin:str, strength:float=0.5):
	# the main fuction

	# if strength is 1 everything is owo uwu "w" @w@ .w. :3 ^w^
	if strength == 1:
		pass

	common_sub=[
		[" hi", " haii<END>"],
		[" bye", "baii<END>"],
		["see", "notice"],
		["omg", "omg<!>"],
		["wow...", "wow<sad>"],
		["wow..", "wow<sad>"],
		[" wow ", "wow<!>"],
		["but", "but<!>"],
		[",", "<=>"],
		[".", "<END>"]]

	final_sub=[
		["r","w"],
		["R","W"]]

	happy_emojis=["(. ❛ ᴗ ❛.)", "(◕ᴗ◕✿)", "( ꈍᴗꈍ)", "(≧▽≦)", "(✿^‿^)", "(◠‿・)—☆", ">///<", "^v^", "OwO", "UwU", "^///^", "^~^"]
	light_weight_emojis=["Owo", "owo", "-w-", "^w^", "uwu", "UwU"]

	delimed=strin.split(" ")
	strin=""

	for word in range(len(delimed)):

		if len(delimed[word]) <= 3 and random.random() < 0.5:
			delimed[word]=delimed[word].upper()
		elif len(delimed[word]) > 7 and random.random() < 0.3:
			delimed[word]=delimed[word].upper()
		else:
			delimed[word]=delimed[word].lower()
		
		if word == len(delimed)-1:
			strin += delimed[word]
		else:
			strin += delimed[word]+" "

	delimed=strin.split("u")
	strin=""
	for stuff in range(len(delimed)):
		if stuff == len(delimed)-1:
			strin += delimed[stuff]
		else:
			strin+=delimed[stuff] + "u"
			if random.random() < 0.2:
				strin+="wu"

	delimed=strin.split("o")
	strin=""
	for stuff in range(len(delimed)):
		if stuff == len(delimed)-1:
			strin += delimed[stuff]
		else:
			strin+=delimed[stuff] + "o"
			if random.random() < 0.2:
				strin+="wo"

	for k in common_sub:
		strin = strin.replace(k[0], k[1])
	# print(strin)

	while "<=>" in strin:
		strin=strin.replace("<=>", f" {light_weight_emojis[random.randint(0, len(light_weight_emojis)-1)]}", 1)
	
	while "<END>" in strin:
		strin=strin.replace("<END>", f" {happy_emojis[random.randint(0, len(happy_emojis)-1)]} ", 1)

	while "<!>" in strin:
		strin=strin.replace("<!>", "!!!!")

	for k in final_sub:
		strin = strin.replace(k[0], k[1])
		
	return strin

def url_to_str(url):
	data = urllib.request.urlopen(url)

	url_bytes = data.read()

	doc = url_bytes.decode("utf8")

	data.closed

	return doc

def uwuify_url(doc):
	soup = BeautifulSoup(doc, 'html.parser')
	uwu = ''

	for tag in soup.find_all('p'):
		uwu += uwuify(tag.get_text()) + '\n\n'

	return uwu

# epic fail
if __name__ == "__main__":

	doc = url_to_str("https://en.wikipedia.org/wiki/Uwu_(emoticon)")

	uwu = uwuify_url(doc).strip()

	# open a new txt file and write uwu into it
	with open("hehe.txt", "w") as text:
		print(uwu, file=text)

	# open txt file
	# TODO: make it open url to uwuey page!
	if platform.system() == "Linux":
		os.system("xdg-open hehe.txt")
	# TODO: add windows option
	if platform.system() == "Windows":
		pass

	# TODO: insert text into a body, then open webpage
	
