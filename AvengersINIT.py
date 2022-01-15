class Avenger:

    def __init__(self, name):
        self.name = name

    def win(self):
        print(self.name + " always win")

    def love(self):
        print("Everybody loves " + self.name)    


class Strong(Avenger):

    def win(self):
        super().win()
        print("The " + self.name + " won, but with changed shape")    

class Smart(Avenger):

    def love(self):
        print("Somebody loves " + self.name + ", somebody doesn't")

class Interesting(Avenger):

    def win(self):
        print(self.name + " always win, but by the interesting ways")

    def love(self):
        print(self.name + " is the selfish badass, which a lot of people don't WIKE")    

class Dead(Avenger):

    def win(self):
        print(self.name + " won, but died")

    def love(self):
        print("Everybody loves " + self.name + ", because " + self.name + " died for us!")


def winning_test(p):
    p.win()

def loving_test(p):
    p.love()   


Iron_Man = Dead('Tony')
Black_Widow = Dead('Nat')
Ant_Man = Avenger('Scott')
Hulk = Strong('Bruce')
Dr_Strange = Smart('Stephen')
Scarlett_Witch = Interesting('Wanda')
Thor = Strong('Thor')
Hawkeye = Avenger('Clint')
Captain_America = Strong('Steve')

for i in Iron_Man, Black_Widow, Ant_Man, Hulk, Dr_Strange, Scarlett_Witch, Thor, Hawkeye, Captain_America:
    winning_test(i)
    loving_test(i)