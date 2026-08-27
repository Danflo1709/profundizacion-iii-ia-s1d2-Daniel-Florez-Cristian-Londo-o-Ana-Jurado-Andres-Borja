"""Visualización de la trayectoria de la pelota."""

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

from .parameters import (
    TABLE_LENGTH,
    TABLE_WIDTH,
    TABLE_HEIGHT,
)


def plot_trajectory(positions):
    """
    Grafica la trayectoria 3D de la pelota.
    """

    fig = plt.figure(figsize=(10, 6))
    ax = fig.add_subplot(111, projection="3d")

    ax.plot(
        positions[0],
        positions[1],
        positions[2],
        linewidth=2,
        label="Trayectoria",
    )

    # Mesa
    x = [0, TABLE_LENGTH, TABLE_LENGTH, 0, 0]
    y = [0, 0, TABLE_WIDTH, TABLE_WIDTH, 0]
    z = [TABLE_HEIGHT] * 5

    ax.plot(x, y, z, linewidth=2)

    ax.set_xlabel("X (mm)")
    ax.set_ylabel("Y (mm)")
    ax.set_zlabel("Z (mm)")

    ax.set_title("Simulación Tenis de Mesa")
    ax.legend()

    plt.show()