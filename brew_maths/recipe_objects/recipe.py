import dataclasses
from typing import List

from brew_maths.recipe_objects.grist import GristRecipe
from brew_maths.recipe_objects.hop import HopRecipe


@dataclasses.dataclass
class Recipe:
    grists: List[GristRecipe]
    hops: List[HopRecipe]
