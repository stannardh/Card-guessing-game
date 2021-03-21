import random
import os

Cards = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9",
         "10", "J", "Q", "K"]

Suits = ["Clubs", "Hearts", "Diamonds", "Spades"]

Deck = []

discardPile = []


def game_instructions():
    "The computer will select a card at random, you as the player, need to guess whether the next drawn card is higher or lower than the selected card.  If your guess is correct, you will win a point, if you are incorrect, you will lose a point! Happy playing!"
    print(game_instructions.__doc__)


help(game_instructions)


def createDeck():
    value = 1
    for card in Cards:
        for suit in Suits:
            Deck.append([card + " of " + suit, value])
        value = value + 1
    random.shuffle(Deck)
    return Deck


cardDeck = createDeck()
print(cardDeck)
card1 = cardDeck.pop()
card2 = cardDeck.pop()
print(card1)
print(card2)
print(card1[0])
print(card2[0])
print(card1[1])
print(card2[1])


class Player:

    def __init__(self, Hand=[]):
        self.Score = 10
        self.Hand = Hand

    def setName(self):
        global playerName
        playerName = input("Please enter your name: ")
        return playerName

    def drawCards(self):
        cardDeck = createDeck()
        global card1
        global card2
        card1 = [cardDeck.pop()]
        card2 = [cardDeck.pop()]

    def loseRound(self):
        print("Nope!")
        print(f"The card was {card2[0]}")
        self.playAgain()
        discardPile.append([card1, card2])
        self.Score -= 1

    def winRound(self):
        print("Correct!")
        print(f"The card was {card2[0]}")
        self.playAgain()
        discardPile.append([card1, card2])
        self.Score += 1

    def drawRound(self):
        print("It 's a draw!")
        print(f"The card was {card2[0]}")
        self.playAgain()
        discardPile.append([card1, card2])

    def guessCard(self):
        guessCard = input(
            f"{playerName}, please guess higher or lower: ").lower()
        if guessCard == "higher" and card1[1] > card2[1]:
            self.loseRound()
        elif guessCard == "lower" and card1[1] < card2[1]:
            self.loseRound()
        elif guessCard == "higher" and card1[1] < card2[1]:
            self.winRound()
        elif guessCard == "lower" and card1[1] > card2[1]:
            self.winRound()
        elif guessCard == "lower" and card1[1] == card2[1]:
            self.drawRound()
        elif guessCard == "higher" and card1[1] == card2[1]:
            self.drawRound()
        else:
            print("Invalid response, please enter 'Higher' or 'Lower'")
            self.guessCard()

    def playGame(self):
        os.system("cls")
        print(f"Your current score is {self.Score}")
        Player.drawCards()
        print(f"The current card is {card1[0]}")
        self.guessCard()

    def playAgain(self):
        replay = input(
            f"{playerName}, would you like to play again? Y/N: ").lower()
        if replay == "y":
            Player.drawCards()
            self.playGame()
        else:
            print(
                f"Thank you for playing, {playerName}! Your final score is {self.Score}")


Player = Player()
Player.setName()

while (True):
    Player.playGame()
