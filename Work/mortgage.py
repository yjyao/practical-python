# mortgage.py
#
# Exercise 1.7

from itertools import count

extra_payment_start_month = 60 # year 5
extra_payment_end_month = 108 # year 9
extra_payment = 1000

principal = 500_000
interest_rate = 0.05
monthly_pay = 2684.11
total_paid = 0

for i in count(1):
  pay = monthly_pay
  if extra_payment_start_month <= i <= extra_payment_end_month:
    pay += extra_payment
  principal = max(principal * (1 + interest_rate/12) - pay, 0)
  total_paid += pay
  print(i, total_paid, principal)
  if not principal:
    break

print(f'Total paid ${round(total_paid, 2)} over {i} months')
