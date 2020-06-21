# mortgage.py
#
# Exercise 1.7

from itertools import count

principal = 500_000
interest_rate = 0.05
monthly_pay = 2684.11
total_paid = 0

for i in count(1):
  pay = monthly_pay
  if i <= 12:
    pay += 1000
  principal = max(principal * (1 + interest_rate/12) - pay, 0)
  total_paid += pay
  if not principal:
    break

print(f'Total paid ${round(total_paid, 2)} over {i} months')
