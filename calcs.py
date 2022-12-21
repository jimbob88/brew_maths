from typing import List

from recipe_objects.grist import GristRecipe


def total_mass(grists: List[GristRecipe]) -> float:
    """Calculates the total mass of a set of grists"""
    return sum(
        grist.mass for grist in grists
    )


def percentage_by_mass(grist: GristRecipe, grists: List[GristRecipe]) -> float:
    """Gets the percentage by mass of a grist

    This is different from the way WWW calculates percentage (this returns the fractional value)
    """
    return grist.mass / total_mass(grists)


def original_gravity_points(grists: List[GristRecipe], efficiency: float = 0.75):
    """Calculates the `points` for the original_gravity calc"""
    return sum(
        (grist.extract * (grist.mass / 1000)) * (efficiency if grist.mashable else 1)
        for grist in grists
    )


def original_gravity(grists: List[GristRecipe], volume: float, efficiency: float = 0.75) -> float:
    """Calculates the original gravity of a recipe

    :param grists: The grains used
    :param volume: The target volume in litres
    :return: The original gravity in 1000 form, i.e. 1046.1
    """
    points = original_gravity_points(grists, efficiency)
    return (points / volume) + 1000
