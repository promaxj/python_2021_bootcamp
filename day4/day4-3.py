# 🚨 Don't change the code below 👇
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
# row = int(position)%10
# column = int(position)//10

print(f"{row}\n{column}")
if (row<1 or row>3 or column<1 or column>3):
    print("type wrong!!!")
elif (column==1):
    row1[row-1] = "X"
elif (column==2):
    row2[row-1] = "X"
    print(f"{row1}\n{row2}\n{row3}")
elif (column==3):
    row3[row-1] = "X"
    print(f"{row1}\n{row2}\n{row3}")



#Write your code above this row 👆

# 🚨 Don't change the code below 👇
