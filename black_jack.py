import random

class Card():

    def __init__(self, card_type):
        self.card_type = card_type
        if card_type in ['J', 'Q', 'K']:
            self.value = 10
        elif card_type == 'A':
            self.value = 11
        else:
            self.value = int(card_type)


class Deck():

    def __init__(self):
        self.initialise()

    def initialise(self):
        self.deck_values = self.create_deck()
        self.deck = [Card(card) for card in self.deck_values]

    def create_deck(self):
        deck = []
        for i in range(2, 11):
            deck.extend([str(i)] * 4)
        deck.extend(['J'] * 4)
        deck.extend(['Q'] * 4)
        deck.extend(['K'] * 4)
        deck.extend(['A'] * 4)
        return deck

    def get_card(self):
        random.shuffle(self.deck)
        print (len(self.deck))
        return self.deck.pop()

    def __str__(self):
        print (len(self.deck))

class Player():

    def __init__(self):
        self.balance = 0
        self.bet = 0

    def start_game(self, deck):
        self.cards = []
        self.sum = 0
        for i in range(0, 2):
            card = deck.get_card()
            self.cards.append(card.card_type)
            self.sum += card.value
            print(f"Card fetched for Player is {self.cards[-1]}, sum is {self.sum}")

    def add_card(self, card):
        self.cards.append(card.card_type)
        self.sum += card.value
        self.total_sum()
        print(f"Card fetched for Player is {self.cards[-1]}, sum is {self.sum}")

    def total_sum(self):
        if self.sum <= 21:
            return
        else:
            if 'A' in self.cards:
                self.cards[self.cards.index('A')] = '1'
                self.sum -= 10
            return

    def deposit(self, amount):
        self.balance += amount
        print (f"Current Balance is {self.balance}")

    def withdraw(self, amount):
        if amount < self.balance:
            print(f"Insuiffient Funds!!! Current Balance is {self.balance}")
        else:
            self.balance -= amount
            print (f"Withdrawal successful!!! Current Balance is {self.balance}")

    def betting(self, amount):
        if amount > self.balance:
            print(f"Insuiffient Funds!!! Current Balance is {self.balance}")
            return 0
        else:
            self.bet = amount
            self.balance -= amount
            print (f"Bet Placed!!! Current Balance is {self.balance}")
            return 1

class Computer():

    def __init__(self):
        self.balance = 0
        print ("Computer is ready to play")

    def start_game(self, deck):
        self.cards = []
        self.sum = 0
        card = deck.get_card()
        self.cards.append(card.card_type)
        self.sum += card.value
        print(f"Card fetched for Computer is {self.cards[-1]}, sum is {self.sum}")
        self.hidden_card = deck.get_card()
        print(f"Hidden Card is fetched and kept seperately")

    def add_hidden_card(self):
        return self.add_card(self.hidden_card)

    def add_card(self, card):
        self.cards.append(card.card_type)
        self.sum += card.value
        self.total_sum()
        print(f"Card fetched for Computer is {self.cards[-1]}, sum is {self.sum}")

    def total_sum(self):
        if self.sum <= 21:
            return
        else:
            if 'A' in self.cards:
                self.cards[self.cards.index('A')] = '1'
                self.sum -= 10
            return

    def add_amount(self, amount):
        self.balance += amount
        print (f"Computer Current Balance is {self.balance}")

    def show_earnings(self):
        print (f"Computer Current Balance is {self.balance}")

class BlackJack():

    def __init__(self):
        print("Welcome to Black Jack Game!!")
        self.player = Player()
        self.computer = Computer()

    def start_game(self):
        self.deck = Deck()
        self.player.start_game(self.deck)
        self.computer.start_game(self.deck)

    def get_money_from_player(self):
        while True:
            try:
                amount = int(input("How much money you want to deposit:"))
            except:
                print ("Not a valid input!")
                continue
            else:
                self.player.deposit(amount)
                break

    def play_time(self):
        self.get_money_from_player()
        while True:
            try:
                bet = int(input("How much you want to bet on this game?"))
                if self.player.betting(bet):
                    self.start_game()
                    mode = 0
                    while True:
                        if self.player.sum == 21:
                            print (f"Player wins!! It's straight BlackJack!!")
                            self.player.deposit(self.player.bet * 2)
                            mode = 1 # player won
                            break
                        elif self.player.sum > 21:
                            print (f"Player have lost this game!!")
                            print (f"You have lost {self.player.bet} bucks")
                            mode = -1 # player lost
                            break
                        player_choice = input("You want to hit or stand?")
                        if player_choice == 'hit':
                            card = self.deck.get_card()
                            self.player.add_card(card)
                            continue
                        elif player_choice == 'stand':
                            print (f"Sum for player is {self.player.sum}")
                            break

                    if mode != 0:
                        continue
                    self.computer.add_hidden_card()
                    while True:
                        if self.computer.sum == 21:
                            print (f"Computer wins!! It's straight BlackJack!!")
                            self.computer.add_amount(self.player.bet * 2)
                            mode = 1 # player won
                            break
                        elif self.computer.sum > 21:
                            print (f"Computer have lost this game!!")
                            print (f"You have lost {self.player.bet * 2} bucks")
                            self.computer.add_amount(self.player.bet * -2)
                            self.player.deposit(self.player.bet * 2)
                            mode = -1 # player lost
                            break
                        elif self.computer.sum in range(self.player.sum + 1,21):
                            print ("Computer wins!!!")
                            print (f"Player have lost this game of {self.player.bet} bet, current balance is {self.player.balance}")
                            self.computer.add_amount(self.player.bet)
                            break
                        card = self.deck.get_card()
                        self.computer.add_card(card)

                else:
                    self.get_money_from_player()
                    continue

            except:
                print ("Not a valid input!!")
                continue


if __name__ == "__main__":
    black_jack = BlackJack()
    black_jack.play_time()