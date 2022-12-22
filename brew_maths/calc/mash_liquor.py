from typing import List

from brew_maths.calc.util import total_mass_of_mashables
from brew_maths.recipe_objects.grist import GristRecipe


def mash_liquor(grists: List[GristRecipe], lgr: float = 2.5) -> float:
    """Source: https://byo.com/article/managing-mash-thickness/

    :param grists: The grists to calculate from
    :param lgr: The Liquor to Grist Ratio (2.5 or 3.2 are common values used by brewers)
    """
    grist_mass_kg = total_mass_of_mashables(grists) / 1000
    return grist_mass_kg * lgr
