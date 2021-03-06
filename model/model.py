class User:
    def __init__(self,uname="",address="",email="",gender="",phoneno="",roomno='',date=""):
        self.__username=uname
        self.__address = address
        self.__email = email
        self.__gen = gender
        self.__pno = phoneno
        self.__rno=roomno
        self.__date=date


    def set_username(self,uname):
        """
                        Function to set value for username.
                        :param id:set_username
                        :type id:str
                """
        self.__username=uname

    def get_username(self):
        return self.__username

    def set_address(self, address):
        """
                                Function to set value for address.
                                :param id:set_address
                                :type id:str
                        """
        self.__address = address

    def get_address(self):
        return self.__address

    def set_email(self, email):
        """
                                Function to set value for email.
                                :param id:set_email
                                :type id:str
                        """
        self.__email = email

    def get_email(self):
        return self.__email

    def set_gender(self,gender):
        """
                                Function to set value for gender.
                                :param id:set_gender
                                :type id:str
                        """
        self.__gen = gender

    def get_gender(self):
        return self.__gen


    def set_pno(self,phoneno):
        """
                                Function to set value for phonenumber.
                                :param id:set_pno
                                :type id:int
                        """
        self.__pno = phoneno


    def get_pno(self):
        return self.__pno


    def set_rno(self, roomno):
        """
                                Function to set value for roomnumber.
                                :param id:set_rno
                                :type id:int
                        """
        self.__rno = roomno


    def get_rno(self):
        return self.__rno

    def set_date(self, date):
        """
                                Function to set value for date.
                                :param id:set_date
                                :type id:int
                        """
        self.__date = date

    def get_date(self):
        return self.__date