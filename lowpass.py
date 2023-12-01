from typing import List

from pozar import lut_3db_equalrip
from ReactiveComponents import Capacitor, Inductor
from pozar import get_g_equal_ripple


def scale_to_lowpass(r0: float, components: List[Inductor | Capacitor], fc: float):
    wc = 2 * 3.141592653589793 * fc
    scaled_values = {}
    for index, component in enumerate(components):
        if isinstance(component, Inductor):
            scaled_values[f"g{index + 1}"] = r0 * component.value * wc
        if isinstance(component, Capacitor):
            scaled_values[f"g{index + 1}"] = 1 / (r0 * component.value * wc)
    return scaled_values


# 1) Find order of filter.
omega = 3.535E9
omega_c = 2.9E9

x_axis_look = abs(omega / omega_c) - 1
print("X - Axis Lookup Value: ", x_axis_look)

g_value_components = get_g_equal_ripple(7, "C")
for component in g_value_components:
    print(component)
