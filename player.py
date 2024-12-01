class Player:
    def __init__(self, type, cardsWon = [], turnToPlay = False, cardsInHand = []):
        self.set_type(type)
        self.wins_cards(cardsWon)
        self.set_turn(turnToPlay)
        self.set_hand(cardsInHand)

    def set_type(self, type):
        self.__type = type

    def wins_cards(self, cardsWon):
        for card in cardsWon:
            self.__cardsWon = cardsWon

    def set_turn(self, turnToPlay)
        self.__turnToPlay = turnToPlay

    def set_hand(self, cardsInHand):
        self.__cardsInHand = cardsInHand

    def get_type(self):
        return self.__type
    
    def get_cardsWon(self):
        return self.__cardsWon
    
    def get_hand(self):
        return self.__cardsInHand