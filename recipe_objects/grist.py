import dataclasses
from enum import Enum
from typing import Optional


class GristType(Enum):
    PRIMARY_MALT = 1
    SECONDARY_MALT = 2
    MASH_TUN_ADJUNCT = 3
    CAN_BE_STEEPED = 4
    MALT_EXTRACT = 5  # Non Mashable
    COPPER_SUGAR = 6  # Non Mashable


NON_MASHABLES = {GristType.MALT_EXTRACT, GristType.COPPER_SUGAR}


@dataclasses.dataclass
class GristMetadata:
    name: Optional[str] = None
    description: Optional[str] = None
    type: Optional[GristType] = None


@dataclasses.dataclass
class Grist:
    """Grain or Malt"""
    ebc: float
    mashable: bool
    extract: float
    moisture: float
    fermentability: float
    metadata: Optional[GristMetadata] = None


@dataclasses.dataclass
class GristRecipe(Grist):
    mass: float = 0  # in grams
