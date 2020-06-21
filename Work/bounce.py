# bounce.py
#
# Exercise 1.5

height = 100 # m

for i in range(10):
  height = 3/5 * height
  print(i+1, round(height, 4))
