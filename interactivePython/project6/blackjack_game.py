"""
|-------------------------------------------------------------------------------
| blackjack_game.py
|-------------------------------------------------------------------------------
|
| Author:   Alwin Tareen
| Created:  Jun 28, 2015
| Execute:  python3 blackjack_game.py
|
| This program implements the blackjack game.
|
| Codeskulptor link:
| https://py2.codeskulptor.org/#user6-AemuZnJl43-82.py
|
"""

import simplegui
import random

# load card sprite - 949x392 - source: jfitz.com
CARD_SIZE = (73, 98)
CARD_CENTER = (36.5, 49)
card_images = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/cards.jfitz.png")

CARD_BACK_SIZE = (71, 96)
CARD_BACK_CENTER = (35.5, 48)
card_back = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/card_back.png")    

# initialize some useful global variables
in_play = False
message = ''
outcome = ''
score = 0
player_hand = None
dealer_hand = None
casino_deck = None

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
# define hand class
class Hand:
    def __init__(self):
        self.cards = []

    def __str__(self):
        ans = [str(i) for i in self.cards]
        return str(ans)

    def add_card(self, card):
        self.cards.append(card)

    # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
    def get_value(self):
        self.hand_value = 0
        ace_exist = False
        for one_item in self.cards:
            self.hand_value += VALUES.get(one_item.get_rank())
            if (one_item.get_rank() == 'A'):
                ace_exist = True
        if not ace_exist:
            return self.hand_value
        else:
            if self.hand_value <= 21:
                return self.hand_value + 10
            else:
                return self.hand_value

    def busted(self):
        pass	# replace with your code
    
    def draw(self, canvas, position):
        for dealt_card in self.cards:
            dealt_card.draw(canvas, position)
            position[0] += 100
 
        
# define deck class
class Deck:
    def __init__(self):
        self.full_deck = [Card(suit, rank) for suit in SUITS for rank in RANKS]

    # add cards back to deck and shuffle
    def shuffle(self):
        random.shuffle(self.full_deck)

    def deal_card(self):
        return self.full_deck.pop()
    
    def __str__(self):
        res = [str(i) for i in self.full_deck]
        return str(res)



#define event handlers for buttons
def deal():
    global message, outcome, in_play, player_hand, dealer_hand, casino_deck, score

    if (in_play):
        outcome = 'Pressed Deal, you lose.'
        message = 'New deal?'
        score -= 1
        in_play = False
    else:    
        casino_deck = Deck()    
        casino_deck.shuffle()
    
        player_hand = Hand()
        dealer_hand = Hand()
    
        player_hand.add_card(casino_deck.deal_card())    
        dealer_hand.add_card(casino_deck.deal_card())
        player_hand.add_card(casino_deck.deal_card())    
        dealer_hand.add_card(casino_deck.deal_card())
    
        outcome = ''
        message = 'Hit or stand?'
        in_play = True
    
        print 'Player hand: ', player_hand
        print 'Player hand value: ', player_hand.get_value()
        print ''
        print 'Dealer hand: ', dealer_hand
        print 'Dealer hand value: ', dealer_hand.get_value()
        print ''

    
def hit():
    global message, outcome, in_play, player_hand, score
    
    # if the hand is in play, hit the player
    if (in_play):
        if (player_hand.get_value() <= 21):
            player_hand.add_card(casino_deck.deal_card())
    
        print 'Player hand: ', player_hand
        print 'Player hand value: ', player_hand.get_value()
        print ''        
    
        # if busted, assign an message to outcome, update in_play and score
        if (player_hand.get_value() > 21):
            outcome = 'You went bust and lose.'
            message = 'New deal?'
            score -= 1
            in_play = False
            print 'You have busted'
            print outcome
       
def stand():
    global message, outcome, in_play, dealer_hand, score

    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more
    if (in_play):
        while (dealer_hand.get_value() < 17):
            dealer_hand.add_card(casino_deck.deal_card())
            print 'Dealer hand: ', dealer_hand
            print 'Dealer hand value: ', dealer_hand.get_value()
            print ''

        # assign a message to outcome, update in_play and score
        if (dealer_hand.get_value() > 21):
            outcome = 'Dealer went bust, you win.'
            score += 1
            print 'Dealer went bust'
        elif (player_hand.get_value() <= dealer_hand.get_value()):
            outcome = 'You lose.'
            score -= 1
        else:
            outcome = 'You win.'
            score += 1
        message = 'New deal?'
        in_play = False
        
        print outcome

# draw handler    
def draw(canvas):
    # test to make sure that card.draw works, replace with your code below
    # card = Card("S", "A")
    # card.draw(canvas, [300, 300])
    canvas.draw_text("Blackjack", (100, 100), 30, "Blue")
    canvas.draw_text("Score:", (400, 100), 20, "Black")    
    canvas.draw_text(str(score), (500, 100), 20, "Black")
    canvas.draw_text("Dealer", (100, 175), 20, "Black")
    canvas.draw_text(outcome, (300, 175), 20, "Black")  
    canvas.draw_text("Player", (100, 375), 20, "Black")
    canvas.draw_text(message, (300, 375), 20, "Black")
    dealer_hand.draw(canvas, [100, 200])
    player_hand.draw(canvas, [100, 400])
    if (in_play):
        canvas.draw_image(card_back, CARD_BACK_CENTER, CARD_BACK_SIZE, [100 + CARD_BACK_CENTER[0], 200 + CARD_BACK_CENTER[1]], CARD_BACK_SIZE)

    
# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)

# deal an initial hand

# get things rolling
frame.start()
deal()

