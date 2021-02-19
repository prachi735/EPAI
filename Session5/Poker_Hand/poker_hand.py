# http://www.mathcs.emory.edu/~cheung/Courses/170/Syllabus/10/pokerCheck.html
from random import sample
from typing import Text

VALS = ['2', '3', '4', '5', '6', '7', '8',
        '9', '10', 'jack', 'queen', 'king', 'ace']
SUITS = ['spades', 'clubs', 'hearts', 'diamonds']

SORT_ORDER = {'2': 13, '3': 12, '4': 11, '5': 10, '6': 9, '7': 8, '8': 7,
              '9': 6, '10': 5, 'jack': 4, 'queen': 3, 'king': 2, 'ace': 1}

FULL_DECK = [(v, s) for v in VALS for s in SUITS]


class Poker_Simulation:

    def __init__(self) -> None:
        self.deck = []
        self.player1 = []
        self.player2 = []

    def get_deck_with_lamnbda(self):
        '''
        single expression that includes lambda, zip and map functions to select create 52 cards in a deckfor
        '''
        t = [item for sublist in list(
            map(lambda a: [(a, b) for b in SUITS], VALS)) for item in sublist]
        return t

    def get_deck(self):
        '''normal function without using lambda, zip, and map function to create 52 cards in a deck
        '''
        #self.deck = [(v, s) for v in VALS for s in SUITS]
        return [(v, s) for v in VALS for s in SUITS]

    def create_a_hand(self, no_of_cards=-1):
        '''
        randomly create a hand from the cards left in deck
        '''
        if no_of_cards == -1:
            no_of_cards = sample([3, 4, 5], 1)[0]
        hand = sample(self.deck, no_of_cards)
        # remove the dealt cards from deck
        self.deck = list(filter(lambda i: i not in hand, self.deck))

        return hand

    def is_valid_hand(self, cards: list, min: int = 3, max: int = 5) -> bool:
        if len(cards) == len(set(cards)):
            if min <= len(cards) <= max:
                c_stat = [True for x in cards if x in FULL_DECK]
                if len(cards) == len(c_stat) and all(c_stat):
                    return (True, "Valid hand")
                else:
                    return (False, "Invalid hand: Contains invalid cards", [True for x in cards if x in FULL_DECK])
            else:
                return (False, "Invalid hand: Contains wrong number of cards")
        else:
            return (False, "Invalid hand: Contains repeating cards")

    def sort_by_suits(self, cards: list) -> bool:
        '''
        returns the cards list sorted by suits
        '''
        cards.sort(key=lambda x: x[1])
        return cards

    def sort_by_rank(self, cards: list) -> list:
        '''
        returns the card list sorted rank
        '''
        cards.sort(key=lambda x: SORT_ORDER[x[0]])
        return cards

    def compare_cards(self, card1: tuple, card2: tuple) -> str:
        '''
        comapre the 2 cards and returns a staus code:
            0: nothing common in cards
            1: both cards are same
            2: cards have same rank
            3: cards belong to same suit
        '''
        status = [card1[0] == card2[0], card1[1] == card2[1]]
        if status == [True, True]:
            return 1
        elif status == [True, False]:
            return 2
        elif status == [False, True]:
            return 3
        else:
            return 0

    def is_flush(self, cards: list) -> bool:
        '''
        All cards belong to same suit
        '''
        if len(cards) == 5 and self.is_valid_hand(cards)[0]:
            cards = self.sort_by_suits(cards)
            return cards[0][1] == cards[4][1]
        else:
            return False

    def is_straight(self, cards: list) -> bool:
        '''
            All cards are increasing continuously in rank
        '''
        if len(cards) == 5 and self.is_valid_hand(cards)[0]:
            cards = self.sort_by_rank(cards)
            if cards[0][0] == 'ace':
                a = cards[1][0] == '2' and cards[2][0] == '3' and cards[3][0] == '4' and cards[4][0] == '5'
                b = cards[1][0] == 'king' and cards[2][0] == 'queen' and cards[3][0] == 'jack' and cards[4][0] == '10'
                return a or b
            else:
                rank = VALS.index(cards[0][0])
                for i in range(5):
                    if cards[i][0] != VALS[rank]:
                        return False
                    rank -= 1
                return True
        else:
            return False

            
    def is_straight_flush(self, cards: list) -> bool:
        '''
        all cards are in sequence
        and of same suit
        '''
        return self.is_straight(cards) and self.is_flush(cards)

    def is_royal_flush(self, cards: list) -> bool:
        '''
        Royal Flush is the Highest Straight Flush
        and cards are (A, K, Q, J, 10)
        '''
        if len(cards) == 5 and self.is_valid_hand(cards)[0]:
            cards = self.sort_by_rank(cards)
            return self.is_straight_flush(cards) and cards[0][0] == "ace"
        else:
            return False

    def is_four_of_a_kind(self, cards: list) -> bool:
        '''    
        4 cards have the same rank
        The 5th card can be of any rank 
        '''
        if len(cards) == 5 and self.is_valid_hand(cards)[0]:
            cards = self.sort_by_rank(cards)
            # check for x x x x a
            a = cards[0][0] == cards[1][0] == cards[2][0] == cards[3][0]
            # check for a x x x x
            b = cards[1][0] == cards[2][0] == cards[3][0] == cards[4][0]
            return a or b

        else:
            return False

    def is_full_house(self, cards: list) -> bool:
        '''    
        3 cards have the same rank and
        2 remaining cards have the same rank 
        '''
        if len(cards) == 5 and self.is_valid_hand(cards)[0]:
            cards = self.sort_by_rank(cards)
            # Check for: x x x y y
            a = cards[0][0] == cards[1][0] == cards[2][0] and cards[3][0] == cards[4][0]
            # Check for: x x y y y
            b = cards[0][0] == cards[1][0] and cards[2][0] == cards[3][0] == cards[4][0]
            return a or b
        else:
            return False

    def is_three_of_a_kind(self, cards: list) -> bool:
        '''    
        3 cards have the same rank
        Plus 2 unmatched cards 
        '''
        if len(cards) == 5 and self.is_valid_hand(cards)[0]:
            cards = self.sort_by_rank(cards)

            if self.is_full_house(cards) or self.is_four_of_a_kind(cards):
                return False

            # Check for: x x x a b || a x x x b || a b x x x
            for i in range(3):
                if cards[i][0] == cards[i+1][0] == cards[i+2][0]:
                    return True
            return False
        else:
            return False

    def is_two_pair(self, cards: list) -> bool:
        '''    
        2 cards have the same rank
        2 other cards have the same rank that is different from the first pair
        The 5th card can be of any unmatched rank 
        '''
        if len(cards) == 5 and self.is_valid_hand(cards)[0]:
            cards = self.sort_by_rank(cards)

            if self.is_full_house(cards) or self.is_four_of_a_kind(cards) or self.is_three_of_a_kind(cards):
                return False

            # a x x y y
            a = cards[1][0] == cards[2][0] and cards[3][0] == cards[4][0]
            # x x y y a
            b = cards[0][0] == cards[1][0] and cards[2][0] == cards[3][0]
            # x x a y y
            c = cards[0][0] == cards[1][0] and cards[3][0] == cards[4][0]
            return a or b or c

        else:
            return False

    def is_one_pair(self, cards: list) -> bool:
        '''    
        2 cards have the same rank
        The 3 other cards must be of unmatched rank 
        '''
        if len(cards) == 5 and self.is_valid_hand(cards)[0]:
            cards = self.sort_by_rank(cards)

            if self.is_full_house(cards) or self.is_four_of_a_kind(cards) or self.is_three_of_a_kind(cards) or self.is_two_pair(cards):
                return False

            # x x a b c
            # a x x b c
            # a b x x c
            # a b c x x
            for i in range(4):
                if cards[i][0] == cards[i+1][0]:
                    return True
            return False
        else:
            return False

    def get_highest_card(self, cards: list) -> bool:
        '''
        get the highest card by rank
        '''
        cards = self.sort_by_rank(cards)
        return cards[0]

    def get_poker_winner(self, set1, set2):
        '''
        return the winner
        '''
        # the order of card set winning value
        win_order = [
            self.is_one_pair,
            self.is_two_pair,
            self.is_three_of_a_kind,
            self.is_straight,
            self.is_flush,
            self.is_full_house,
            self.is_four_of_a_kind,
            self.is_straight_flush,
            self.is_royal_flush
            ]

        set_vals = []

        for c_set in [set1, set2]:
            # find the card set value : min of win_order
            check_set = [f(c_set) for f in win_order]
            set_vals.append(
                max([i for i, val in enumerate(check_set) if val], default=-1))

        if(set_vals[0]!=-1):
            print('Player1\'s hand is a', win_order[set_vals[0]].__name__[3:])
        if(set_vals[1]!=-1):
            print('Player2\'s hand is a', win_order[set_vals[1]].__name__[3:])

        # find the winning card set
        if set_vals[0] > set_vals[1]:
            return 'Player1 is winner!!!'
        elif set_vals[1] > set_vals[0]:
            return 'Player2 is winner!!!'
        # Both player have similar hand so we check cards with higher rank
        while(0 < len(set1) and 0 < len(set2)):
            set1_high = self.get_highest_card(set1)
            set2_high = self.get_highest_card(set2)
            if set1_high < set2_high:
                return 'Player1 is winner!!!'
            elif set2_high < set1_high:
                return 'Player2 is winner!!!'
            set1.remove(set1_high)
            set2.remove(set2_high)
        return 'It\'s a draw!!! '


def main():
    g = Poker_Simulation()
    g.deck = g.get_deck()
    g.player1 = g.create_a_hand(5)
    g.player2 = g.create_a_hand(5)
    print("Player1's hand: ", g.player1)
    print("Player2's hand: ", g.player2)
    print(g.get_poker_winner(g.player1, g.player2))
    print("\n")
    

if __name__ == "__main__":
    for _ in range(1):#number of simulations
        main()
