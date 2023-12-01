from ReactiveComponents import Capacitor, Inductor

from pozar import *
from scipy.constants import c

f1 = 2.125E9
w1 = 2 * pi * f1
f2 = 2.875E9
w2 = 2 * pi * f2
f3 = 1.525E9
w3 = 2 * pi * f3
f4 = 1.705E9
w4 = 2 * pi * f4
f5 = 3.535E9
w5 = 2 * pi * f5
f6 = 5
w6 = 2 * pi * f6
w0 = sqrt(w1 * w2)
print(f"f0: {w0 / (2 * pi * 1E9)} GHz")
delta = (w2 - w1) / w0
print({"w1": w1, "w2": w2, "delta": delta})

w_lp = 1 / delta * (w4 / w0 - w0 / w4)

table_value = abs(w_lp / 1) - 1
print("Table Value:", table_value)

# g_values = [1.0, 1.7504, 1.2690, 2.6678, 1.3673, 2.7239, 1.3673, 2.6678, 1.2690, 1.7504, 1.0]


g_values = get_g_equal_ripple(7, "C")
g_val_raw = []
for i, g in enumerate(g_values):
    if i == 0:
        g_val_raw.append(g)
    else:
        g_val_raw.append(g.value)

g_values = g_val_raw

g_values = [1.0, 0.3473, 1.0000, 1.5321, 1.8794, 2.0000, 1.8794, 1.5321, 1.0000, 0.3473, 1.0000]
# Could have used get_g_equal_ripple, but we had trouble controlling the return loss and figured the
# conical shape of was better suited since it's monotonic in the passband.
print("G Values:", g_values)
j_values = calculate_Jz0(9, .303, g_values, 50)
print("J*z0 Values:", j_values)
z0e_values = get_z0e(j_values, 30)
z0o_values = get_z0o(j_values, 30)
print(f"Z0e Values [{len(z0e_values)}]: {z0e_values}")
print(f"Z0o Values [{len(z0o_values)}]: {z0o_values}")

# b_values = get_b_values(50, j_values)
# print("B Values:", b_values)
# theta_values = get_theta_values(50, b_values)
# theta_values_deg = [radians_to_degrees(theta) for theta in theta_values]
# print("Theta Values [Degrees]:", theta_values_deg)
# # cns = get_cns(b_values, f * 2 * pi)
# # print(f"Cn Values: [{len(cns)}]", cns)

# lmbda = c / f  # meters

# print("Physical Lengths:",
#       [c * theta / (2 * pi * f) for theta in theta_values],
#       "meters"
#       )
# J = 0.2065
#
# print(J / (1 - (1 * J) ** 2))
# print(get_b_values(50, [0.2065]))
