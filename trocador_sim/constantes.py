import pint
from typing import Union

UREG = pint.UnitRegistry()
Q_ = UREG.Quantity
Unit = Union[Q_, float, int]