from typing import List

from brew_maths.recipe_objects.grist import GristRecipe


def total_mass(grists: List[GristRecipe]) -> float:
    """Calculates the total mass of a set of grists in grams"""
    return sum(
        grist.mass for grist in grists
    )


def total_mass_of_mashables(grists: List[GristRecipe]):
    return sum(
        grist.mass for grist in grists if grist.mashable
    )


def percentage_by_mass(grist: GristRecipe, grists: List[GristRecipe]) -> float:
    """Gets the percentage by mass of a grist

    This is different from the way WWW calculates percentage (this returns the fractional value)
    """
    return grist.mass / total_mass(grists)
