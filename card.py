class Card:
    def __init__(self, suit, value, image, is_on_board=False):
        self.set_suit(suit)
        self.set_value(value)
        self.set_image(image)
        self.set_is_denaro(suit)
        self.set_is_7denaro(suit, value)
        self.set_on_board(is_on_board)
        Card.dict_for_cards = {'suit' : ['Denaro', 'Coppa', 'Bastone', 'Spada'], 'value': [1,2,3,4,5,6,7,8,9,10]}

    def set_suit(self, suit):
        self.__suit = suit

    def set_value(self, value):
        self.__value = value

    def set_image(self, image):
        self.__image = image

    def set_is_denaro(self, suit):
        if self.get_suit() == 'Denaro':
            self.__is_denaro = True
        else:
            self.__is_denaro = False
    
    def set_is_7denaro(self, suit, value):
        if self.get_suit() == 'Denaro' and self.get_value() == 7:
            self.__is_7denaro = True
        else:
            self.__is_7denaro = False

    def set_on_board(self, is_on_board):
        self.__on_board = is_on_board

    def get_suit(self):
        return self.__suit
    
    def get_value(self):
        return self.__value
    
    def get_image(self):
        return self.__image
    
    def get_is_denaro(self):
        return self.__is_denaro
    
    def get_is_7denaro(self):
        return self.__is_7denaro
    
    def get_is_on_board(self):
        return self.__on_board

    
    