# doesn't check for accented vowels
def harmony(input):
	input = input.lower()
	
	back_vowels_list  = ["a", "ı", "o", "u"]
	front_vowels_list = ["e", "i", "ö", "ü"]
	
	back = None
	front = None
	
	for char in input:
		if char in back_vowels_list:
			back = True
		elif char in front_vowels_list:
			front = True

	if back == None and front == None:
		return False
	else:
		return not (back and front)
	
	
if __name__ == '__main__':

	f = open("dict.txt", "r", encoding="utf-8")
	words = f.read().split('\n')

	for word in words:
		print(harmony(word))
