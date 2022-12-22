from typing import List

from brew_maths.recipe_objects.grist import GristRecipe


def original_gravity_points(grist: GristRecipe, efficiency: float = 0.75):
    """Calculates the `points` for the original_gravity calc (alongside efficiency)

    In Graham Wheeler's Home Brewing, this value is referred to as the `brewer's degrees`
    """
    mass_kg = (grist.mass / 1000)
    return (grist.extract * mass_kg) * (efficiency if grist.mashable else 1)


def original_gravity(grists: List[GristRecipe], volume: float, efficiency: float = 0.75) -> float:
    """Calculates the original gravity of a recipe

    :param grists: The grains used
    :param volume: The target volume in litres
    :param efficiency: Percentage efficiency (true extract vs experimental extract multiplier)
    :return: The original gravity in brewer's degrees
    """
    points = sum(original_gravity_points(grist, efficiency) for grist in grists)
    return points / volume


def individual_gravity(grist: GristRecipe, volume: float, efficiency: float = 0.75) -> float:
    """
    :return: The gravity of a grist in non 1000 form (i.e. 2.7 instead of 1002.7)
    """
    return original_gravity_points(grist, efficiency) / volume

# TODO: Add a system for calculating percentage + orig_grav -> mass
# https://github.com/jimbob88/wheelers-wort-works/blob/master/beer_engine.py#L1066
