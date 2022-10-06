import math
from typing import Union


def calc_circle(diameter: Union[float, int], double_up:int= 1, rounding: int=3) -> Union[float, int]:
    '''
    Function to calculate the size of a circle

    
    Params:
    * diameter

    Returns:
    * size of the diameter
    '''

    # validate the types
    available_types = [int, float]

    if type(diameter) not in available_types:
        raise TypeError("This is not the right type")

    # execute the calculation
    radius = diameter / 2 
    size = radius ** 2 * math.pi
    size_rounded = round(size, rounding) * double_up
    
    return size_rounded