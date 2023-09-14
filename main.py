import os
from pyfiglet import figlet_format
from time import sleep
from random import randint
from sys import exit
from sys import stdout

damage_regulator = 3
potion_quantity = 1
randopotion_quantity = 1
money = randint(435, 1025)
confusion_turn_count = 0
disabled_turn_count = 0

class Haunter():
    def __init__(self):
        self.name = "Haunter"
        self.type1 = "Ghost"
        self.type2 = "Poison"    

        self.max_hp          = 85    
        self.hp              = 85
        self.attack          = 38
        self.defence         = 38
        self.special_attack  = 55
        self.special_defence = 50
        self.speed           = 50

        self.disabled        = False
        self.fainted         = False

class Kadabra():
    def __init__(self):
        self.name = "Kadabra"
        self.type1 = "Psychic"

        self.max_hp          = 75    
        self.hp              = 75
        self.attack          = 35
        self.defence         = 35
        self.special_attack  = 60
        self.special_defence = 54
        self.speed           = 55

        self.sleep           = False
        self.confused        = False
        self.fainted         = False
        self.recoil          = False

def delay_print(word):
    for character in word:
        stdout.write(character)
        stdout.flush()
        sleep(0.05)
    print('')

def title_banner():
    os.system('clear')
    print('==================================================')
    print(figlet_format("Jaykemon"))
    print('==================================================')

def randomiser():
    global randomise
    randomise = randint(1,3)
    return randomise

def turn():
    title_banner()
    print('')
    sleep(0.5)
    delay_print(f'Haunter (HP {haunter.hp}/{haunter.max_hp}) vs Kadabra (HP {kadabra.hp}/{kadabra.max_hp})')
    print('')
    sleep(0.5)
    delay_print('1 Fight')
    sleep(0.5)
    delay_print('2 Item')
    sleep(0.5)
    delay_print('3 Pokemon')
    sleep(0.5)
    delay_print('4 Run')
    sleep(0.5)
    print('')
    print('==================================================')
    sleep(0.5)

    while True:
        sleep(0.5)
        turn_choice = input('Type a number to select an option: ')
        if turn_choice == '1':
            sleep(0.5)
            delay_print('You chose: Fight')
            sleep(2.5)
            fight_choice()
            return False
        elif turn_choice == '2':
            sleep(0.5)
            delay_print('You chose: Item')
            sleep(2.5)
            item_choice()
            return False
        elif turn_choice == '3':
            sleep(0.5)
            delay_print('You chose: Pokemon')
            sleep(2.5)
            pokemon_choice()
            return False
        elif turn_choice == '4':
            sleep(0.5)
            delay_print('You chose: Run')
            sleep(2.5)
            run_choice()
            return False
        else:
            sleep(0.5)
            delay_print('Only select a choice between 1 and 4...')
            sleep(2.5)
            turn()

