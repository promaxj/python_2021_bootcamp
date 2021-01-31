#Write your code below this line 👇
def prime_checker(number):
    if  number == 2:
        print(f"TRUE        {number} is a prime number.")
        return
    else:
        for n in range(2, number):
            if number % n == 0:
                print(f"FALSE       {number} is not a prime number.")
                return
        print(f"TRUE        {number} is a prime number.")





#Write your code above this line 👆

#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)



