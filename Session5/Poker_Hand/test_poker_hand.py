import pytest
from poker_hand import *

deck = [('2', 'spades'), ('2', 'clubs'), ('2', 'hearts'), ('2', 'diamonds'), ('3', 'spades'), ('3', 'clubs'), ('3', 'hearts'), ('3', 'diamonds'), ('4', 'spades'), ('4', 'clubs'), ('4', 'hearts'), ('4', 'diamonds'), ('5', 'spades'), ('5', 'clubs'), ('5', 'hearts'), ('5', 'diamonds'), ('6', 'spades'), ('6', 'clubs'), ('6', 'hearts'), ('6', 'diamonds'), ('7', 'spades'), ('7', 'clubs'), ('7', 'hearts'), ('7', 'diamonds'), ('8', 'spades'),
        ('8', 'clubs'), ('8', 'hearts'), ('8', 'diamonds'), ('9', 'spades'), ('9', 'clubs'), ('9', 'hearts'), ('9', 'diamonds'), ('10', 'spades'), ('10', 'clubs'), ('10', 'hearts'), ('10', 'diamonds'), ('jack', 'spades'), ('jack', 'clubs'), ('jack', 'hearts'), ('jack', 'diamonds'), ('queen', 'spades'), ('queen', 'clubs'), ('queen', 'hearts'), ('queen', 'diamonds'), ('king', 'spades'), ('king', 'clubs'), ('king', 'hearts'), ('king', 'diamonds'), ('ace', 'spades'), ('ace', 'clubs'), ('ace', 'hearts'), ('ace', 'diamonds')]


def test_get_deck_with_lamnbda():
    g = Poker_Simulation()
    t_deck = g.get_deck_with_lamnbda()
    assert t_deck == deck


def test_get_deck():
    g = Poker_Simulation()
    g.deck = g.get_deck()
    assert g.deck == deck


def test_create_a_hand_length():
    g = Poker_Simulation()
    g.deck = g.get_deck()
    hand = g.create_a_hand()
    assert 3 <= len(hand) <= 5


def test_create_a_hand_valid_cards():
    g = Poker_Simulation()
    g.deck = g.get_deck()
    hand = g.create_a_hand()
    assert all([True for c in hand if c in deck])


def test_create_a_hand_deck_update():
    g = Poker_Simulation()
    g.deck = g.get_deck()
    hand = g.create_a_hand()
    assert not any([True for c in hand if c in g.deck])


def test_is_valid_hand_unique_cards():
    g = Poker_Simulation()
    g.deck = g.get_deck()
    hand = [('5', 'spades'), ('8', 'clubs'), ('ace', 'spades'),
            ('2', 'hearts'), ('3', 'hearts')]
    assert g.is_valid_hand(hand)


def test_is_valid_hand_rep_cards():
    g = Poker_Simulation()
    g.deck = g.get_deck()
    hand = [('5', 'spades'), ('8', 'clubs'), ('ace', 'spades'),
            ('2', 'hearts'), ('8', 'clubs')]
    #assert len(hand) == len(set(hand))
    assert not g.is_valid_hand(hand)[0]


def test_is_valid_hand_from_deck():
    g = Poker_Simulation()
    g.deck = g.get_deck()
    hand = [('9', 'clubs'), ('7', 'hearts'), ('5', 'diamonds'),
            ('queen', 'spades'), ('6', 'clubs')]
    assert g.is_valid_hand(hand)[0]


def test_is_valid_hand_not_in_deck():
    g = Poker_Simulation()
    g.deck = g.get_deck()
    hand = [('6', 'clubs'), ('7', 'hearts'), ('5', 'diamonds'),
            ('queen', 'spades'), ('6', 'Blue')]
    assert not g.is_valid_hand(hand)[0]


def test_is_valid_hand_less_cards():
    g = Poker_Simulation()
    g.deck = g.get_deck()
    hand = [('jack', 'spades'), ('9', 'spades')]
    assert not g.is_valid_hand(hand)[0]


def test_is_valid_hand_many_cards():
    g = Poker_Simulation()
    g.deck = g.get_deck()
    hand = [('3', 'hearts'), ('2', 'clubs'), ('ace', 'spades'),
            ('queen', 'diamonds'), ('queen', 'spades'),
            ('queen', 'spades'), ('6', 'clubs')]
    assert not g.is_valid_hand(hand)[0]


