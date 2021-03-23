import argparse

instructions = "The computer will select a card at random, you as the player, need to guess whether the next drawn card is higher or lower than the selected card.\n" "If your guess is correct, you will win a point, if you are incorrect, you will lose a point!"

parser = argparse.ArgumentParser(description="How to Play")
parser.add_argument("--instructions", help="instructions")

args = parser.parse_args()

if args.instructions:
    print(instructions)
else:
    print("You're fine")
