#Simple turn based, 2 player game written in python 3
#Jaroslaw Glodowski
class Ship:

    def __init__(self, name):
        self.name = name
        self.health = 100
        self.heavy_ammo = 3
        self.light_ammo = 15

    def get_info(self):
        print("  %s's Warship: %d%% Health, Heavy Ammo: %d, Light Ammo: %d" % (self.name, self.health, self. heavy_ammo, self.light_ammo))

    def get_heavy_ammo(self):
        return self.heavy_ammo

    def get_light_ammo(self):
        return self.light_ammo

    def get_name(self):
        return self.name

    def is_alive(self):
        if self.health <= 0:
            return False
        return True

    def sub_heavy_ammo(self):
        self.heavy_ammo -= 1

    def sub_light_ammo(self):
        self.light_ammo -= 1

    def sub_health(self, num):
        self.health -= num
