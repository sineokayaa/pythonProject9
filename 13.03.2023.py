import ru_local as ru

ptrl_g = float(input())  # Petrol input (in gallons).
ptrl_l = ptrl_g * 3.785  # Petrum volume(litres).
oil_b = ptrl_g/19.5  # The amount of burrels of oil to produse gasoline.
co2 = ptrl_g * 20  # Volume of carbon dioxide burning in the engine of this gasoline.
enrgy_ptrl_g = ptrl_g * 115000  # Gasoline energy.
ethnl_g = enrgy_ptrl_g/75700  # Equivalent volume of ethanol (in gallons).
cost = ptrl_g * 3  # Gasoline cost (USD).
V = 0.766  # The number of litres of gasoline that Russians spend per day on average.
V_nsk = V * 1576000  # Approximate gas consumption (in liters) for Novosibirsk.
V_rus = V * 146424729 * 365  # Approximate gasoline consumption (in liters) for Russia.

print(ru.PTRL_G, ptrl_g)
print(ru.PTRL_L, ptrl_l)
print(ru.OIL_B, oil_b)
print(ru.CO2, co2)
print(ru.ETHNL_G, ethnl_g)
print(ru.COST, cost)
print(ru.V_NSK, V_nsk)
print(ru.V_RUS, V_rus)
