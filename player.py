class Player:
    def __init__(self, type, cardsWon = [], turnToPlay = False, cardsInHand = []):
        self.set_type(type)
        self.wins_cards(cardsWon)
        self.set_turn(turnToPlay)
        self.pick_from_deck(cardsInHand)

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

    def get_type(self):
        return self.__type
    
    def get_cardsWon(self):
        return self.__cardsWon
    
    def get_hand(self):
        return self.__cardsInHand
    
    def my_turn(self):
        return self.__turnToPlay

        