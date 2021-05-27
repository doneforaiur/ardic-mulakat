def harmony(input):
	input = input.lower()
	
	back_vowels_list  = ["a", "ı", "o", "u"]
	front_vowels_list = ["e", "i", "ö", "ü"]

	front, back = False, False
	
	for char in input:
		if char in back_vowels_list:
			back = True
		elif char in front_vowels_list:
			front = True

		if front and back:
			return False

	# 0 0 = 0
	# 1 0 = 1
	# 0 1 = 1
	# 1 1 = 0
	return (front ^ back)

if __name__ == '__main__':

	#dictionary = open("dict.txt", "r", encoding="utf-8")
	#words = dictionary.read().split('\n')
	
	words = ["TBMM", "İstanbul", "hamsi", "araba"]
	for word in words:
		print(harmony(word))
		#harmony(word)
