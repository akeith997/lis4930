from datetime import timedelta  
d = datetime.now()
td_seconds = timedelta(seconds=-60) #subtract 60 seconds
td_years = timedelta(weeks=104) #add two years
print(d + td_seconds + td_years)