def fight_choice():
    title_banner()
    print('')
    sleep(0.5)
    delay_print('1 Shadow Ball')
    sleep(0.5)
    delay_print('2 Shadow Punch')
    sleep(0.5)
    delay_print('3 Confuse Ray')
    sleep(0.5)
    delay_print('4 Hypnosis')
    sleep(0.5)
    print('')
    delay_print('x Return to Fight | Items | Pokemon | Run screen')
    sleep(0.5)
    print('')
    print('==================================================')
    sleep(0.5)

    # Todo: do I need return statements for hp, confusion and sleep status'? Test
    while True:
        global move_selected
        move_selected = input('Type a number between 1 and 4, or type x: ')
        # move_selected = input('Type a number between 1 and 4, or x to select an option: ')
        title_banner()
        if haunter.disabled == True and move_selected == disabled_move:
            sleep(1.5)
            print('')
            delay_print(f'Haunter\'s {disabled_move} is disabled. Select another choice...')
            sleep(3.5)
            fight_choice()
            return False 
        else:
            if move_selected == '1':
                # Shadow Ball
                sleep(1.5)
                print('')
                delay_print('Haunter used Shadow Ball!')
                sleep(0.5)
                delay_print('It\'s super effective!')
                shadow_ball_base_damage = 80
                shadow_ball_damage = haunter.special_attack - kadabra.special_defence + round((shadow_ball_base_damage/damage_regulator))
                kadabra.hp -= shadow_ball_damage
                sleep(0.5)
                if kadabra.hp <= 0:
                    kadabra.fainted = True
                    delay_print(f'Kadabra fainted! You win ${money}!')
                    sleep(2.5)
                    exit()
                else:
                    delay_print(f'Haunter dealt {shadow_ball_damage} points of damage!')
                    sleep(1.5)
                    delay_print(f'Enemy Kadabra\'s HP is now {kadabra.hp}/{kadabra.max_hp}')
                sleep(2.5)
                return False
            if move_selected == '2':
                # Shadow Punch
                sleep(1.5)
                print('')
                delay_print('Haunter used Shadow Punch!')
                sleep(0.5)
                delay_print('It\'s super effective!')
                shadow_punch_base_damage = 60
                shadow_punch_damage = haunter.attack - kadabra.defence + round((shadow_punch_base_damage/damage_regulator))
                kadabra.hp -= shadow_punch_damage
                sleep(0.5)
                if kadabra.hp <= 0:
                    delay_print(f'Kadabra fainted! You win ${money}!')
                    sleep(2.5)
                    exit()
                else:
                    delay_print(f'Haunter dealt {shadow_punch_damage} points of damage!')
                    sleep(1.5)
                    delay_print(f'Enemy Kadabra\'s HP is now {kadabra.hp}/{kadabra.max_hp}')
                sleep(2.5)
                return False
            if move_selected == '3':
                # Confuse Ray
                sleep(1.5)
                print('')
                delay_print('Haunter used Confuse Ray!')
                sleep(0.5)
                if kadabra.confused == True:
                    delay_print('Kadabra is already confused...')
                else:
                    delay_print('Enemy Kadabra is confused!')
                kadabra.confused = True
                sleep(2.5)
                return False
            if move_selected == '4':
                # Hypnosis            
                sleep(1.5)
                print('')
                delay_print('Haunter used Hypnosis!')
                sleep(0.5)
                if kadabra.sleep == True:
                    delay_print('Kadabra is already asleep...')
                else:
                    sleep_chance = randomise
                    if sleep_chance != 1:
                        kadabra.sleep = True
                        delay_print('Enemy Kadabra fell asleep!')
                    else:
                        delay_print('Haunter\'s Hypnosis missed!')
                sleep(2.5)
                return False
            if move_selected == 'x' or 'X':
                turn()
                return False
            else:
                # Invalid choice
                sleep(1.5)
                delay_print('Only select a choice between 1 and 4, or x...')
                sleep(3.5)
                fight_choice()
                return False     

