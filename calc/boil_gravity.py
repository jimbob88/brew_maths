from typing import List

from calc.original_gravity import original_gravity
from recipe_objects.grist import Grist, GristRecipe


def boil_gravity(grists: List[GristRecipe], boil_volume: float, efficiency: float = 0.75):
    """Alias for boil gravity, it's the same as original gravity, but simply uses boil volume instead"""
    return original_gravity(grists, boil_volume, efficiency)
