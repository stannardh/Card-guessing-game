import random
import os
import sys
import time
import argparse
Cards = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9",
         "10", "J", "Q", "K"]

Suits = ["Clubs", "Hearts", "Diamonds", "Spades"]

Deck = []

discardPile = []


def createDeck():
    value = 1
    for card in Cards:
        for suit in Suits:
            Deck.append([card + " of " + suit, value])
        value = value + 1
    random.shuffle(Deck)
    return Deck

# checking to see if the cards print correctly and the list items can be accessed


""" cardDeck = createDeck()
print(cardDeck)
card1 = cardDeck.pop()
card2 = cardDeck.pop()
print(card1)
print(card2)
print(card1[0])
print(card2[0])
print(card1[1])
print(card2[1]) """


class Player:

    def __init__(self):
        self.Score = 0

    def setName(self):
        global playerName
        playerName = input("Please enter your name: ")
        return playerName

    def drawCards(self):
        cardDeck = createDeck()
        global card1
        global card2
        card1 = cardDeck.pop()
        card2 = cardDeck.pop()

    def loseRound(self):
        print("Nope!")
        print(f"The card was {card2[0]}")
        self.Score -= 1
        discardPile.append([card1, card2])
        time.sleep(2)
        os.system("cls")

    def winRound(self):
        print("Correct!")
        print(f"The card was {card2[0]}")
        self.Score += 1
        discardPile.append([card1, card2])
        time.sleep(2)
        os.system("cls")

    def drawRound(self):
        print("It 's a draw!")
        print(f"The card was {card2[0]}")
        discardPile.append([card1, card2])
        time.sleep(2)
        os.system("cls")

    def guessCard(self):
        guessCard = input(
            f"{playerName}, please guess higher (h) or lower (l): ").lower()
        if guessCard == "h" and card1[1] > card2[1]:
            self.loseRound()
        elif guessCard == "l" and card1[1] < card2[1]:
            self.loseRound()
        elif guessCard == "h" and card1[1] < card2[1]:
            self.winRound()
        elif guessCard == "l" and card1[1] > card2[1]:
            self.winRound()
        elif guessCard == "l" and card1[1] == card2[1]:
            self.drawRound()
        elif guessCard == "h" and card1[1] == card2[1]:
            self.drawRound()
        else:
            print("Invalid response, please enter 'h' or 'l'")
            self.guessCard()

    def playGame(self):
        turn = 0
        while turn < 10:
            print(f"Your current score is {self.Score}")
            Player.drawCards()
            print(f"The current card is {card1[0]}")
            self.guessCard()
            turn += 1

        self.playAgain()

    def playAgain(self):
        replay = input(
            f"{playerName}, your final score is {self.Score}, would you like to play again? Y/N: ").lower()
        if replay == "y":
            self.Score = 0
            os.system("cls")
            self.drawCards()
            self.playGame()
        elif replay == "n":
            print(
                f"Thank you for playing, {playerName}! Your final score is {self.Score}")
            text = input("Press any key + ENTER to quit: ")
            for i in text:
                if i > "0":
                    return
        else:
            print("Invalid Response. Please enter Y to play again, or N to exit")
            self.playAgain()

    def Helper(self):
        instructions = "The computer will select a card at random, you as the player, need to guess whether the next drawn card is higher or lower than the selected card.\n" "If your guess is correct, you will win a point, if you are incorrect, you will lose a point!"

        parser = argparse.ArgumentParser(description="How to Play")
        parser.add_argument("--instructions", help="instructions")

        args = parser.parse_args()

        if args.instructions:
            print(instructions)
        else:
            print("You're fine")


Player = Player()
Player.setName()
Player.playGame()

# figure out instructions
