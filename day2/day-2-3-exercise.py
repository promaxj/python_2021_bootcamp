year_now = input("What year is it now?\n")
year_now = int(year_now)
age_now = input("how old are you?\n")
age_now = int(age_now)
burn_year = year_now - age_now
if (burn_year < 2000):


    the_life_year_after_2000 = burn_year + 90 - 2000
    the_life_year_before_2000 = 90 - the_life_year_after_2000

    before_2000_nu_year = 26 - ((100 - the_life_year_before_2000)//4)
    before_2000_not_nu_year = the_life_year_before_2000 - before_2000_nu_year

    after_2000_nu_year = the_life_year_after_2000 // 4
    after_2000_not_nu_year = the_life_year_after_2000 - after_2000_nu_year

    # print(f"the_life_year_before_2000: {the_life_year_before_2000}\nbefore_2000_nu_year: {before_2000_nu_year}\nbefore_2000_not_nu_year: {before_2000_not_nu_year}")
    # print(f"the_life_year_after_2000: {the_life_year_after_2000}\nafter_2000_nu_year: {after_2000_nu_year}\nafter_2000_not_nu_year: {after_2000_not_nu_year}\n")
else:
    the_life_year_after_2000 = burn_year + 90 - 2000 - age_now
    if (the_life_year_after_2000//4 >= 25):
        after_2000_nu_year = (the_life_year_after_2000//4) - 1
    else:
        after_2000_nu_year = the_life_year_after_2000//4
    after_2000_not_nu_year = the_life_year_after_2000 - after_2000_nu_year
    if (burn_year == 2000):
        after_2000_nu_year += 1
        after_2000_not_nu_year -= 1
    the_life_year_before_2000 = 0
    before_2000_nu_year = 0
    before_2000_not_nu_year = 0
    # print(f"the_life_year_after_2000: {the_life_year_after_2000}\nafter_2000_nu_year: {after_2000_nu_year}\nafter_2000_not_nu_year: {after_2000_not_nu_year}\n")
add_week = (before_2000_nu_year + after_2000_nu_year)//7



# left_years = 90 - int(age_now)
left_years = the_life_year_before_2000 + the_life_year_after_2000
left_months = round(left_years * 12)
left_weeks = round(left_years * 52 + add_week)
left_days = round(left_years * 365 + before_2000_nu_year + after_2000_nu_year)

print(f"\nIf you will live to 90 years old\nYou have {left_days} days, {left_weeks} weeks, and {left_months} months left.")