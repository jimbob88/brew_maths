from typing import List

from recipe_objects.grist import GristRecipe


def graham_grist_ebc_in_solution(grist: GristRecipe, volume: float, efficiency: float = 0.75) -> float:
    """https://www.lovibond.com/en/PC/Colour-Measurement/Colour-Scales-Standards/EBC-European-Brewing-Convention"""
    mass_kg = grist.mass / 1000
    eff = efficiency if grist.mashable else 1
    #  The EBC 430nm method specifies a fixed path length of 10mm.
    return (grist.ebc * mass_kg * eff * 10) / volume


def graham_recipe_ebc(grists: List[GristRecipe], volume: float, efficiency: float = 0.75) -> float:
    """Graham's Formula used in Beer Engine: https://www.jimsbeerkit.co.uk/forum/viewtopic.php?t=26000"""
    return sum(
        graham_grist_ebc_in_solution(grist, volume, efficiency) for grist in grists
    )
