# Zeller's congruence
# https://en.wikipedia.org/wiki/Zeller%27s_congruence

def zeller(day, month, year):
	if month < 3:
		month = 12 + month
		year = year - 1
	
	# 0: Saturday, 1: Sunday, 2: Monday, ..., 6: Friday
	day_of_the_week =( day + 13 * (month + 1) // 5 + (year % 100) + (year % 100) // 4 + (year // 100) // 4 + 5 * (year // 100) ) % 7
	
	if day_of_the_week == 1:
		if month > 12:
			month = month - 12
			year = year + 1
		print(str(day) + "/" + str(month) + "/" + str(year))
	
	
if __name__ == '__main__':
	
	for year in range(1900, 3000):
		for month in range(1,12):
			zeller(1,month,year)
