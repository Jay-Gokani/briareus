import unittest
import main
from random import randint

damage_regulator = 3

class TestHaunter(unittest.TestCase):

    def test_move_selected_1(self):
        # Shadow Ball
        haunter = main.Haunter()
        kadabra = main.Kadabra()
        kadabra.fainted = False
        shadow_ball_base_damage = 80
        shadow_ball_damage = haunter.special_attack - kadabra.special_defence + round((shadow_ball_base_damage/damage_regulator))
        kadabra.hp -= shadow_ball_damage
        if kadabra.hp <= 0:
             kadabra.fainted = True
             self.assertTrue(kadabra.fainted)

    def test_move_selected_2(self):
        # Shadow Punch
        haunter = main.Haunter()
        kadabra = main.Kadabra()
        shadow_punch_base_damage = 60
        shadow_punch_damage = haunter.attack - kadabra.defence + round((shadow_punch_base_damage/damage_regulator))
        kadabra.hp -= shadow_punch_damage

        if kadabra.hp <= 0:
            self.assertTrue(kadabra.fainted)

    def test_move_selected_3(self):
        # Confuse Ray
        kadabra = main.Kadabra()
        kadabra.confused = True
        self.assertTrue(kadabra.confused)

    def test_move_selected_4(self):
        # Hypnosis
        kadabra = main.Kadabra
        kadabra.sleep = False
        sleep_chance = randint(1, 3)
        if sleep_chance != 1:
            kadabra.sleep = True
            self.assertTrue(kadabra.sleep)
        else:
            self.assertFalse(kadabra.sleep)

if __name__ == '__main__':
	unittest.main()