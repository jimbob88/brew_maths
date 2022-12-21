import unittest

from calc.abv import alcohol_by_volume_degrees
from calc.final_gravity import final_gravity
from calc.mash_liquor import mash_liquor
from calc.util import total_mass, percentage_by_mass
from calc.ebc import graham_recipe_ebc
from calc.original_gravity import original_gravity, individual_gravity, original_gravity_points
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


class TestOriginalGravity(unittest.TestCase):
    def test_original_gravity_withMashableMalt(self):
        grists = [
            GristRecipe(ebc=60,
                        mashable=True,
                        extract=265,
                        moisture=3,
                        fermentability=None,
                        metadata=GristMetadata(name='Amber Malt'),
                        mass=100)
        ]
        grav = original_gravity(grists, 10, 0.75)
        # Test is in agreement with WWW
        self.assertEqual(round(grav), 2)

    def test_original_gravity_withUnmashableSugar(self):
        grists = [
            GristRecipe(ebc=50,
                        mashable=False,
                        extract=370,
                        moisture=30,
                        fermentability=1,
                        metadata=GristMetadata(name='Sugar, Demerara'),
                        mass=100)
        ]
        grav = original_gravity(grists, 10, 0.75)
        # Test is in agreement with WWW
        self.assertEqual(round(grav, 1), 3.7)

    def test_original_gravity_withGrists(self):
        grists = [
            GristRecipe(ebc=60,
                        mashable=True,
                        extract=265,
                        moisture=3,
                        fermentability=None,
                        metadata=GristMetadata(name='Amber Malt'),
                        mass=100),
            GristRecipe(ebc=50,
                        mashable=False,
                        extract=370,
                        moisture=30,
                        fermentability=1,
                        metadata=GristMetadata(name='Sugar, Demerara'),
                        mass=100),
        ]
        grav = original_gravity(grists, 10, 0.75)
        # Test is in agreement with WWW
        self.assertEqual(round(grav, 1), 5.7)

    def test_original_gravity_withDifferentTargetVolume(self):
        grists = [
            GristRecipe(ebc=60,
                        mashable=True,
                        extract=265,
                        moisture=3,
                        fermentability=None,
                        metadata=GristMetadata(name='Amber Malt'),
                        mass=100),
            GristRecipe(ebc=50,
                        mashable=False,
                        extract=370,
                        moisture=30,
                        fermentability=1,
                        metadata=GristMetadata(name='Sugar, Demerara'),
                        mass=100),
        ]
        grav = original_gravity(grists, 30, 0.75)
        # Test is in agreement with WWW
        self.assertEqual(round(grav, 1), 1.9)

    def test_original_gravity_withDifferentEfficiency(self):
        grists = [
            GristRecipe(ebc=60,
                        mashable=True,
                        extract=265,
                        moisture=3,
                        fermentability=None,
                        metadata=GristMetadata(name='Amber Malt'),
                        mass=100),
            GristRecipe(ebc=50,
                        mashable=False,
                        extract=370,
                        moisture=30,
                        fermentability=1,
                        metadata=GristMetadata(name='Sugar, Demerara'),
                        mass=100),
        ]
        grav = original_gravity(grists, 10, 0.65)
        # Test is in agreement with WWW
        self.assertEqual(round(grav, 1), 5.4)

    def test_individual_gravity_withMashable(self):
        amber_malt = GristRecipe(ebc=60,
                                 mashable=True,
                                 extract=265,
                                 moisture=3,
                                 fermentability=None,
                                 metadata=GristMetadata(name='Amber Malt'),
                                 mass=100)
        grav = individual_gravity(amber_malt, 10, 0.75)
        self.assertEqual(round(grav, 1), 2.0)

    def test_individual_gravity_withNonMashable(self):
        sugar = GristRecipe(ebc=50,
                            mashable=False,
                            extract=370,
                            moisture=30,
                            fermentability=1,
                            metadata=GristMetadata(name='Sugar, Demerara'),
                            mass=100)
        grav = individual_gravity(sugar, 10, 0.75)
        self.assertEqual(round(grav, 1), 3.7)