def item_choice():
    title_banner()
    sleep(0.5)
    print('')
    delay_print('Items')
    print('')
    sleep(0.5)
    delay_print('1 Potion')
    sleep(0.5)
    delay_print('2 Randopotion')
    sleep(0.5)
    delay_print('3 Pokeball')
    sleep(0.5)
    print('')
    delay_print('x Return to Fight | Items | Pokemon | Run screen')
    sleep(0.5)
    print('')
    print('==================================================')
    sleep(0.5)

    while True:
        item_selected = input('Type a number between 1 and 3, or x to select an option: ')
        if item_selected == '1':
            # Potion
            global potion_quantity
            if potion_quantity != 0:
                if haunter.hp == haunter.max_hp:
                    sleep(1.5)
                    delay_print('Haunter\'s HP is already at max. Select another choice...')
                    sleep(3.5)
                    item_choice()
                    return False 
                else:
                    start_hp = haunter.hp
                    if haunter.max_hp - haunter.hp <= 20:
                        restored_hp = haunter.max_hp - haunter.hp
                        haunter.hp = haunter.max_hp
                    else:
                        restored_hp = 20
                        haunter.hp += 20
                    sleep(0.5)
                    delay_print(f'Haunter\'s HP was restored by {restored_hp} points, from {start_hp} to {haunter.hp}')
                    sleep(2.5)
                    potion_quantity = 0
                    return False
            else:
                sleep(0.5)
                delay_print('You have ran out of potions. Select another choice...')
                sleep(3.5)
                item_choice()
                return False
        elif item_selected == '2':
            # Randopotion
            global randopotion_quantity 
            if randopotion_quantity != 0:
                if haunter.hp == haunter.max_hp:
                    sleep(1.5)
                    delay_print('Haunter\'s HP is already at max. Select another choice...')
                    sleep(3.5)
                    item_choice()
                    return False
                else:
                    start_hp = haunter.hp
                    potion_power = randint(0, haunter.max_hp - haunter.hp)
                    haunter.hp += potion_power
                    sleep(0.5)
                    delay_print(f'Haunter\'s HP was restored by {potion_power} points, from {start_hp} to {haunter.hp}')
                    sleep(2.5)
                    randopotion_quantity = 0
                    return False
            else:
                sleep(0.5)
                delay_print('You have ran out of randopotions. Select another choice...')
                sleep(3.5)
                item_choice()
                return False
        elif item_selected == '3':
            # Pokeball
            sleep(0.5)
            delay_print('You can\'t catch another trainer\'s Pokemon! Select another item...')
            sleep(3.5)
            item_choice()
            return False
        if item_selected == 'x' or 'X':
                turn()
                return False
        else:
            # Invalid choice
            sleep(0.5)
            delay_print('Only select a choice between 1 and 3, or x...')
            sleep(3.5)
            item_choice()
            return False

def pokemon_choice():
    sleep(0.5)
    delay_print('You currently have no other Pokemon in your party. Select another choice...')
    sleep(3.5)
    turn()

def run_choice():
    sleep(0.5)
    delay_print('You can\'t run from a trainer battle! Select another choice...')
    sleep(2.5)
    turn()

def kadabra_sleep_checker():
    title_banner()
    print('')
    sleep(0.5)
    delay_print('Enemy Kadabra\'s turn...')
    sleep(0.5)

    if kadabra.sleep == True:
        sleep_chance = randomise
        if sleep_chance == 1:
            delay_print('Kadabra woke up!')
            sleep(1.5)
            kadabra.sleep = False
        else:
            sleep(0.5)
            delay_print('Kadabra is fast asleep...')
            sleep(2.5)

def kadabra_confusion():
    kadabra.recoil = False
    if kadabra.confused == True:
        global confusion_turn_count
        confusion_turn_count += 1
    if confusion_turn_count == 3:
        kadabra.confused = False
        confusion_turn_count = 0
        delay_print('Kadabra snapped out of its confusion!')
        sleep(2.5)
    if kadabra.confused == True:
        delay_print('Kadabra is confused...')
        sleep(1.5)
        recoil_chance = randomise
        if recoil_chance == 1:
            kadabra.recoil = True
            delay_print('Kadabra hurt itself in it\'s confusion!')
            kadabra.hp -= round(kadabra.max_hp * (randint(20, 30)/100))
            if kadabra.hp <= 0:
                delay_print(f'Kadabra fainted! You win ${money}!')
                sleep(2.5)
                exit()
            else:
                sleep(1.5)
                delay_print(f'Enemy Kadabra\'s HP is now {kadabra.hp}/{kadabra.max_hp}')
                sleep(2.5)

