class Player:
    def __init__(self, type, turnToPlay = False):
        self.set_type(type)
        self.__cardsWon = []
        self.__cardsInHand = []
        self.set_turn(turnToPlay)
        self.__numberOfScopa = 0

    def set_type(self, type):
        self.__type = type

    def wins_cards(self, cardsWon):
        for card in cardsWon:
            self.__cardsWon.append(card)

    def set_turn(self, turnToPlay):
        self.__turnToPlay = turnToPlay

    def pick_from_deck(self, deck):
        self.__cardsInHand = []
        for card in deck[:3]:
            self.__cardsInHand.append(card)

    def add_scopa(self):
        self.__numberOfScopa += 1

    def get_type(self):
        return self.__type
    
    def get_cardsWon(self):
        return self.__cardsWon
    
    def get_hand(self):
        return self.__cardsInHand
    
    def is_my_turn(self):
        return self.__turnToPlay

    def make_a_move(self, choosenCard, listMatchingCards):
        count = 0
        for card in listMatchingCards:
            count += card.get_value()
        if choosenCard.get_value() == count:
            self.__cardsWon.extend(listMatchingCards)