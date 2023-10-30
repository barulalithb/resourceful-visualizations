import numpy as np
import matplotlib.pyplot as plt

# Define a range of coordinates
x_range = np.linspace(-1, 1, 100)
y_range = np.linspace(-1, 1, 100)

# Create a grid of coordinates
X, Y = np.meshgrid(x_range, y_range)

# List of p values
p_values = [0.5, 1, 2, 3, 5]

# Create a figure
plt.figure(figsize=(10, 10), dpi=300)

# Plot Lp Norms for each p value
for p in p_values:
    Z = (np.abs(X) ** p + np.abs(Y) ** p) ** (1 / p)
    contour = plt.contour(X, Y, Z, levels=10, label=f'L{p} Norm', linewidths=2)
    
    # Add labels to the contours
    plt.clabel(contour, inline=1, fontsize=10, fmt='%1.1f')

# Set aspect ratio to be equal
plt.axis('equal')

# Add legend
plt.legend()

# Set plot title
plt.title('Lp Norms for Different p Values')

# Label axes
plt.xlabel('X')
plt.ylabel('Y')

plt.grid(True)
plt.show()