def test_sort_by_suits():
    hand = [('2', 'diamonds'), ('2', 'spades'), ('4', 'diamonds'),
            ('6', 'spades'), ('3', 'diamonds')]
    g = Poker_Simulation()
    assert g.sort_by_suits(hand) == [(
        '2', 'diamonds'), ('4', 'diamonds'), ('3', 'diamonds'), ('2', 'spades'), ('6', 'spades')]


def test_sort_by_rank():
    hand = [('ace', 'clubs'), ('queen', 'hearts'), ('jack', 'clubs'),
            ('10', 'spades'), ('queen', 'diamonds')]
    g = Poker_Simulation()
    assert g.sort_by_rank(hand) == [('ace', 'clubs'), ('queen', 'hearts'),
                                    ('queen', 'diamonds'), ('jack', 'clubs'), ('10', 'spades')]


def test_is_royal_flush_valid():
    hand = [('queen', 'clubs'), ('10', 'clubs'),
            ('king', 'clubs'), ('ace', 'clubs'), ('ace', 'clubs')]
    g = Poker_Simulation()
    assert not g.is_royal_flush(hand)


def test_is_royal_flush_invalid1():
    hand = [('queen', 'clubs'), ('10', 'clubs'),
            ('king', 'clubs'), ('ace', 'clubs'), ('ace', 'hearts')]
    g = Poker_Simulation()
    assert not g.is_royal_flush(hand)


def test_is_royal_flush_invalid2():
    hand = [('queen', 'clubs'), ('10', 'clubs'),
            ('king', 'clubs'), ('ace', 'clubs'), ('king', 'clubs')]
    g = Poker_Simulation()
    assert not g.is_royal_flush(hand)


def test_is_straight_flush_valid():
    hand = [('10', 'clubs'), ('7', 'clubs'),
            ('9', 'clubs'), ('8', 'clubs'), ('6', 'clubs')]
    g = Poker_Simulation()
    assert g.is_straight_flush(hand)


def test_is_straight_flush_invalid():
    hand = [('10', 'clubs'), ('7', 'clubs'),
            ('9', 'clubs'), ('8', 'spades'), ('6', 'clubs')]
    g = Poker_Simulation()
    assert not g.is_straight_flush(hand)


def test_is_four_of_a_kind_valid():
    hand = [('4', 'spades'), ('4', 'diamonds'),
            ('4', 'hearts'), ('2', 'diamonds'), ('4', 'clubs')]
    g = Poker_Simulation()
    assert g.is_four_of_a_kind(hand)


def test_is_four_of_a_kind_invalid():
    hand = [('4', 'spades'), ('3', 'diamonds'),
            ('4', 'hearts'), ('2', 'diamonds'), ('4', 'clubs')]
    g = Poker_Simulation()
    assert not g.is_four_of_a_kind(hand)


def test_is_full_house_valid():
    hand = [('queen', 'hearts'), ('queen', 'diamonds'),
            ('2', 'diamonds'), ('2', 'hearts'), ('2', 'clubs')]
    g = Poker_Simulation()
    assert g.is_full_house(hand)


def test_is_full_house_invalid():
    hand = [('queen', 'hearts'), ('4', 'diamonds'),
            ('2', 'diamonds'), ('2', 'hearts'), ('2', 'clubs')]
    g = Poker_Simulation()
    assert not g.is_full_house(hand)


def test_is_flush_valid():
    hand = [('king', 'clubs'), ('7', 'clubs'),
            ('9', 'clubs'), ('8', 'clubs'), ('6', 'clubs')]
    g = Poker_Simulation()
    assert g.is_flush(hand)


def test_is_flush_invalid():
    hand = [('10', 'clubs'), ('7', 'clubs'),
            ('9', 'clubs'), ('8', 'spades'), ('6', 'clubs')]
    g = Poker_Simulation()
    assert not g.is_flush(hand)


def test_is_straight_valid():
    hand = [('10', 'clubs'), ('7', 'clubs'),
            ('9', 'clubs'), ('8', 'spades'), ('6', 'clubs')]
    g = Poker_Simulation()
    assert g.is_straight(hand)


def test_is_straight_invalid():
    hand = [('queen', 'clubs'), ('7', 'clubs'),
            ('9', 'clubs'), ('8', 'spades'), ('jack', 'clubs')]
    g = Poker_Simulation()
    assert not g.is_straight(hand)


