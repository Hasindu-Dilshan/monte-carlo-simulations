import random
import math

radius = 1
num_simulations = 1000000

inside_circle = 0

for i in range(num_simulations):

    # 0.0 <= random.random() <= 1.0
    x = random.random()
    y = random.random()

    # For every float x & y , 0 <= sqrt(x^2 + y^2) <= sqrt(2) ==> 0 <= x^2 + y^2 <= 2
    position_square = x ** 2 + y ** 2

    if position_square <= 1:
        inside_circle += 1

ratio_darts = inside_circle / num_simulations
ratio_areas = (math.pi * radius * radius) / (radius * 4)

# print(inside_circle)

print(f"\nnumber of simulations: {num_simulations:,}\n")
print(f"dart ratio : {ratio_darts}")
print(f"area ratio : {ratio_areas}")
