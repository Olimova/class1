class Odam:

    def __init__(self,ism):
        self.ism=ism

    def salomlashish(self):
        print(f"Salom {self.ism}")

person=Odam(input("Ismingizni kiriting: "))
person.salomlashish()