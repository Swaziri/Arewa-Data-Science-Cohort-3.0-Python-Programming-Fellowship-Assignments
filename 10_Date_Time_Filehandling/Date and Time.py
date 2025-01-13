from datetime import datetime, timedelta

# Get the current day, month, year, hour, minute, and timestamp
now = datetime.now()
print("Current Day:", now.day)
print("Current Month:", now.month)
print("Current Year:", now.year)
print("Current Hour:", now.hour)
print("Current Minute:", now.minute)
print("Current Timestamp:", now.timestamp())

# Format the current date using "%m/%d/%Y, %H:%M:%S"
formatted_date = now.strftime("%m/%d/%Y, %H:%M:%S")
print("Formatted Date:", formatted_date)

# Convert "5 December, 2019" to datetime
date_string = "5 December, 2019"
date_obj = datetime.strptime(date_string, "%d %B, %Y")
print("Converted Time Object:", date_obj)

# Calculate time difference between now and New Year
new_year = datetime(year=now.year + 1, month=1, day=1, hour=0, minute=0, second=0)
time_difference = new_year - now
print("Time until New Year:", time_difference)

# Calculate time difference between 1 January 1970 and now
epoch = datetime(1970, 1, 1)
time_difference_epoch = now - epoch
print("Time since 1 January 1970:", time_difference_epoch)

# Applications of datetime module
print("\nApplications of datetime module:")
print("1. Time Series Analysis")
print("2. Recording timestamps for user activities")
print("3. Scheduling and reminders")
print("4. Automatically attaching timestamps to blog posts")
print("5. Tracking system logs or monitoring processes")
print("6. Calculating age or duration for milestones")
