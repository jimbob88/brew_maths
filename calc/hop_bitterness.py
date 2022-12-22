from calc.hop_util import utilization
from recipe_objects.hop import HopRecipe


# TODO: Create hop util functions first
# https://github.com/jimbob88/wheelers-wort-works/blob/79e2e1b811e147cc0f54a7c063df02e527c74a59/beer_engine.py#L1178


def hop_ibu(hop: HopRecipe, volume: float, boil_gravity: float) -> float:
    """

    Source: http://www.backtoschoolbrewing.com/blog/2016/9/5/how-to-calculate-ibus

    :param hop: The hop to calculate ibus for
    :param volume: The target volume of the beer
    :param boil_gravity: The original gravity, calculated using the boil_volume (i.e. 1.050)
    :return: IBUs of an individual hop
    """
    correction = 1
    if boil_gravity > 1.050:
        correction = 1 + (boil_gravity - 1.05) / 2

    return (hop.mass * hop.alpha * utilization(hop, boil_gravity) * 1000) / (volume * correction)
