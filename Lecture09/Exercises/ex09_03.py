months = {
    "01": "January", "02": "February", "03": "March", 
    "04": "April", "05": "May", "06": "June", 
    "07": "July", "08": "August", "09": "September", 
    "10": "October", "11": "November", "12": "December"
}

days = {
    "01": "first", "02": "second", "03": "third", "04": "fourth", "05": "fifth",
    "06": "sixth", "07": "seventh", "08": "eighth", "09": "ninth", "10": "tenth",
    "11": "eleventh", "12": "twelfth", "13": "thirteenth", "14": "fourteenth", 
    "15": "fifteenth", "16": "sixteenth", "17": "seventeenth", "18": "eighteenth", 
    "19": "nineteenth", "20": "twentieth", "21": "twenty-first", "22": "twenty-second", 
    "23": "twenty-third", "24": "twenty-fourth", "25": "twenty-fifth", 
    "26": "twenty-sixth", "27": "twenty-seventh", "28": "twenty-eighth", 
    "29": "twenty-ninth", "30": "thirtieth", "31": "thirty-first"
}

def months_to_words(date):
    month, day = date.split('-')
    month_name = months[month]
    day_word = days[day]
    return f"{month_name} {day_word}"

print(months_to_words("12-25"))  # Output: December twenty-fifth
print(months_to_words("07-04"))  # Output: July fourth
