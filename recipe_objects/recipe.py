import dataclasses
from typing import List

from recipe_objects.grist import Grist, GristRecipe
from recipe_objects.hop import Hop


@dataclasses.dataclass
class Recipe:
    grists: List[GristRecipe]
    hops: List[Hop]
