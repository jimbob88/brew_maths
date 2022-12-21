from typing import Optional, List

from calc.original_gravity import original_gravity_points
from recipe_objects.grist import GristRecipe


def apply_attenuation(fermentability: Optional[float], attenuation: float) -> float:
    """

    :param fermentability: The fermentability (i.e. for sugars 1, for malts None)
    :param attenuation: The default attenuation, a common value is 0.62 (Medium 66C)
    :return: The fermentability of a grist
    """
    return fermentability if fermentability is not None else attenuation


def final_gravity(grists: List[GristRecipe], volume: float, efficiency: float = 0.75, attenuation: float = 0.62):
    """Returns final gravity in brewer's degrees"""
    a = sum(
        apply_attenuation(grist.fermentability, attenuation)
        * (grist.mass / 1000)
        * grist.extract
        * (efficiency if grist.mashable else 1)
        for grist in grists
    )
    b = sum(
        (1 - apply_attenuation(grist.fermentability, attenuation))
        * (grist.mass / 1000)
        * grist.extract
        * (efficiency if grist.mashable else 1)
        for grist in grists
    )
    return (b - (a * 0.225)) / volume
