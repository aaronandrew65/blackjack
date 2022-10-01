
from random import shuffle

playing = True

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10, 
            'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank= rank

    def __str__(self):
        return self.rank  + ' of ' + self.suit


class Deck:
    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank))

    def __str__(self):
        deck_comp = ''
        for card in self.deck:
            deck_comp += '\n ' + card.__str__()
        return 'The deck has ' + deck_comp
    
    def shufffle(self):
        shuffle(self.deck)

    def deal(self):
        single_card = self.deck.pop()
        return single_card

class Hand:

    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def addCard(self, card):
        self.cards.append(card)
        self.value += values[card.rank]
        if card.rank == 'Ace':
            self.aces += 1

    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1

class Chips:
    def __init__(self):
        self.total= 100
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet

def take_bet(chips):

    while True:
        try:
            chips.bet = int(input('How many chips would you like to bet? '))
        except ValueError:
            print('Sorry! Please type in a number:  ')
        else:
            if chips.bet > chips.total:
                print('Your bet cannot exceed 100.')
            else:
                break
def hit(deck, hand):
    hand.addCard(deck.deal())
    hand.adjust_for_ace()



def hit_or_stay(deck, hand):
    global playing

    while True:
        ask = input('Would you like to hit or stay? Please enter h or s: ')

        if ask.lower() == 'h':
            hit(deck, hand)
        elif ask.lower() == 's':
            print('Dealers turn..')
            playing = False
        else:
            print('not an option bud')
            continue
        break

def show_some(player,dealer):
    print('\nDealers Hand: ')
    print(' card hidden')
    print('',dealer.cards[1])
    print('\nPlayers hand: ', player.cards[0],player.cards[1], sep='\n ')

def show_all(player,dealer):
    print('\nDealers Hand: ', dealer.cards, sep='\n')
    print('Dealers Hand = ', dealer.value)
    print('\nPlayers Hand: ', player.cards, sep='\n')
    print('Players hand = ', player.value)

def player_busts(player, dealer, chips):
    print('Player busts!')
    chips.lose_bet()

def player_wins(player, dealer, chips):
    print('Player wins!')
    chips.win_bet()

def dealer_busts(player, dealer, chips):
    print('Dealer busts!')
    chips.win_bet()

def Dealer_wins(player, dealer, chips):
    print('Dealer wins!')
    chips.lose_bet()

def push(player, dealer):
    print('Its a push!')


while True:
    print('Welcome to Blackjack!')

    deck = Deck()
    deck.shufffle()

    player_hand = Hand()
    player_hand.addCard(deck.deal())
    player_hand.addCard(deck.deal())

    dealer_hand = Hand()
    dealer_hand.addCard(deck.deal())
    dealer_hand.addCard(deck.deal())

    player_chips = Chips()

    take_bet(player_chips)

    show_some(player_hand, dealer_hand)

    playing = True
    while playing:

        hit_or_stay(deck, player_hand)
        show_some(player_hand, dealer_hand)

    
        if player_hand.value > 21:
            player_busts(player_hand, dealer_hand, player_chips)
            break
        if player_hand.value <= 21:

            while dealer_hand.value < 17:
                hit(deck, dealer_hand)

        show_all(player_hand, dealer_hand)

        if dealer_hand.value > 21:
            dealer_busts(player_hand, dealer_hand, player_chips)

        elif dealer_hand.value < player_hand.value:
            player_wins(player_hand, dealer_hand, player_chips)

        elif dealer_hand.value > player_hand.value:
            Dealer_wins(player_hand, dealer_hand, player_chips)
        
        if player_hand.value > 21:
            player_busts(player_hand, dealer_hand, player_chips)
    print('\nPLayers winnings: ', player_chips.total)

    new_game = (input('Would you like to play again? y/n '))
    if new_game.lower() == 'y':
        playing = True
    else:
        print('Thank you for playing!')
        break
