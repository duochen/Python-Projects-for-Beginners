import re

pattern = r'\d{4}-\d{2}-\d{2}'
text = 'John Smith was born on 1990-01-15 and died on 2021-07-22.'
dates = re.findall(pattern, text)
print(dates)

if len(dates) == 2:
    birthdate, deathdate = dates
    print(f"Born on: {birthdate}")
    print(f"Died on: {deathdate}")
else:
    print("Could not find the birthdate and death date.")


