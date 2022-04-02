class UserMail:

    def __init__(self, login: str, email: str):
        self.login = login
        self.__email = email

    def get_email(self):
        return self.__email

    def set_email(self, email: str):
        if (email.count("@") == 1) and (email.count(".") == 1):
            if email.index("@") < email.index("."):
                self.__email = email
            else:
                print("Ошибочная почта")
        else:
            print("Ошибочная почта")

    def del_email(self):
        del self.__email

    # Свойства
    email = property(fget=get_email, fset=set_email, fdel=del_email)

    # email = property()
    # email = email.getter(get_email)
    # email = email.setter(set_email)
    # email = email.deleter(del_email)


k = UserMail('belosnezhka', 'prince@wait.you')
print(k.email)  # prince@wait.you

k.email = [1, 2, 3] # Ошибочная почта
k.email = 'prince@still@.wait'  # Ошибочная почта
k.email = 'prince@still.wait'
print(k.email)  # prince@still.wait


