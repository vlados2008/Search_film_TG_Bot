class User:
    def __init__ (self, id, full_name, name, username):
        self.__id = id
        self.__full_name = full_name
        self.__name = name
        self.__username = username
        self.__language = 'ru'

    @classmethod
    def create_from_message(cls,message):
        return cls(message.from_user.id,  message.from_user.full_name, message.from_user.first_name, message.from_user.username)

    @property
    def id (self):
        return self.__id
    
    @property
    def full_name (self):
        return self.__full_name
    
    @property
    def name (self):
        return self.__name
    
    @property
    def username (self):
        return self.__username

    @property
    def language (self):
        return self.__language
