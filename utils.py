import random
import matplotlib.pyplot as plt


def roll_dice():
    die1 = random.randint(1,6)
    die2 = random.randint(1,6)
    return die1 + die2


def scratch_horses():
    scratched_horses = []
    # keep rolling until 4 distinct horses have been scratched
    while len(scratched_horses) < 4:
        dice_sum = roll_dice()
        if dice_sum in scratched_horses:
            pass
        else:
            scratched_horses.append(dice_sum)
    return scratched_horses


def race():
    horse_positions = [0,0,0,0,0,0,0,0,0,0,0]

    is_winner = False
    winning_horse = -1

    scratched_horses = scratch_horses()

    while not is_winner:
        dice_sum = roll_dice()
        if dice_sum not in scratched_horses:
            # need -2 in index because of 0 based indexing and the first horse is labeled 2
            horse_positions[dice_sum - 2] += 1

        # check for winner
        if (horse_positions[0]==2 or 
            horse_positions[1]==3 or 
            horse_positions[2]==4 or 
            horse_positions[3]==5 or 
            horse_positions[4]==6 or 
            horse_positions[5]==7 or 
            horse_positions[6]==6 or 
            horse_positions[7]==5 or 
            horse_positions[8]==4 or 
            horse_positions[9]==3 or 
            horse_positions[10]==2):

            is_winner = True 
            winning_horse = dice_sum

    return (scratched_horses, winning_horse)

def plot_frequency_of_winners_and_scratchers(x_axis, y_axis_winners, y_axis_scratched_horses, number_of_races):
    plt.style.use('seaborn-v0_8')
    plt.suptitle(f"Frequency of Winning Horse Numbers vs. Scratched Horse Numbers after {number_of_races} trials", fontsize=14)

    plt.subplot(2, 1, 1)
    plt.bar(x_axis, y_axis_winners, label='Winners')
    plt.ylabel('Number of Races Won')
    for i, value in enumerate(y_axis_winners):
        plt.text(x_axis[i], value + 1, str(value), ha='center', va='bottom')

    plt.subplot(2, 1, 2)
    plt.bar(x_axis, y_axis_scratched_horses, label='Scratchers')
    plt.ylabel('Number of Races Scratched')
    plt.xlabel('Horse')
    for i, value in enumerate(y_axis_scratched_horses):
        plt.text(x_axis[i], value + 1, str(value), ha='center', va='bottom')

    plt.savefig('fig/frequency_of_winners_and_scratchers.png')
    plt.close()

def plot_probability_of_winning(x_axis, y_axis_winners, number_of_races):
    probabilities = [100.0 * y/number_of_races for y in y_axis_winners]

    plt.style.use('seaborn-v0_8')
    plt.bar(x_axis, probabilities)
    plt.title(f'Chance of each Horse winning after {number_of_races} trials')
    plt.ylabel('Chance of Winning (%)')
    plt.xlabel('Horse')

    for i, value in enumerate(probabilities):
        plt.text(x_axis[i], value, f'{value/100:.2%}', ha='center', va='bottom')

    plt.savefig('fig/probability_of_each_horse_winning.png')
    plt.close()
