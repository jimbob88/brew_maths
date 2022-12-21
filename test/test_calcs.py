import unittest

from calc.util import total_mass, percentage_by_mass
from calc.ebc import graham_recipe_ebc
from calc.original_gravity import original_gravity, individual_gravity
from recipe_objects.grist import GristRecipe, GristMetadata


class TestMisc(unittest.TestCase):
    def test_total_mass(self):
        grists = [
            GristRecipe(
                0, False, 0, 0, 0, None, 100
            ),
            GristRecipe(
                0, False, 0, 0, 0, None, 300
            ),
        ]
        self.assertEqual(total_mass(grists), 400)

    def test_percentage_by_mass(self):
        grists = [
            GristRecipe(
                0, False, 0, 0, 0, None, 100
            ),
            GristRecipe(
                0, False, 0, 0, 0, None, 300
            ),
        ]
        self.assertEqual(total_mass(grists), 400)
        self.assertEqual(percentage_by_mass(grists[0], grists), 0.25)

    def test_original_gravity_withMashableMalt(self):
        grists = [
            GristRecipe(ebc=60,
                        mashable=True,
                        extract=265,
                        moisture=3,
                        fermentability=200,
                        metadata=GristMetadata(name='Amber Malt'),
                        mass=100)
        ]
        grav = original_gravity(grists, 10, 0.75)
        # Test is in agreement with WWW
        self.assertEqual(round(grav), 1002)

    def test_original_gravity_withUnmashableSugar(self):
        grists = [
            GristRecipe(ebc=50,
                        mashable=False,
                        extract=370,
                        moisture=30,
                        fermentability=100,
                        metadata=GristMetadata(name='Sugar, Demerara'),
                        mass=100)
        ]
        grav = original_gravity(grists, 10, 0.75)
        # Test is in agreement with WWW
        self.assertEqual(round(grav, 1), 1003.7)

    def test_original_gravity_withGrists(self):
        grists = [
            GristRecipe(ebc=60,
                        mashable=True,
                        extract=265,
                        moisture=3,
                        fermentability=200,
                        metadata=GristMetadata(name='Amber Malt'),
                        mass=100),
            GristRecipe(ebc=50,
                        mashable=False,
                        extract=370,
                        moisture=30,
                        fermentability=100,
                        metadata=GristMetadata(name='Sugar, Demerara'),
                        mass=100),
        ]
        grav = original_gravity(grists, 10, 0.75)
        # Test is in agreement with WWW
        self.assertEqual(round(grav, 1), 1005.7)

    def test_original_gravity_withDifferentTargetVolume(self):
        grists = [
            GristRecipe(ebc=60,
                        mashable=True,
                        extract=265,
                        moisture=3,
                        fermentability=200,
                        metadata=GristMetadata(name='Amber Malt'),
                        mass=100),
            GristRecipe(ebc=50,
                        mashable=False,
                        extract=370,
                        moisture=30,
                        fermentability=100,
                        metadata=GristMetadata(name='Sugar, Demerara'),
                        mass=100),
        ]
        grav = original_gravity(grists, 30, 0.75)
        # Test is in agreement with WWW
        self.assertEqual(round(grav, 1), 1001.9)

    def test_original_gravity_withDifferentEfficiency(self):
        grists = [
            GristRecipe(ebc=60,
                        mashable=True,
                        extract=265,
                        moisture=3,
                        fermentability=200,
                        metadata=GristMetadata(name='Amber Malt'),
                        mass=100),
            GristRecipe(ebc=50,
                        mashable=False,
                        extract=370,
                        moisture=30,
                        fermentability=100,
                        metadata=GristMetadata(name='Sugar, Demerara'),
                        mass=100),
        ]
        grav = original_gravity(grists, 10, 0.65)
        # Test is in agreement with WWW
        self.assertEqual(round(grav, 1), 1005.4)

    def test_individual_gravity_withMashable(self):
        amber_malt = GristRecipe(ebc=60,
                                 mashable=True,
                                 extract=265,
                                 moisture=3,
                                 fermentability=200,
                                 metadata=GristMetadata(name='Amber Malt'),
                                 mass=100)
        grav = individual_gravity(amber_malt, 10, 0.75)
        self.assertEqual(round(grav, 1), 2.0)

    def test_individual_gravity_withNonMashable(self):
        sugar = GristRecipe(ebc=50,
                            mashable=False,
                            extract=370,
                            moisture=30,
                            fermentability=100,
                            metadata=GristMetadata(name='Sugar, Demerara'),
                            mass=100)
        grav = individual_gravity(sugar, 10, 0.75)
        self.assertEqual(round(grav, 1), 3.7)

    def test_graham_recipe_ebc_withMixedMashability(self):
        grists = [
            GristRecipe(ebc=60,
                        mashable=True,
                        extract=265,
                        moisture=3,
                        fermentability=200,
                        metadata=GristMetadata(name='Amber Malt'),
                        mass=100),
            GristRecipe(ebc=50,
                        mashable=False,
                        extract=370,
                        moisture=30,
                        fermentability=100,
                        metadata=GristMetadata(name='Sugar, Demerara'),
                        mass=100),
        ]
        ebc = graham_recipe_ebc(grists, 10, 0.75)
        self.assertEqual(round(ebc, 1), 9.5)


if __name__ == '__main__':
    unittest.main()
