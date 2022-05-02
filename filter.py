obscene = ['dick', 'cunt', 'penis', 'vagina', 'sex']
threat = ['kill', 'mame', 'torture', 'die']
identity_hate = ['faggot', 'fag', 'faggots', 'gays', 'pedophile']
insult = ['stupid', 'idiot', 'dumb']
profanity = ['shit', 'fuck', 'damn', 'hell', 'fucking', 'bitch', 'asshole', 'ass', 'bastard']

def calc_toxicity_score(statement):
	score = 0
	if any(word in statement for word in obscene):
		score += 2
	if any(word in statement for word in threat):
		score += 3
	if any(word in statement for word in identity_hate):
		score += 5
	if any(word in statement for word in insult):
		score += 1
	if any(word in statement for word in profanity):
		score +=2
	return score