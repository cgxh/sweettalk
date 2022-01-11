class Order:
    def __init__(self, name, card_number, expiry_date, cvv, address):
        self.__name = name
        self.__card_number = card_number
        self.__expiry_date = expiry_date
        self.__cvv = cvv
        self.__address = address

    def get_user_id(self):
        return self.__user_id

    def get_first_name(self):
        return self.__first_name

    def get_card_number(self):
        return self.__card_number

    def get_expiry_date(self):
        return self.__expiry_date

    def get_cvv(self):
        return self.__cvv

    def get_address(self):
        return self.__address

    def set_user_id(self, user_id):
        self.__user_id = user_id

    def set_first_name(self, first_name):
        self.__first_name = first_name

    def set_card_number(self, card_number):
        self.__card_number = card_number

    def set_expiry_date(self, expiry_date):
        self.__expiry_date = expiry_date

    def set_cvv(self, cvv):
        self.__cvv = cvv

    def set_address(self, address):
        self.__address = address


