#Simple turn based, 2 player game written in python 3
#Jaroslaw Glodowski
from classes.ship import Ship
from classes.attack import Attack
import os

os.system("cls")
p1 = input("Enter player 1's name: ")
p2 = input("Enter player 2's name: ")
os.system("cls")

m1 = Attack()
s1 = Ship(p1)
s2 = Ship(p2)

player = s1
ggame = True

def update_player(player):
    if player == s1:
        return s2
    else:
        return s1

def turn_move_light(ammo_type, plr):
    dmg = m1.attack(ammo_type)
    plr.sub_light_ammo()
    plr = update_player(plr)
    plr.sub_health(dmg)
    plr = update_player(plr)
    player = plr

def turn_move_heavy(ammo_type, plr):
    dmg = m1.attack(ammo_type)
    plr.sub_heavy_ammo()
    plr = update_player(plr)
    plr.sub_health(dmg)
    plr = update_player(plr)
    player = plr

while ggame is True:

    print("  ------------------------------------------------------------")
    s1.get_info()
    s2.get_info()
    print("  ------------------------------------------------------------")
    print("\n  ---- %s's Turn ----\n  Choose attack:" % player.get_name())
    attack_choice = input("  1: Light Attack (80% Hit Chance)\n  2: Heavy Attack (40% Hit Chance)\n  ")
    os.system("cls")

    while attack_choice == "1" or attack_choice == "2":
        if attack_choice == "1":
            ammoCount = player.get_light_ammo()
            if ammoCount > 0:
                turn_move_light("1", player)
                player = update_player(player)
            else:
                print("\n\n\n  ---- Light Ammo Depleted! ----\n\n\n")
                player = update_player(player)
                player = update_player(player)

        elif attack_choice == "2":
            ammoCount = player.get_heavy_ammo()
            if ammoCount > 0:
                turn_move_heavy("2", player)
                player = update_player(player)
            else:
                print("\n\n\n  ---- Heavy Ammo Depleted! ----\n\n\n")
                player = update_player(player)
                player = update_player(player)

        attack_choice = "0"
        ggame = player.is_alive()

player = update_player(player)
print("  --- Game Over! ---\n     %s has Won!\n  ------------------\n\n  -------------------- Winner Stats --------------------" % player.get_name())
player.get_info()
print("  ------------------------------------------------------")
