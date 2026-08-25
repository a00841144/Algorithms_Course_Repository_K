present_value = 1500
interest_rate = 0.07
periods = 12

future_value = present_value * (1 + interest_rate) ** periods

print("Present value:", present_value)
print("Interest rate:", interest_rate)
print("Periods:", periods)
print("Future value:", round(future_value, 2))