from Account import User
class Customer(User):
    count_id=0
    def __init__(self,first_name, last_name, mobile_no,address,username,password,):
        super().__init__(username,password)
        Customer.count_id+=1
        self.__customer_id=Customer.count_id
        self.__first_name = first_name
        self.__last_name = last_name
        self.__mobile_no=mobile_no
        self.__address=address

    def get_customer_id(self):
        return self.__customer_id

    def get_first_name(self):
        return self.__first_name

    def get_last_name(self):
        return self.__last_name

    def get_mobile_no(self):
        return self.__mobile_no

    def get_address(self):
        return self.__address



    def set_first_name(self, first_name):
        self.__first_name = first_name

    def set_last_name(self, last_name):
        self.__last_name = last_name

    def set_mobile_no(self, mobile_no):
        self.__mobile_no = mobile_no

    def set_address(self, address):
        self.__address = address

