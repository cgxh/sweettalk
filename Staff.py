from Account import User
class Staff(User):
    count_id=0
    def __init__(self,staff_id,username,password):
        super().__init__(username,password)
        self.__staff_id=staff_id
        Staff.count_id+=1
        self.__staff_count=Staff.count_id

    def get_staff_count(self):
        return self.__staff_count

    def get_staff_id(self):
        return self.staff_id

    def set_staff_id(self, staff_id):
        self.__staff_id = staff_id

