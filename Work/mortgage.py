# mortgage.py
#
# Exercise 1.7

principal = 500_000
interest_rate = 0.05
monthly_pay = 2684.11
total_paid = 0

while principal:
  principal = max(principal * (1 + interest_rate/12) - monthly_pay, 0)
  total_paid += monthly_pay

print(f'Total paid: ${round(total_paid, 2)}')
