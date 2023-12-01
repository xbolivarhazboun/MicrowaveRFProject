from typing import List

from pozar import lut_3db_equalrip
from ReactiveComponents import Capacitor, Inductor
from pozar import get_g_equal_ripple


def scale_to_highpass(r0: float, components: List[Inductor | Capacitor], fc: float):
    wc = 2 * 3.141592653589793 * fc
    scaled_values = {}
    for index, component in enumerate(components):
        if isinstance(component, Inductor):
            scaled_values[f"g{index + 1}"] = 1 / (r0 * component.value * wc)
        if isinstance(component, Capacitor):
            scaled_values[f"g{index + 1}"] = r0 / (component.value * wc)
    return scaled_values


low_pass_prototype = get_g_equal_ripple(5, "L")

g_scaled = scale_to_highpass(50, low_pass_prototype, 3.0E9)
print(g_scaled)
