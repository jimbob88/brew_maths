import dataclasses
from typing import Optional


@dataclasses.dataclass
class HopMetadata:
    form: str
    origin: str
    use: str


@dataclasses.dataclass
class Hop:
    alpha: float
    metadata: Optional[HopMetadata] = None