class TestEBC(unittest.TestCase):
    def test_graham_recipe_ebc_withMixedMashability(self):
        grists = [
            GristRecipe(ebc=60,
                        mashable=True,
                        extract=265,
                        moisture=3,
                        fermentability=None,
                        metadata=GristMetadata(name='Amber Malt'),
                        mass=100),
            GristRecipe(ebc=50,
                        mashable=False,
                        extract=370,
                        moisture=30,
                        fermentability=1,
                        metadata=GristMetadata(name='Sugar, Demerara'),
                        mass=100),
        ]
        ebc = graham_recipe_ebc(grists, 10, 0.75)
        self.assertEqual(round(ebc, 1), 9.5)


class TestMashLiqour(unittest.TestCase):
    def test_mash_liquor_withMixedMashability(self):
        grists = [
            GristRecipe(ebc=60,
                        mashable=True,
                        extract=265,
                        moisture=3,
                        fermentability=None,
                        metadata=GristMetadata(name='Amber Malt'),
                        mass=100),
            GristRecipe(ebc=50,
                        mashable=False,
                        extract=370,
                        moisture=30,
                        fermentability=1,
                        metadata=GristMetadata(name='Sugar, Demerara'),
                        mass=100),
        ]
        mash_liq = mash_liquor(grists, 2.5)
        self.assertEqual(round(mash_liq, 1), 0.2)

    def test_mash_liquor_withNoMashables(self):
        grists = [GristRecipe(ebc=50,
                              mashable=False,
                              extract=370,
                              moisture=30,
                              fermentability=1,
                              metadata=GristMetadata(name='Sugar, Demerara'),
                              mass=100),
                  ]
        mash_liq = mash_liquor(grists, 2.5)
        self.assertEqual(mash_liq, 0)


class TestFinalGravity(unittest.TestCase):
    def test_final_gravity(self):
        grists = [
            GristRecipe(ebc=60,
                        mashable=True,
                        extract=265,
                        moisture=3,
                        fermentability=None,
                        metadata=GristMetadata(name='Amber Malt'),
                        mass=1100),
            GristRecipe(ebc=50,
                        mashable=False,
                        extract=370,
                        moisture=30,
                        fermentability=1,
                        metadata=GristMetadata(name='Sugar, Demerara'),
                        mass=40),
        ]
        final_grav = final_gravity(grists, 10, 0.75, 0.62)

        self.assertEqual(round(final_grav, 1), 4.9)

    def test_final_gravity_withLotsOfSugar(self):
        grists = [
            GristRecipe(ebc=60,
                        mashable=True,
                        extract=265,
                        moisture=3,
                        fermentability=None,
                        metadata=GristMetadata(name='Amber Malt'),
                        mass=1100),
            GristRecipe(ebc=50,
                        mashable=False,
                        extract=370,
                        moisture=30,
                        fermentability=1,
                        metadata=GristMetadata(name='Sugar, Demerara'),
                        mass=6040),
        ]
        final_grav = final_gravity(grists, 10, 0.75, 0.62)

        self.assertEqual(round(final_grav, 1), -45)


class TestABV(unittest.TestCase):
    def test_alcohol_by_volume_degrees_withLotsOfSugar(self):
        grists = [
            GristRecipe(ebc=60,
                        mashable=True,
                        extract=265,
                        moisture=3,
                        fermentability=None,
                        metadata=GristMetadata(name='Amber Malt'),
                        mass=1100),
            GristRecipe(ebc=50,
                        mashable=False,
                        extract=370,
                        moisture=30,
                        fermentability=1,
                        metadata=GristMetadata(name='Sugar, Demerara'),
                        mass=6040),
        ]
        orig_grav = original_gravity(grists, 10, 0.75)
        final_grav = final_gravity(grists, 10, 0.75, 0.62)
        abv = alcohol_by_volume_degrees(orig_grav, final_grav)
        self.assertEqual(round(abv, 1), 40.4)


if __name__ == '__main__':
    unittest.main()
