class Client:
    def __init__(self, age, number, e_mail):
        self.age = age
        self.number = number
        self.e_mail = e_mail
        
    def draw(self):
        print("Вік клієнта", self.age)
        print("Номер клієнта", self.number)
        print("Адрес клієнта", self.e_mail)
client1 = Client("Антон", 1337, "133714881945")
client2 = Client("светлана", 1488, "133714881945")
client3 = Client("Фюррер", 1945, "133714881945")
client1.draw()
client1.number = "13371488192312213213213213213123213213"
client1.draw()








