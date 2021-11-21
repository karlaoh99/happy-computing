import math
import numpy as np
from services import Service


def uniform():
    return np.random.uniform()


def exponential(l):
    return -(1/l) * math.log(uniform())


def poisson(l):
    x = 0
    u = uniform()
    while u >= math.e ** (-l):
        u *= uniform()
        x += 1
    return x


def normal(mu, sigma):
    e1 = 0
    e2 = 0
    while (e2 - (((e1 - 1) ** 2) / 2)) <= 0:
        e1 = exponential(1)
        e2 = exponential(1)
    u = uniform()
    result = e1 if u > 0.5 else -e1
    return result * math.sqrt(sigma) + mu


def generate_service_type():
    u = uniform()
    if u <= 0.45:
        return Service.WARRANTY_REPAIR
    if 0.45 < u <= 0.70:
        return Service.OUT_OF_WARRANTY_REPAIR
    if 0.70 < u <= 0.80:
        return Service.CHANGE_OF_EQUIPMENT
    if 0.80 < u <= 1:
        return Service.SELL_OF_EQUIPMENT


def generate_arrival_time():
    return poisson(20)


def generate_seller_time():
    return normal(5, 2)


def generate_repair_time():
    return exponential(1/20)


def generate_change_time():
    return exponential(1/15)