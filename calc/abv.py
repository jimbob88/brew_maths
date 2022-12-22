from typing import NamedTuple, List, Optional


def www_alcohol_by_volume(original_gravity: float, final_gravity: float) -> float:
    """

    :param original_gravity: Original gravity (in full, for example 1.045)
    :param final_gravity: Final gravity (in full, for example 1.031)
    :return: ABV
    """
    return ((1.05 * (original_gravity - final_gravity)) / final_gravity / 0.79) * 100


def www_alcohol_by_volume_degrees(og_degrees: float, fg_degrees: float) -> float:
    """

    :param og_degrees: in degrees, i.e. 45
    :param fg_degrees: in degrees, i.e. 31
    :return: ABV (i.e. 0.69 = 0.69% ABV)
    """
    original_gravity = (1000 + og_degrees) / 1000
    final_gravity = (1000 + fg_degrees) / 1000
    return www_alcohol_by_volume(original_gravity, final_gravity)


def ritchie_abv(original_gravity: float, final_gravity: float) -> float:
    """
    Code Source: https://github.com/Brewtarget/brewtarget/blob/develop/src/Algorithms.cpp#L532
    Source: http://www.brewersfriend.com/2011/06/16/alcohol-by-volume-calculator-updated/

    "[This] formula, and variations on it, comes from Ritchie Products Ltd, (Zymurgy, Summer 1995, vol. 18, no. 2)
    Michael L. Hall’s article Brew by the Numbers: Add Up What’s in Your Beer, and Designing Great Beers by Daniels.
       ...
    The relationship between the change in gravity, and the change in ABV is not linear. All these equations are
    approximations."

    :param original_gravity: Original gravity (in full, for example 1.045)
    :param final_gravity: Final gravity (in full, for example 1.031)
    :return: ABV (i.e. 0.69 = 0.69% ABV)
    """
    return (76.08 * (original_gravity - final_gravity) / (1.775 - original_gravity)) * (final_gravity / 0.794)


class ABVFactor(NamedTuple):
    excess_gravity_diff_min: float
    excess_gravity_diff_max: float
    abv_min: float  # sanity check
    abv_max: float  # sanity check
    factor: float


GOV_UK_ABV_FACTOR: List[ABVFactor] = [
    ABVFactor(0, 6.9, 0, 0.8, 0.125),
    ABVFactor(7.0, 10.4, 0.8, 1.3, 0.126),
    ABVFactor(10.5, 17.2, 1.3, 2.1, 0.127),
    ABVFactor(17.3, 26.1, 2.2, 3.3, 0.128),
    ABVFactor(26.2, 36.0, 3.3, 4.6, 0.129),
    ABVFactor(36.1, 46.5, 4.6, 6.0, 0.130),
    ABVFactor(46.6, 57.1, 6.0, 7.5, 0.131),
    ABVFactor(57.2, 67.9, 7.5, 9.0, 0.132),
    ABVFactor(68.0, 78.8, 9.0, 10.5, 0.133),
    ABVFactor(78.9, 89.7, 10.5, 12.0, 0.134),
    ABVFactor(89.8, 100.7, 12.0, 13.6, 0.135)
]


def find_gov_uk_factor(excess_gravity_diff: float) -> Optional[ABVFactor]:
    """

    :param excess_gravity_diff: Should be rounded to one decimal place
    :return: ABVFactor, if not in range, returns None
    """
    return next((factor for factor in GOV_UK_ABV_FACTOR
                 if factor.excess_gravity_diff_min <= excess_gravity_diff <= factor.excess_gravity_diff_max), None)


def gov_uk_abv(original_gravity: float, final_gravity: float, sanity_check: bool = False):
    """

    SOURCE: https://www.gov.uk/government/publications/excise-notice-226-beer-duty/excise-notice-226-beer-duty--2#calculation-strength

    :param original_gravity: The original gravity (in full, i.e. 1.045)
    :param final_gravity: The final gravity (in full, i.e. 1.031)
    :param sanity_check: If true, raises value error if abv not in expected range
    :return: ABV (i.e. 4.5 = 4.5% ABV)
    """
    excess_gravity_diff = round(original_gravity - final_gravity, 1)
    factor = find_gov_uk_factor(excess_gravity_diff)

    # fallback, use ritchie formula
    if factor is None:
        return ritchie_abv(original_gravity, final_gravity)

    abv = excess_gravity_diff * factor.factor

    if sanity_check and not (factor.abv_min <= abv <= factor.abv_max):
        raise ValueError(f"{abv} not in range [{factor.abv_min}, {factor.abv_max}]")

    return abv