def kadabra_move():
    kadabra_move_selected = randint(1, 4)
    if kadabra_move_selected == 1:
        # Confusion
        sleep(1.5)
        print('')
        delay_print('Kadabra used Confusion!')
        sleep(0.5)
        delay_print('It\'s super effective!')
        confusion_base_damage = 50
        confusion_damage = kadabra.special_attack - haunter.special_defence + round((confusion_base_damage/damage_regulator))
        haunter.hp -= confusion_damage
        sleep(0.5)
        if haunter.hp <= 0:
            delay_print(f'Haunter fainted! You lose...')
            sleep(2.5)
            exit()
        else:
            delay_print(f'Kadabra dealt {confusion_damage} points of damage!')
            sleep(1.5)
            delay_print(f'Haunter\'s HP is now {haunter.hp}/{haunter.max_hp}')
        sleep(2.5)

    elif kadabra_move_selected == 2:
        # Psybeam
        sleep(1.5)
        print('')
        delay_print('Kadabra used Psybeam!')
        sleep(0.5)
        delay_print('It\'s super effective!')
        psybeam_base_damage = 60
        psybeam_damage = kadabra.special_attack - haunter.special_defence + round((psybeam_base_damage/damage_regulator))
        haunter.hp -= psybeam_damage
        sleep(0.5)
        if haunter.hp <= 0:
            delay_print(f'Haunter fainted! You lose...')
            sleep(2.5)
            exit()
        else:
            delay_print(f'Kadabra dealt {psybeam_damage} points of damage!')
            sleep(1.5)
            delay_print(f'Haunter\'s HP is now {haunter.hp}/{haunter.max_hp}')
        sleep(2.5)

    elif kadabra_move_selected == 3:
        # Disable
        if haunter.disabled == False:
            sleep(1.5)
            print('')
            delay_print('Kadabra used Disable!')
            sleep(0.5)
            global disabled_move
            global disabled_move_name
            disabled_move = move_selected

            haunter_moves = {
            '1': 'Shadow Ball',
            '2': 'Shadow Punch',
            '3': 'Confuse Ray',
            '4': 'Hypnosis'
            }

            disabled_move_name = haunter_moves.get(disabled_move)
            delay_print(f'Haunter\'s {disabled_move_name} has been disabled!')
            haunter.disabled = True
            sleep(2.5)
        else:
            kadabra_move()

    elif kadabra_move_selected == 4:
        # Recover
        if kadabra.hp == kadabra.max_hp:
            kadabra_move()
        else:
            sleep(1.5)
            print('')
            delay_print('Kadabra used Recover!')
            sleep(0.5)
            kadabra_start_hp = kadabra.hp
            kadabra.hp += round((0.5 * kadabra.max_hp))
            if kadabra.hp > kadabra.max_hp:
                kadabra.hp = kadabra.max_hp
            restored_hp = kadabra.hp - kadabra_start_hp
            sleep(0.5)
            delay_print(f'Kadabra\'s HP was restored by {restored_hp} points, from {kadabra_start_hp} to {kadabra.hp}')
            sleep(2.5)

def disable_turns():
    if haunter.disabled == True:
        global disabled_turn_count
        disabled_turn_count += 1
        if disabled_turn_count == 3:
            print('')
            delay_print(f'Haunter\'s {disabled_move_name} is no longer disabled!')
            sleep(2.5)
            disabled_turn_count = 0
            haunter.disabled = False

# =====================================================
# ================= Game loop =========================
# =====================================================

haunter = Haunter()
kadabra = Kadabra()

title_banner()
print('')
delay_print('Sabrina wants to battle...')
sleep(1.5)
print('')
delay_print('Sabrina sent out Kadabra!')
sleep(1.5)
print('')
delay_print('Ash sent out Haunter!')
print('')
print('==================================================')
sleep(2.5)

while True:
    randomiser()
    turn()
    randomiser()
    kadabra_sleep_checker()
    if kadabra.sleep == False:
        randomiser()
        kadabra_confusion()
        if kadabra.recoil == True:
            pass
        else: kadabra_move()
    disable_turns()

if __name__ == '__main__':
	main()