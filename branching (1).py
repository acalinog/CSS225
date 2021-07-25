# A time traveler has suddenly appeared in your classroom!

# Create a variable representing the traveler's
# year of origin (e.g., year = 2000)
# and greet our strange visitor with a different message
# if he is from the distant past (before 1900),
# the present era (1900-2020) or from the far future (beyond 2020).

# Equals: a == b
# Not Equal: a != b
# Less than: a < beyond 
# Less than or qual to: a <= b
# Greater than: a > b
# Greater than or equal to: a >= b

def year():
    print ('2000')

year == input("Greetings! What is your year of origin?")

if year <= 1900:
    print ('Woah, thats the past!')
elif year > 1900 & year < 2020:
    print ("That's totally the present!")
else:
    print ("Far out, that's the future!!")