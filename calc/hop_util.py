import math

from recipe_objects.hop import HopRecipe


def utilization(hop: HopRecipe, boil_gravity: float):
    """
    Utilization = f(G) x f(T)
    f(G) = 1.65 x 0.000125^(Gb - 1)
    f(T) = [1 - e^(-0.04 x T)] / 4.15
    Where Gb is boil gravity and T is time

    :param hop: The hop to calculate util for
    :param boil_gravity: Boil gravity, i.e. 1.045
    :return: The utilization rate, i.e. 0.69 = 69%
    """
    fG = 1.65 * (0.000125 ** (boil_gravity - 1))
    fT = (1 - math.e ** (-0.04 * hop.time)) / 4.15
    return fG * fT
