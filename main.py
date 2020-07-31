





import random



# something else




def uwuify(strin:str, strength:float=0.5):
	# the main fuction 

	common_sub=[
		[" hi", "haii<END>"],
		[" bye", "baii<END>"],
		["see", "notice"],
		["omg", "omg<!>"],
		["wow...", "wow<sad>"],
		["wow..", "wow<sad>"],
		["wow", "wow<!>"],
		["but", "but<!>"],
		[",", "<=>"],
		[".", "<END>"]
	]
	final_sub=[
		["r","w"],
		["R","W"]
	]

	happy_emojis=["(. ❛ ᴗ ❛.)", "(◕ᴗ◕✿)", "( ꈍᴗꈍ)", "(≧▽≦)", "(✿^‿^)", "(◠‿・)—☆", ">///<", "^v^", "OwO", "UwU", "^///^", "^~^"]
	light_weight_emojis=["Owo", "owo", "-w-", "^w^", "uwu", "UwU"]
	delimed=strin.split(" ")
	strin=""
	for word in delimed:
		if len(word) <= 3 and random.random() < 0.5:
			word=word.upper()
		elif len(word) > 7 and random.random() < 0.3:
			word=word.upper()
		else:
			word=word.lower()
		strin+=word+" "
	delimed=strin.split("u")
	strin=""
	for stuff in delimed:
		strin+=stuff+"u"
		if random.random() < 0.2:
			strin+="wu"
	delimed=strin.split("o")
	strin=""
	for stuff in delimed:
		strin+=stuff+"o"
		if random.random() < 0.2:
			strin+="wo"

	for k in common_sub:
		strin = strin.replace(k[0], k[1])
	# print(strin)

	while "<=>" in strin:
		strin=strin.replace("<=>", f" {light_weight_emojis[random.randint(0, len(light_weight_emojis)-1)]} ", 1)
	
	while "<END>" in strin:
		strin=strin.replace("<END>", f" {happy_emojis[random.randint(0, len(happy_emojis)-1)]} ", 1)

	while "<!>" in strin:
		strin=strin.replace("<!>", "!!1!")

	for k in final_sub:
		strin = strin.replace(k[0], k[1])
		
	return strin




# epic fail
if __name__ == "__main__":
	print(uwuify(
		"""
The Industrial Revolution, now also known as the First Industrial Revolution, was the transition to new manufacturing processes in Europe and the United States, in the period from about 1760 to sometime between 1820 and 1840. This transition included going from hand production methods to machines, new chemical manufacturing and iron production processes, the increasing use of steam power and water power, the development of machine tools and the rise of the mechanized factory system. The Industrial Revolution also led to an unprecedented rise in the rate of population growth.

Textiles were the dominant industry of the Industrial Revolution in terms of employment, value of output and capital invested. The textile industry was also the first to use modern production methods.
"""
	))