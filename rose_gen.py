import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Parameters
n = 800
A = 1.995653
B = 1.27689
C = 8

# Generate r and theta values
r = np.linspace(0, 1, n)
theta = np.linspace(-2, 20 * np.pi, n)
R, THETA = np.meshgrid(r, theta)

# Define the number of petals per cycle
petalNum = 3.6
x = 1 - (1/2) * ((5/4) * (1 - np.mod(petalNum * THETA, 2 * np.pi) / np.pi)**2 - 1/4)**2
phi = (np.pi / 2) * np.exp(-THETA / (C * np.pi))
y = A * (R**2) * (B * R - 1)**2 * np.sin(phi)

R2 = x * (R * np.sin(phi) + y * np.cos(phi))
X = R2 * np.sin(THETA)
Y = R2 * np.cos(THETA)
Z = x * (R * np.cos(phi) - y * np.sin(phi))

# Define a red colormap
red_map = np.zeros((10, 3))
red_map[:, 0] = np.linspace(1, 0.25, 10)  # Red channel

# Plot the surface
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection='3d')

# Normalize Z values and apply colormap
norm = plt.Normalize(Z.min(), Z.max())
colors = plt.cm.Reds(norm(Z))
ax.plot_surface(X, Y, Z, facecolors=colors, edgecolor='none')
ax.view_init(elev=42, azim=-40.5)

# Remove axes
ax.set_xticks([])
ax.set_yticks([])
ax.set_zticks([])
ax.set_box_aspect([1,1,1])  # Maintain aspect ratio
# Hide X-axis line
ax.xaxis.line.set_color((1, 1, 1, 0))  
# Hide Y-axis line
ax.yaxis.line.set_color((1, 1, 1, 0))  
# Hide Z-axis line
ax.zaxis.line.set_color((1, 1, 1, 0)) 
ax.set_xlabel('')
ax.set_ylabel('')
ax.set_zlabel('')
ax.grid(False)  # Remove grid

# # Remove pane and spines (box) for 3D plot
# # For 3D plots, use '_axis3don' to control pane visibility
# ax.xaxis._axis3don = False
# ax.yaxis._axis3don = False
# ax.zaxis._axis3don = False

# # Remove spines (if needed, though they should already be hidden)
# # ax.xaxis.line.set_visible(False)
# # ax.yaxis.line.set_visible(False)
# # ax.zaxis.line.set_visible(False)

# Hide the bounding box
# ax.set_frame_on(False)
ax.xaxis.pane.set_visible(False)
ax.yaxis.pane.set_visible(False)
ax.zaxis.pane.set_visible(False)


plt.show()