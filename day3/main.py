#Day 3 project: Treasure Island

print("Welcome to Treasure Island.\nYour Mission is to find the treasure.")
direction = input("Left or right? ")

if direction == "left":
    swimWait = input("Swim or wait? ")
    if swimWait == "wait":
        door = input("Which door: red, blue or yellow? ")
        if door == "yellow":
            print("You win!")
        elif door == "blue":
            print("Eaten by beasts.\nGame Over.")
        elif door == "red":
            print("Burned by fire.\nGame Over.")        
        else:
            print("Game Over.") 
    else:
        print("Attacked by trout.\nGame Over.")
else:
    print("Fall into a hole.\nGame Over.")                   