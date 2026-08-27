def separator(sentance):
	import string
	sentance = sentance.lower()
	for i in string.punctuation:
		new = sentance.replace(i, ',')
		sentance = new
	new = new.replace('and', ',')
	new = new.split(',')
	new = [i.strip() for i in new if i]
	return new

def brain(sentance, primary_data):
	count = 0
	count_list = []
	sentance = sentance.split()
	for i in primary_data:
		for j in sentance:
			for k in i:
				if j == k:
					count += 1
		count_list.append(count)
		count = 0
	return count_list

def generate_response(sentances, primary_data, responses):
	final_response = ""
	sig = 0
	for i in sentances:
		process_data = brain(i, primary_data)
		if sum(process_data) != 0:
			if process_data.index(max(process_data)) == len(process_data) - 1:
				sig = 1
			response = responses[process_data.index(max(process_data))]
			final_response += (response[0] + ' ')
			if sig == 1:
				return final_response, sig
	return final_response, sig if len([i for i in final_response if i.isalpha()]) > 0 else None

primary_data = [
["who", "made", "you", "what", "created", "built", "crafted", "programmed", "your", "maker"],
["hello", "there", "how", "are", "you", "good", "fine", "great", "hi"],
["greetings", "good", "morning", "afternoon", "evening", "night"],
["thank", "you", "thanks", "gratitude", "to", "very", "much"],
["what", "is", "your", "name", "may", "i", "know", "good", "are", "you", "called", "who"],
["what", "is", "define", "tell", "explain", "about", "c", "programming", "language", "it", "me"],
["goodbye", "good", "bye", "see", "you", "later", "soon", "got", "to", "hurry", "go", "gotta"]]

responses = [["The one who made me is lance."], ["Hi there!"], ["Greetings to you too!"], ["You're welcome!"], ["I'm Artificial Super Intelligence."], ["C is a statically typed procedural middle-level programming developed by Dennis M. Ritchie."], ["Take care, have a nice day."]]

while 1:
	sentance = input("You: ")
	sentances = separator(sentance)
	response, sig = generate_response(sentances, primary_data, responses)
	if response == None:
		print("Response not set.")
	else:
		print("Response:", response)
		if sig == 1:
			break
