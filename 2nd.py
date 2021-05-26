# Sakamoto's method
# https://en.wikipedia.org/wiki/Determination_of_the_day_of_the_week#Sakamoto's_methods

def zeller(day, month, year):
	if month < 3:
		year -= 1
	
	day_offsets = [0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4] # [int(2.6*month - 0.2) for month in range(1,12)
	
	# leap year offsets
	lyo_4   = year // 4
	lyo_100 = year // 100
	lyo_400 = year // 400
	
	prev_month_offsets = month - 1
	
	# 0: Sunday, 1: Monday, ..., 6: Saturday.
	day_of_week = year + lyo_4 - lyo_100 + lyo_400 + day_offsets[prev_month_offsets] + day
	
	day_of_week = day_of_week % 7 # mod number of days in a week
	
	if day_of_week == 0:
		if month < 3:
			year += 1
		print(day,month, year)
	
if __name__ == '__main__':
	for year in range(1900, 2000):
		for month in range(1,12):
			zeller(1,month,year)
