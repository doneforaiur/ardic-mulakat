def harmony(input):
	back_vowels  = ["a", "ı", "o", "u"]
	front_vowels = ["e", "i", "ö", "ü"]
	
	state = ""
	
	for i in range(len(input)):
		if input[i] in back_vowels and state == "":
			state = "back"
		elif input[i] in front_vowels and state == "":
			state = "front"
		
		if ((state == "back") and (input[i] in front_vowels)) or ((state == "front") and (input[i] in back_vowels)):
			return False
	return True
	
	
if __name__ == '__main__':
	word = "bilezik"
	print(harmony(word))
