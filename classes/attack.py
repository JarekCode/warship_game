#Simple turn based, 2 player game written in python 3
#Jaroslaw Glodowski
import random
class Attack:

    def attack(self, attack_type):
        #light
        if attack_type == "1":
            num = random.randrange(1, 100)
            damage = random.randrange(10, 20)
            if num <= 80:
                print("\n  Hit! (-%d%% Health)\n" % damage)
                return damage
            else:
                print("\n  Miss!\n")
                return 0
        #heavy
        else:
            num = random.randrange(1, 100)
            damage = random.randrange(30, 40)
            if num <= 40:
                print("\n  Hit! (-%d%% Health)\n" % damage)
                return damage
            else:
                print("\n  Miss!\n")
                return 0
