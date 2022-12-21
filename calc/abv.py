def alcohol_by_volume(original_gravity: float, final_gravity: float) -> float:
    """

    :param original_gravity: Original gravity (in full, for example 1.045)
    :param final_gravity: Final gravity (in full, for example 1.031)
    :return: ABV
    """
    return ((1.05 * (original_gravity - final_gravity)) / final_gravity / 0.79) * 100


def alcohol_by_volume_degrees(og_degrees: float, fg_degrees: float) -> float:
    """

    :param og_degrees: in degrees, i.e. 45
    :param fg_degrees: in degrees, i.e. 31
    :return: ABV
    """
    original_gravity = (1000 + og_degrees) / 1000
    final_gravity = (1000 + fg_degrees) / 1000
    return alcohol_by_volume(original_gravity, final_gravity)
