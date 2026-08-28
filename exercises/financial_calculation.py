# Scenario 1: original investment
present_value_1 = 500
interest_rate_1 = 0.10
periods_1 = 24

# Formula: FV = PV * (1 + r) ** n (compound interest)
future_value_1 = present_value_1 * (1 + interest_rate_1) ** periods_1

# Scenario 2: same investment, lower interest rate
present_value_2 = 500
interest_rate_2 = 0.06
periods_2 = 24
future_value_2 = present_value_2 * (1 + interest_rate_2) ** periods_2

print("Scenario 1:")
print("Present value:", present_value_1)
print("Interest rate:", interest_rate_1)
print("Periods:", periods_1)
print("Future value:", round(future_value_1, 2))

print("\nScenario 2:")
print("Present value:", present_value_2)
print("Interest rate:", interest_rate_2)
print("Periods:", periods_2)
print("Future value:", round(future_value_2, 2))

# Comparison
diff = round(future_value_1 - future_value_2, 2)
print("\nScenario 1 earns", diff, "more than Scenario 2")