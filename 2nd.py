# Sakamoto's method
# https://en.wikipedia.org/wiki/Determination_of_the_day_of_the_week#Sakamoto's_methods

def is_sunday(day, month, year):
	if month < 3:
		year -= 1
	
	# Formula to calculate the following table;
	# Shift months by 2;
	# [1: March, 2: April, ..., 12: February]
	# Print month and corresponding number in months' correct order;
	# [January:11, February: 12, March:1, ..., December: 10]
	# Months = [11, 12, 1, 2, ..., 10]
	# day_offsets = [(int(2.6* month - 0.2) % 7 ) for month in Months]
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
	
	if day_names[day_of_week] == "Sunday":
		return True
	else:
		return False
	
if __name__ == '__main__':
	for year in range(1900, 2001):
		for month in range(1,13):
			if(is_sunday(1, month, year)):
				print(1, month, year)
