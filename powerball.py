import random

def print_banner():
    banner = r"""
    ╔═══════════════════════════════════════════════════════════════════════════════╗
    ║                                                                               ║
    ║  ██████╗  ██████╗ ██╗    ██╗███████╗██████╗ ██████╗  █████╗ ██╗     ██╗       ║
    ║  ██╔══██╗██╔═══██╗██║    ██║██╔════╝██╔══██╗██╔══██╗██╔══██╗██║     ██║       ║
    ║  ██████╔╝██║   ██║██║ █╗ ██║█████╗  ██████╔╝██████╔╝███████║██║     ██║       ║
    ║  ██╔═══╝ ██║   ██║██║███╗██║██╔══╝  ██╔══██╗██╔══██╗██╔══██║██║     ██║       ║
    ║  ██║     ╚██████╔╝╚███╔███╔╝███████╗██║  ██║██████╔╝██║  ██║███████╗███████╗  ║                                                                        ║
    ║                                                                               ║
    ║                                                                               ║
    ║                              POWERBALL SIMULATOR                              ║
    ║                              -------------------                              ║
    ║                              Pick your numbers.                               ║
    ║                              Test your luck.                                  ║
    ║                              DREAM BIG, WIN BIG!                              ║
    ║                                                                               ║
    ╚═══════════════════════════════════════════════════════════════════════════════╝
"""
    print(banner)

if __name__ == "__main__":
    print_banner()

print('''\nPowerball Lottery, by Nostripeszebra 
      
Inspired by Al Sweigart's original work

Each powerball lottery ticket costs $2.00 The jackpot for this game
is $1.5 billion! The odds of you winning are 1 in 293,000,000. 

Good luck!
''')

# Let the player enter the first five numbers, 1 to 69:
while True:
    print('Enter 5 different numbers from 1 to 69, with spaces between')
    print('each number. (For example: 5 17 23 42 50)')
    response = input('> ')

    # Check that the player entered 5 numbers:
    numbers = response.split()
    if len(numbers) != 5:
        print('\nError! Please enter 5 numbers, separated by spaces.\n')
        continue

    # Convert the strings into integers:
    try:
        numbers = [int(n) for n in numbers]
    except ValueError:
        print('\nError! Please enter numbers, like 27, 35, or 62.\n')
        continue

    # Check that the numbers are between 1 and 69:
    if any(n < 1 or n > 69 for n in numbers):
            print('\nError! The numbers must all be between 1 and 69.\n')
            continue
    
    # Check that the numbers are unique:
    # (Create a set from number to remove duplicates.)
    if len(set(numbers)) != 5:
        print('\nError! You must enter 5 different numbers.\n')
        continue

    break

# Let the player select the powerball, 1 to 26:
while True:
    print('\nEnter the powerball number from 1 to 26.')
    response = input('> ')

    # Convert the strings into integers:
    try:
        powerball = int(response)
    except ValueError:
        print('\nError! Please enter a number, like 3, 15, or 22.\n')
        continue

    # Check that the number is between 1 and 26:
    if not (1 <= powerball <= 26):
        print('\nError! The powerball number must be between 1 and 26.\n')
        continue

    break

# Enter the number of times you want to play:
while True:
    print('\nHow many times do you want to play? (Max: 1000000)')
    response = input('> ')

    # Convert the strings into integers:
    try: 
        numPlays = int(response)
    except ValueError:
        print('\nPlease enter a number, like 3, 15, or 22000.\n')
        continue

    # Check that the number is between 1 and 1000000:
    if not (1 <= numPlays <= 1000000):
        print('\nError! You can play between 1 and 1000000 times.\n')
        continue

    break

# Run the simlulation:
price = '$' + str(2 * numPlays)
print('\nIt will cost', price, 'to play', numPlays, 'times, but don\'t')
print('worry! I\'m sure you\'ll win it all back.')
input('\nPress Enter to start...')

possibleNumbers = list(range(1, 70))
for i in range(numPlays):
    # Come up with lottery numers:
    random.shuffle(possibleNumbers)
    winningNumbers = possibleNumbers[0:5]
    winningPowerball = random.randint(1, 26)

    # Display winning numbers:
    print('\nThe winning numbers are: ', end='')
    allWinningNums = ''
    for i in range(5):
        allWinningNums += str(winningNumbers[i]) + ' '
    allWinningNums += 'and ' + str(winningPowerball)
    print(allWinningNums.ljust(21), end='')

    # NOTE: Sets are not ordered, so it doesn't matter what order the
    # integers in set(numbers) and set(winningNumbers) are.
    if (set(numbers) == set(winningNumbers) 
        and powerball == winningPowerball):
            print()
            print('\nYou have won the Powerball Lottery! Congratulations,')
            print('\nYou would be a billionaire if this was not simulated!')
            break
    else:
        print ('\nYou lost, Better luck next time.')

print('\nYou have wasted', price)
print('Thank you for playing!\n')



