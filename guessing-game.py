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


def clear_screen():
    time.sleep(2)
    os.system("cls")


def createDeck():
    value = 1
    for card in Cards:
        for suit in Suits:
            Deck.append([card + " of " + suit, value])
        value = value + 1
    random.shuffle(Deck)
    return Deck


class Player:

    def __init__(self):
        self.Score = 0

    def setName(self):
        global playerName
        playerName = input("Please enter your name: ")
        if playerName == "--help":
            clear_screen()
            print("RULES OF THE GAME\n")
            time.sleep(1)
            print("The computer will select a card at random, you as the player, need to guess whether the next drawn card is higher or lower than the selected card.\n" "If your guess is correct, you will win a point, if you are incorrect, you will lose a point!")
            time.sleep(2)
            resume_play = input("To continue playing type --resume ")
            if resume_play == "--resume":
                clear_screen()
                self.setName()
        else:
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
        clear_screen()

    def winRound(self):
        print("Correct!")
        print(f"The card was {card2[0]}")
        self.Score += 1
        discardPile.append([card1, card2])
        clear_screen()

    def drawRound(self):
        print("It 's a draw!")
        print(f"The card was {card2[0]}")
        discardPile.append([card1, card2])
        clear_screen()

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
        elif guessCard == "--help":
            self.instructions()
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
            clear_screen()
            self.drawCards()
            self.playGame()
        elif replay == "n":
            print(
                f"Thank you for playing, {playerName}! Your final score is {self.Score}")
            text = input("Press any key + ENTER to quit: ")
            for i in text:
                if i > "0":
                    return
        elif replay == "--help":
            clear_screen()
            print("RULES OF THE GAME\n")
            time.sleep(1)
            print("The computer will select a card at random, you as the player, need to guess whether the next drawn card is higher or lower than the selected card.\n" "If your guess is correct, you will win a point, if you are incorrect, you will lose a point!")
            time.sleep(2)
            resume_play = input("To continue playing type --resume ")
            if resume_play == "--resume":
                clear_screen()
                self.playAgain()
            else:
                print("Invalid Response. Please enter Y to play again, or N to exit")
                self.playAgain()

    def instructions(self):
        clear_screen()
        print("RULES OF THE GAME\n")
        time.sleep(1)
        print("The computer will select a card at random, you as the player, need to guess whether the next drawn card is higher or lower than the selected card.\n" "If your guess is correct, you will win a point, if you are incorrect, you will lose a point!")
        time.sleep(2)
        resume_play = input("To continue playing type --resume ")
        if resume_play == "--resume":
            clear_screen()
            print(f"{playerName}, your current score is {self.Score}")
            print(f"The current card is {card1[0]}")
            self.guessCard()


Player = Player()


if __name__ == "__main__":
    Player.setName()
    Player.playGame()

# figure out instructions
