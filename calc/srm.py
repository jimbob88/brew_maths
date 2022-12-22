from typing import Tuple


def force_rgb_range(value: float, lower_bound: float = 0, upper_bound: float = 255):
    """Keeps rgb value between 0 and 255"""
    return upper_bound if value > upper_bound else max(value, lower_bound)


def philip_lee_srm_to_rgb(srm: float) -> Tuple[float, float, float]:
    """
    Source: https://github.com/Brewtarget/brewtarget/blob/develop/src/Algorithms.cpp#L272 (22/12/2022)
    :param srm: Colour in SRM
    :return: the rgb as a tuple (red, green, blue)
    """
    red = 0.5 + (272.098 - 5.80255 * srm)
    red = min(red, 253)

    green = 0 if srm > 35 else 0.5 + (2.41975e2 - 1.3314e1 * srm + 1.881895e-1 * srm * srm)

    blue = 0.5 + (179.3 - 28.7 * srm)

    return (
        force_rgb_range(red),
        force_rgb_range(green),
        force_rgb_range(blue)
    )
