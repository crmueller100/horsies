import random
import matplotlib.pyplot as plt


def horse_race():
    horse_positions = [0,0,0,0,0,0,0,0,0,0,0]
    dead_horses = []

    while len(dead_horses) < 4:
        die1 = random.randint(1,6)
        die2 = random.randint(1,6)
        dice_sum = die1 + die2

        if dice_sum in dead_horses:
            pass
        else:
            dead_horses.append(die1 + die2)

    print("The dead horses are", dead_horses)

    is_winner = False
    winning_horse = -1

    while not is_winner:
        die1 = random.randint(1,6)
        die2 = random.randint(1,6)
        dice_sum = die1 + die2
        if dice_sum not in dead_horses:
            horse_positions[die1+die2-2] += 1 #Need to minus 2 bc it's 0 based indexing, so the first element in the list represents snake eyes


        if horse_positions[0]==2 or horse_positions[1]==3 or horse_positions[2]==4 or horse_positions[3]==5 or horse_positions[4]==6 or horse_positions[5]==7 or horse_positions[6]==6 or horse_positions[7]==5 or horse_positions[8]==4 or horse_positions[9]==3 or horse_positions[10]==2:
            is_winner = True 
            winning_horse = dice_sum

    print("The winning horse is", winning_horse)
    return (dead_horses, winning_horse)