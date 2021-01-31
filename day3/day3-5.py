# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

lower_case_name1 = name1.lower()
lower_case_name2 = name2.lower()
mixed_lower_case_name = lower_case_name1 + lower_case_name2
t = mixed_lower_case_name.count('t')    #int type
r = mixed_lower_case_name.count('r')    #int type
u = mixed_lower_case_name.count('u')    #int type
e = mixed_lower_case_name.count('e')    #int type
love_score_ten_digit = t+r+u+e          #int type
l = mixed_lower_case_name.count('l')    #int type
o = mixed_lower_case_name.count('o')    #int type
v = mixed_lower_case_name.count('v')    #int type
e = mixed_lower_case_name.count('e')    #int type
love_score_units_digit = l+o+v+e        #int type


# For Love Scores less than 10 or greater than 90, the message should be:
# "Your score is **x**, you go together like coke and mentos."
# For Love Scores between 40 and 50, the message should be:
# "Your score is **y**, you are alright together."
# Otherwise, the message will just be their score. e.g.:
# "Your score is **z**."

love_scores = love_score_ten_digit*10 + love_score_units_digit
if (love_scores < 10 or love_scores > 90):
    print(f"Your score is {love_scores}, you go together like coke and mentos.")
elif (love_scores >= 40 or love_scores <= 50):
    print(f"Your score is {love_scores}, you are alright together.")
else:
    print(f"Your score is {love_scores}.")