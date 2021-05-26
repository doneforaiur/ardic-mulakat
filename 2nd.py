# Sakamoto's method
# https://en.wikipedia.org/wiki/Determination_of_the_day_of_the_week#Sakamoto's_methods

def zeller(day, month, year):
	if month < 3:
		year -= 1
	
	# remainder of cumulative day difference between
	# previous months divided by number of weekdays
	day_offsets = [0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4]
	
	# leap year offsets
	lyo_4   = year // 4
	lyo_100 = year // 100
	lyo_400 = year // 400
	
	prev_month_offset = month - 1
	
	day_names = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
	day_of_week = year + lyo_4 - lyo_100 + lyo_400 + day_offsets[prev_month_offset] + day
	
	days_in_week = 7
	
	day_of_week = day_of_week % days_in_week
	
	if day_names[day_of_week] == "Monday":
		if month < 3:
			year += 1
		print(day,month, year)
	
if __name__ == '__main__':
	for year in range(1900, 2000):
		for month in range(1,12):
			zeller(1,month,year)
