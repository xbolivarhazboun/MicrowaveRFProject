from math import pi, sqrt, atan, atan2
from typing import List

from ReactiveComponents import Capacitor, Inductor

lut_3db_equalrip = {
    1: [1.9953, 1.0000],
    2: [3.1013, 0.5339, 5.8095],
    3: [3.3487, 0.7117, 3.3487, 1.0000],
    4: [3.4389, 0.7483, 4.3471, 0.5920, 5.8095],
    5: [3.4817, 0.7618, 4.5381, 0.7618, 3.4817, 1.0000],
    6: [3.5045, 0.7685, 4.6061, 0.7929, 4.4641, 0.6033, 5.8095],
    7: [3.5182, 0.7723, 4.6386, 0.8039, 4.6386, 0.7723, 3.5182, 1.0000],
    8: [3.5277, 0.7745, 4.6575, 0.8089, 4.6990, 0.8018, 4.4990, 0.6073, 5.8095],
    9: [3.5340, 0.7760, 4.6692, 0.8118, 4.7272, 0.8118, 4.6692, 0.7760, 3.5340, 1.0000],
    10: [3.5384, 0.7771, 4.6768, 0.8136, 4.7425, 0.8164, 4.7260, 0.8051, 4.5142, 0.6091, 5.8095],
}


def get_g_equal_ripple(order: int, first_component: str):
    reactive_g_values = [1]
    g_values = lut_3db_equalrip[order]
    if first_component == "C":
        for index, g in enumerate(g_values):
            if index % 2 == 0:
                reactive_g_values.append(Capacitor(g))
            else:
                reactive_g_values.append(Inductor(g))
    elif first_component == "L":
        for index, g in enumerate(g_values):
            if index % 2 == 0:
                reactive_g_values.append(Inductor(g))
            else:
                reactive_g_values.append(Capacitor(g))
    return reactive_g_values


def calculate_Jz0(N, Delta, g_values, z0):
    if N < 1 or len(g_values) != N + 2:
        raise ValueError("Invalid input. N should be at least 1, and g_values should have N+1 elements.")

    J_over_Y0_values = []

    # First element
    J_over_Y0_values.append(sqrt(pi * Delta / (2 * g_values[0] * g_values[1])))

    # Middle elements
    for k in range(1, N):
        J_over_Y0_values.append((pi * Delta / 2) / sqrt(g_values[k] * g_values[k + 1]))

    # Last element
    J_over_Y0_values.append(sqrt((pi / 2) * Delta / (g_values[N] * g_values[N + 1])))

    return [x for x in J_over_Y0_values]


def get_z0e(jz0_values: List[float], z0: float) -> List[float]:
    z0e_values = []
    for jz0 in jz0_values:
        z0e = z0*(1+jz0+jz0**2)
        z0e_values.append(z0e)
    return z0e_values

def get_z0o(jz0_values: List[float], z0: float) -> List[float]:
    z0o_values = []
    for jz0 in jz0_values:
        z0o = z0*(1-jz0+jz0**2)
        z0o_values.append(z0o)
    return z0o_values


def get_b_values(z0, j_values: List[float]):
    return [J / (1 - (z0 * J) ** 2) for J in j_values]


def get_theta_values(z0, b_values):
    """

    :param z0: Characteristic impedance
    :param b_values: Series admittance values
    :return: Electrical length of each section in degrees
    """
    b = b_values
    thetas = []
    for i in range(len(b_values) - 1):
        thetas.append(pi - 1 / 2 *
                      (atan(2 * z0 * b[i]) + atan(2 * z0 * b[i + 1]))
                      )
    return thetas


def radians_to_degrees(radians):
    return radians * 180 / pi


def get_cns(bn, w0):
    return [bn / w0 for bn in bn]
