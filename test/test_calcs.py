"""
A set of tests and documentation for the calculations available
"""
import unittest

from brew_maths.calc.abv import www_alcohol_by_volume_degrees
from brew_maths.calc.final_gravity import final_gravity
from brew_maths.calc.hop_bitterness import hop_ibu
from brew_maths.calc.hop_util import utilization
from brew_maths.calc.mash_liquor import mash_liquor
from brew_maths.calc.util import total_mass, percentage_by_mass
from brew_maths.calc.ebc import graham_recipe_ebc
from brew_maths.calc.original_gravity import original_gravity, individual_gravity
from brew_maths.recipe_objects.grist import GristRecipe, GristMetadata
from brew_maths.recipe_objects.hop import HopRecipe, HopMetadata


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
        self.assertEqual(400, total_mass(grists))

    def test_percentage_by_mass(self):
        grists = [
            GristRecipe(
                0, False, 0, 0, 0, None, 100
            ),
            GristRecipe(
                0, False, 0, 0, 0, None, 300
            ),
        ]
        self.assertEqual(400, total_mass(grists))
        self.assertEqual(0.25, percentage_by_mass(grists[0], grists))


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
        self.assertEqual(2, round(grav))

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
        self.assertEqual(3.7, round(grav, 1))

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
        self.assertEqual(5.7, round(grav, 1))

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
        self.assertEqual(1.9, round(grav, 1))

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
        self.assertEqual(5.4, round(grav, 1))

    def test_individual_gravity_withMashable(self):
        amber_malt = GristRecipe(ebc=60,
                                 mashable=True,
                                 extract=265,
                                 moisture=3,
                                 fermentability=None,
                                 metadata=GristMetadata(name='Amber Malt'),
                                 mass=100)
        grav = individual_gravity(amber_malt, 10, 0.75)
        self.assertEqual(2.0, round(grav, 1))

    def test_individual_gravity_withNonMashable(self):
        sugar = GristRecipe(ebc=50,
                            mashable=False,
                            extract=370,
                            moisture=30,
                            fermentability=1,
                            metadata=GristMetadata(name='Sugar, Demerara'),
                            mass=100)
        grav = individual_gravity(sugar, 10, 0.75)
        self.assertEqual(3.7, round(grav, 1))


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
        self.assertEqual(9.5, round(ebc, 1))


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
        self.assertEqual(0.2, round(mash_liq, 1))

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
        self.assertEqual(0, mash_liq)


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

        self.assertEqual(4.9, round(final_grav, 1))

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

        self.assertEqual(-45, round(final_grav, 1))


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
        abv = www_alcohol_by_volume_degrees(orig_grav, final_grav)
        self.assertEqual(40.4, round(abv, 1))


class TestIBU(unittest.TestCase):
    def test_hop_ibu(self):
        hop = HopRecipe(
            alpha=0.076,  # 7.6%
            metadata=HopMetadata(name='Challenger'),
            mass=100,
            time=90
        )
        ibu = hop_ibu(hop, 23, 1.000)
        # In agreement with Beer Engine
        self.assertEqual(128, round(ibu))

    def test_hop_ibu_withCorrection(self):
        hop = HopRecipe(
            alpha=0.076,  # 7.6%
            metadata=HopMetadata(name='Challenger'),
            mass=100,
            time=90
        )
        # gravity > 1.050 will add correction
        ibu = hop_ibu(hop, 23, 1.055)
        # In agreement with Beer Engine
        self.assertEqual(78, round(ibu))


class TestHopUtil(unittest.TestCase):
    def test_util(self):
        hop = HopRecipe(
            alpha=0.076,  # 7.6%
            metadata=HopMetadata(name='Challenger'),
            mass=100,
            time=90
        )
        ut = utilization(hop, 1.055)
        # agrees ~ with Beer Engine
        self.assertEqual(0.236, round(ut, 3))


if __name__ == '__main__':
    unittest.main()
