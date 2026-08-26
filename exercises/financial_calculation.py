present_value = 500
interest_rate = 0.10
periods = 24
future_value = present_value * (1 + interest_rate) ** periods
print("Present value:", present_value)
print("Interest rate:", interest_rate)
print("Periods:", periods)
print("Future value:", round(future_value, 2))

interest_earned = future_value - present_value
print("Interest earned:", round(interest_earned, 2))