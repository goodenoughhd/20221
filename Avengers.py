class Avenger:

    def win(self, p):
        print("{} always win".format(p))

    def love(self, p):
        print("Everyone loves {}".format(p))    


class Strong(Avenger):

    def win(self, p):
        print("The {} win, but with changed shape".format(p))    

class Smart(Avenger):

    def love(self, p):
        print("Somebody loves {}, somebody doesn't".format(p))

class Interesting(Avenger):

    def win(self, p):
        print("{} always win, but by the interesting ways".format(p))

    def love(self, p):
        print("{} is the selfish badass, which a lot of people don't WIKE".format(p))    

class Dead(Avenger):

    def win(self, p):
        print("{} won, but dead".format(p))

    def love(self, p):
        print("Everybody loves the dead {}".format(p))

def winning_test(p):
    p.win(p)

def loving_test(p):
    p.love(p)    

Iron_Man = Dead()
Black_Widow = Dead()
Ant_Man = Avenger()
Hulk = Strong()
Dr_Strange = Smart()
Scarlett_Witch = Interesting()
Thor = Strong()
Hawkeye = Avenger()
Captain_America = Strong()



winning_test(Iron_Man)
loving_test(Iron_Man)