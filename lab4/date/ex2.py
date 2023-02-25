from datetime import date, timedelta
today = date.today()
yesterday = today - timedelta(1)
dtom = today + timedelta(1)
print("today date:", today)
print("yesterday's date:", yesterday)
print("tommorow's date:", dtom)