# Calculate pi via montecarlo
import random
N = input("How many points? ")
counter = 0
for i in range (0,int(N)):
    x = random.random()
    y = random.random()
    d = x**2 + y**2
    if d <= 1:
        counter = counter + 1
    pi = (4*counter/int(N))
print(pi)