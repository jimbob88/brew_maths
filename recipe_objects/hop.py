import dataclasses
from typing import Optional


@dataclasses.dataclass
class HopMetadata:
    name: Optional[str] = None
    form: Optional[str] = None
    origin: Optional[str] = None
    use: Optional[str] = None


@dataclasses.dataclass
class Hop:
    alpha: float  # percentage, for example alpha=0.8, means 80% alpha
    metadata: Optional[HopMetadata] = None


@dataclasses.dataclass
class HopRecipe(Hop):
    mass: float = 0  # in grams
    time: float = 0  # in minutes
