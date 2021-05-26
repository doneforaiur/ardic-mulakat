# Zeller's congruence
# https://en.wikipedia.org/wiki/Zeller%27s_congruence

# Accuracy check
# https://www.timeanddate.com/calendar/weekday-sunday-1

def zeller(day, month, year):
	if month == 1:
		month = 13
		year = year - 1
	elif month == 2:
		month = 14
		year = year - 1
	
	q = day
	m = month
	k = year % 100
	j = year // 100
	
	h = q + 13 * (m + 1) // 5 + k + k // 4 + j // 4 + 5 * j
	h = h % 7
	if h == 2:
		print(str(day) + "/" + str(month) + "/" + str(year))
	
if __name__ == '__main__':
	for year in range(1900, 2000):
		for month in range(1,12):
			zeller(1,month,year)
