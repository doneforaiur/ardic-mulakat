def harmony(input):
	input = input.lower()
	
	back_vowels_list  = ["a", "ı", "o", "u"]
	front_vowels_list = ["e", "i", "ö", "ü"]
	
	back_count  = 0
	front_count = 0
	
	for char in input:
		if char in back_vowels_list:
			back_count = back_count + 1
		elif char in front_vowels_list:
			front_count = front_count + 1
	
		if front_count > 0 and back_count > 0:
			return False
	return True
	
	
if __name__ == '__main__':
	
	f = open("dict.txt", "r", encoding="utf-8")
	words = f.readlines()
	for word in words:
		harmony(word)