def test_is_three_of_a_kind_valid():
    hand = [('8', 'spades'), ('8', 'hearts'), ('6', 'clubs'),
            ('9', 'hearts'), ('8', 'diamonds')]
    g = Poker_Simulation()
    assert g.is_three_of_a_kind(hand)


def test_is_three_of_a_kind_invalid():
    hand = [('8', 'spades'), ('8', 'hearts'), ('6', 'clubs'),
            ('9', 'hearts'), ('7', 'diamonds')]
    g = Poker_Simulation()
    assert not g.is_three_of_a_kind(hand)


def test_is_two_pair_valid():
    hand = [('4', 'diamonds'), ('5', 'clubs'), ('jack', 'diamonds'),
            ('4', 'spades'), ('jack', 'hearts')]
    g = Poker_Simulation()
    assert g.is_two_pair(hand)


def test_is_two_pair_invalid():
    hand = [('6', 'diamonds'), ('5', 'clubs'), ('jack', 'diamonds'),
            ('4', 'spades'), ('jack', 'hearts')]
    g = Poker_Simulation()
    assert not g.is_two_pair(hand)


def test_is_one_pair_valid():
    hand = [('ace', 'clubs'), ('5', 'spades'),
            ('4', 'hearts'), ('4', 'clubs'), ('9', 'spades')]
    g = Poker_Simulation()
    assert g.is_one_pair(hand)


def test_is_one_pair_invalid():
    hand = [('ace', 'clubs'), ('5', 'spades'),
            ('4', 'hearts'), ('6', 'clubs'), ('9', 'spades')]
    g = Poker_Simulation()
    assert not g.is_one_pair(hand)


def test_get_highest_card():
    hand = [('ace', 'clubs'), ('5', 'spades'),
            ('4', 'hearts'), ('6', 'clubs'), ('9', 'spades')]
    g = Poker_Simulation()
    assert not g.get_highest_card(hand) == 'ace'

