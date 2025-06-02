import math

h = float(input("Leangth of pendulum (meters): "))

t = (2 * math.pi) * math.sqrt(h / 9.81)

print(f"time(seconds): {t:.2f}.")