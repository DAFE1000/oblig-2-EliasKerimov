import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return np.e ** (-x/4) * np.arctan(x)

def fp(x):
    return np.arctan(x) - 4/(x**2 + 1)

x_values = np.linspace(-5,5,10000)


best_x = x_values[0]
best_value = abs(fp(best_x))

for x in x_values:
    if abs(fp(x)) < best_value:
        best_value = abs(fp(x))
        best_x = x

best_y = f(best_x)

print("Toppunkt:")
print("x =", round(best_x,4)eli)
print("y =", round(best_y,4))

y_values = f(x_values)

plt.plot(x_values,y_values)
plt.scatter(best_x,best_y,color="red")
plt.title("Plot av funksjonen")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.show()