# sample test cases for checking winner of a poker hand
testdata = [
    ([('ace', 'clubs'), ('5', 'spades'), ('4', 'hearts'), ('4', 'clubs'), ('9', 'spades')], 
    [('2', 'spades'), ('7', 'spades'), ('3', 'spades'), ('8', 'spades'), ('king', 'spades')], 
    'Player2 is winner!!!')

    , ([('10', 'hearts'), ('3', 'clubs'), ('3', 'spades'), ('jack', 'hearts'), ('10', 'spades')], 
    [('10', 'clubs'),('queen', 'spades'), ('king', 'spades'), ('4', 'diamonds'), ('king', 'diamonds')], 
    'Player1 is winner!!!')
    
    , ([('8', 'spades'), ('8', 'hearts'), ('6', 'clubs'), ('9', 'hearts'), ('8', 'diamonds')], 
    [('9', 'diamonds'), ('2', 'diamonds'), ('queen', 'diamonds'), ('4', 'hearts'), ('jack', 'clubs')], 
    'Player1 is winner!!!')

    ,([('4', 'diamonds'), ('5', 'clubs'), ('jack', 'diamonds'), ('4', 'spades'), ('jack', 'hearts')],
    [('9', 'spades'), ('5', 'spades'), ('king', 'spades'), ('jack', 'spades'), ('8', 'spades')]
    ,'Player2 is winner!!!')

    ,([('3', 'hearts'), ('9', 'clubs'), ('king', 'diamonds'), ('queen', 'clubs'), ('3', 'diamonds')],
    [('8', 'hearts'), ('6', 'diamonds'), ('10', 'spades'), ('6', 'spades'), ('queen', 'spades')],
    'Player1 is winner!!!')

    ,([('9', 'diamonds'), ('5', 'spades'), ('6', 'clubs'), ('8', 'hearts'), ('7', 'clubs')],
    [('queen', 'diamonds'), ('4', 'hearts'), ('10', 'spades'), ('queen', 'hearts'), ('10', 'diamonds')],
    'Player1 is winner!!!')

    ,([('king', 'spades'), ('3', 'spades'), ('ace', 'clubs'),('5', 'hearts'), ('ace', 'diamonds')],
    [('8', 'hearts'), ('queen', 'diamonds'),('5', 'diamonds'), ('king', 'diamonds'), ('6', 'clubs')],
    'Player1 is winner!!!')

    ,([('7', 'diamonds'), ('ace', 'hearts'),('5', 'clubs'), ('6', 'spades'), ('6', 'clubs')],
    [('king', 'hearts'), ('2', 'hearts'), ('jack', 'diamonds'),('king', 'diamonds'), ('ace', 'spades')],
    'Player1 is winner!!!')

    ,([('9', 'spades'), ('7', 'hearts'), ('ace', 'clubs'),('5', 'spades'), ('3', 'hearts')],
    [('5', 'hearts'), ('10', 'diamonds'), ('king', 'spades'),('jack', 'spades'), ('2', 'hearts')],
    'Player1 is winner!!!')

    ,([('queen', 'hearts'), ('4', 'diamonds'),('2', 'diamonds'), ('king', 'hearts'), ('8', 'hearts')],
    [('3', 'hearts'), ('6', 'spades'), ('4', 'spades'),('ace', 'diamonds'), ('king', 'clubs')],
    'Player2 is winner!!!')

    ,([('king', 'clubs'), ('7', 'diamonds'), ('jack', 'spades'),('ace', 'hearts'), ('4', 'diamonds')],
    [('queen', 'clubs'), ('9', 'clubs'), ('4', 'clubs'),('4', 'spades'), ('jack', 'hearts')],
    'Player2 is winner!!!')

    ,([('jack', 'clubs'), ('2', 'clubs'), ('10', 'diamonds'),('ace', 'diamonds'), ('jack', 'diamonds')],
    [('4', 'diamonds'), ('7', 'diamonds'),('5', 'diamonds'), ('3', 'diamonds'), ('7', 'clubs')],
    'Player2 is winner!!!')

    ,([('4', 'hearts'), ('5', 'diamonds'),('jack', 'clubs'), ('6', 'diamonds'), ('7', 'clubs')],
    [('4', 'spades'), ('8', 'hearts'), ('ace', 'diamonds'),('10', 'hearts'), ('3', 'spades')],
    'Player2 is winner!!!')

    ,([('6', 'spades'), ('ace', 'spades'), ('5', 'clubs'), ('king', 'clubs'), ('9', 'hearts')],
    [('9', 'spades'), ('jack', 'diamonds'), ('queen', 'hearts'), ('king', 'hearts'), ('4', 'diamonds')],
    'Player1 is winner!!!')


    ,([('queen', 'diamonds'), ('8', 'diamonds'), ('jack', 'hearts'), ('7', 'clubs'), ('2', 'clubs')],
    [('7', 'hearts'), ('7', 'spades'), ('queen', 'spades'), ('3', 'spades'), ('5', 'clubs')],
    'Player2 is winner!!!')


    ,([('9', 'clubs'), ('6', 'hearts'), ('7', 'diamonds'), ('king', 'clubs'), ('2', 'diamonds')],
    [('9', 'spades'), ('jack', 'diamonds'),('10', 'hearts'), ('8', 'hearts'), ('3', 'clubs')],
    'Player2 is winner!!!')


    ,([('2', 'hearts'), ('3', 'spades'), ('jack', 'clubs'),('3', 'diamonds'), ('5', 'clubs')],
    [('9', 'clubs'), ('2', 'spades'), ('8', 'diamonds'),('9', 'diamonds'), ('queen', 'spades')],
    'Player1 is winner!!!')


    ,([('king', 'diamonds'), ('8', 'diamonds'),('7', 'hearts'), ('5', 'diamonds'), ('4', 'diamonds')],
    [('3', 'hearts'), ('6', 'diamonds'), ('3', 'spades'),('7', 'diamonds'), ('7', 'spades')],
    'Player2 is winner!!!')


    ,([('6', 'hearts'), ('6', 'diamonds'), ('2', 'hearts'), ('jack', 'spades'), ('9', 'spades')],
    [('7', 'diamonds'), ('2', 'spades'), ('5', 'hearts'), ('3', 'spades'), ('jack', 'diamonds')],
    'Player1 is winner!!!')


    ,([('6', 'diamonds'), ('6', 'hearts'), ('ace', 'spades'), ('7', 'clubs'), ('5', 'clubs')],
    [('queen', 'diamonds'), ('8', 'hearts'), ('3', 'diamonds'), ('king', 'clubs'), ('7', 'spades')],
    'Player1 is winner!!!')


    ,([('5', 'hearts'), ('9', 'hearts'), ('queen', 'diamonds'), ('6', 'spades'), ('ace', 'hearts')],
    [('2', 'hearts'), ('7', 'spades'), ('king', 'spades'),('10', 'diamonds'), ('3', 'hearts')],
    'Player1 is winner!!!')


    ,([('7', 'clubs'), ('4', 'spades'), ('queen', 'diamonds'), ('king', 'diamonds'), ('4', 'clubs')],
    [('2', 'spades'), ('6', 'clubs'), ('8', 'hearts'), ('2', 'clubs'), ('3', 'spades')],
    'Player2 is winner!!!')


    ,([('9', 'diamonds'), ('king', 'hearts'), ('ace', 'spades'), ('queen', 'hearts'), ('10', 'diamonds')],
    [('king', 'diamonds'), ('ace', 'hearts'), ('2', 'clubs'), ('jack', 'clubs'), ('5', 'hearts')],
    'Player2 is winner!!!')


    ,([('10', 'diamonds'), ('queen', 'diamonds'),('9', 'spades'), ('6', 'spades'), ('jack', 'spades')],
    [('5', 'clubs'), ('3', 'hearts'), ('ace', 'hearts'),('jack', 'diamonds'), ('10', 'spades')],
    'Player2 is winner!!!')


    ,([('6', 'diamonds'), ('9', 'spades'), ('9', 'diamonds'),('3', 'hearts'), ('ace', 'hearts')],
    [('queen', 'hearts'), ('8', 'clubs'),('2', 'spades'), ('8', 'hearts'), ('7', 'clubs')],
    'Player1 is winner!!!')


    ,([('9', 'hearts'), ('5', 'hearts'),('ace', 'diamonds'), ('2', 'hearts'), ('2', 'clubs')],
    [('jack', 'clubs'), ('9', 'diamonds'),('10', 'diamonds'), ('10', 'clubs'), ('3', 'spades')],
    'Player1 is winner!!!')


    ,([('4', 'hearts'), ('ace', 'hearts'),('10', 'spades'), ('6', 'spades'), ('8', 'clubs')],
    [('king', 'clubs'), ('ace', 'spades'),('3', 'spades'), ('7', 'diamonds'), ('9', 'clubs')],
    'Player1 is winner!!!')


    ,([('9', 'clubs'), ('3', 'diamonds'),('ace', 'diamonds'), ('3', 'hearts'), ('4', 'hearts')],
    [('5', 'clubs'), ('3', 'clubs'), ('ace', 'spades'),('5', 'spades'), ('4', 'spades')],
    'Player1 is winner!!!')


    ,([('jack', 'clubs'), ('king', 'hearts'),('2', 'diamonds'), ('king', 'clubs'), ('2', 'clubs')],
    [('ace', 'diamonds'), ('8', 'clubs'),('3', 'clubs'), ('9', 'spades'), ('3', 'hearts')],
    'Player1 is winner!!!')


    ,([('2', 'clubs'), ('9', 'diamonds'),('2', 'hearts'), ('4', 'clubs'), ('5', 'spades')],
    [('8', 'clubs'), ('7', 'clubs'), ('5', 'diamonds'),('4', 'spades'), ('3', 'hearts')],
    'Player1 is winner!!!')


    ,([('10', 'hearts'), ('9', 'diamonds'), ('queen', 'clubs'),('3', 'clubs'), ('ace', 'diamonds')],
    [('6', 'spades'), ('6', 'diamonds'), ('king', 'diamonds'),('ace', 'spades'), ('ace', 'hearts')],
    'Player2 is winner!!!')


    ,([('king', 'spades'), ('7', 'clubs'),('10', 'hearts'), ('3', 'spades'), ('9', 'clubs')],
    [('10', 'diamonds'), ('7', 'spades'),('9', 'hearts'), ('7', 'hearts'), ('6', 'clubs')],
    'Player2 is winner!!!')


    ,([('queen', 'spades'), ('5', 'spades'), ('10', 'hearts'), ('king', 'clubs'), ('5', 'hearts')],
    [('king', 'diamonds'), ('queen', 'hearts'),('2', 'clubs'), ('4', 'hearts'), ('5', 'diamonds')],
    'Player1 is winner!!!')
]


@pytest.mark.parametrize("set1, set2, expected", testdata)
def test_get_poker_winner(set1:list, set2:list, expected:str) -> any:
    g = Poker_Simulation()
    g.deck = g.get_deck()
    assert (g.get_poker_winner(set1, set2)) == expected
