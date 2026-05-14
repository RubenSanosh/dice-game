import random
# this is a recreation of what ive made in CS20 "dice game"

# now adding a lucky chance to "find" a chip/coin

# ----------------------------
# INPUT VALIDATION FUNCTION
# ----------------------------
def get_valid_number(prompt, minimum, maximum=999999):

    while True:

        try:
            number = int(input(prompt))

            if number == 0:
                return 0

            if minimum <= number <= maximum:
                return number

            print("Invalid range. Try again.")

        except:
            print("Please enter a WHOLE NUMBER.")


# ----------------------------
# SINGLE ROUND FUNCTION
# ----------------------------
def play_round(balance):

    print("\n--- New Round ---")
    print("Current Balance: $", balance)

    # Player choices
    dice_count = get_valid_number(
        "How many dice would you like to roll? (0 to quit): ",
        1,
        balance # To limit amount of dice rolled equal to balance
    )

    if dice_count <= 0:
        print("Invalid dice count.")
        return balance, False

    if dice_count == 0:
        return balance, True

    side_count = get_valid_number(
        "How many sides should the dice have? (min 2): ",
        2,
        1000
    )

    # 🔴 SAFETY CHECK (IMPORTANT)
    if side_count < 2:
        print("Invalid dice sides. Round cancelled.")
        return balance, False

    guess = get_valid_number(
        f"Choose a guess between 1 and {side_count}: ",
        1,
        side_count
    )

    # Extension: variable wager
    max_wager = max(1, balance // dice_count)

    if max_wager < 1:
        print("Wager too small to play.")

    wager = get_valid_number(
        f"Enter wager per die (Min $1, Max ${max_wager}): ",
        1,
        max_wager
    )

    if wager == 0:
        print("Wager cannot be 0. Setting automatically to $1")
        wager = 1

    total_gain = 0
    correct_dice = 0
    incorrect_dice = 0
    winnings = 0

    print("\nRolling dice...\n")

    # Roll each die
    for roll_number in range(1, dice_count + 1):

        roll = random.randint(1, side_count)

        print(f"Die {roll_number}: {roll}")

        if roll == guess:

            total_gain += wager
            correct_dice += 1

            print("Correct guess! You won $", wager)

        else:

            total_gain -= wager
            incorrect_dice += 1

            print("Incorrect guess! You lost $", wager)

    # Update balance
    balance += total_gain

    # Round summary
    print("\n--- Round Summary ---")
    print("Correct Dice:", correct_dice)
    print("Incorrect Dice:", incorrect_dice)

    if total_gain >= 0:
        print("Total Profit: $", total_gain)
    else:
        print("Total Loss: $", abs(total_gain))

    
 
    # ----------------------------
    # RANDOM EVENT SYSTEM
    # ----------------------------

    lucky_chance = random.randint(1, 100)

    # 50% chance
    if lucky_chance <= 50:

        print("\nNothing special happened this round.")

    # 30% chance
    elif lucky_chance <= 80:

        small_bonus = random.randint(5, 15)

        print("\n🍀 SMALL FIND!")
        print("You found a casino chip worth $", small_bonus)

        balance += small_bonus

    # 15% chance
    elif lucky_chance <= 95:

        medium_bonus = random.randint(20, 50)

        print("\n💎 BIG FIND!")
        print("A high-value poker chip was found worth $", medium_bonus)

        balance += medium_bonus
    
    #chance to lose chips
    elif lucky_chance <= 98:

        penalty = random.randint(10, 75)

        print("\n💀 BAD LUCK!")
        print("You dropped chips worth $", penalty)

        balance -= penalty

    # 5% chance
    else:

        jackpot = random.randint(150, 1000)

        print("\n🎰 JACKPOT FIND!!!")
        print("The highest value chip in the casino was found worth $", jackpot)

        balance += jackpot

    print("\nNew Balance: $", balance)

    return balance, False


# ----------------------------
# MAIN GAME FUNCTION
# ----------------------------
def main():

    play_again = "y"

    while play_again == "y":

        balance = 100

        total_rounds = 0
        total_profit = 0
        total_losses = 0

        print("================================")
        print("WELCOME TO THE DICE GAME BY RUBEN")
        print("================================")

        game_over = False

        while balance > 0 and not game_over:

            old_balance = balance

            balance, game_over = play_round(balance)

            round_change = balance - old_balance

            if round_change > 0:
                total_profit += round_change
            else:
                total_losses += abs(round_change)

            total_rounds += 1

        # End game summary
        print("\n================================")
        print("GAME OVER")
        print("================================")

        print("Final Balance: $", balance)
        print("Rounds Played:", total_rounds)
        print("Total Profit: $", total_profit)
        print("Total Losses: $", total_losses)

        # Ask to play again
        play_again = input("\nWould you like to play again? (Y/N): ").lower()

        while play_again not in ["y", "n"]:
            play_again = input("Please enter Y or N: ").lower()

    print("\nThanks for playing!")

# Run the program
main()