from enum import Enum


class Service(Enum):
    WARRANTY_REPAIR = 1
    OUT_OF_WARRANTY_REPAIR = 2
    CHANGE_OF_EQUIPMENT = 3
    SELL_OF_EQUIPMENT = 4


services_price = {
    1 : 0, 
    2 : 350,
    3 : 500,
    4 : 750,
}