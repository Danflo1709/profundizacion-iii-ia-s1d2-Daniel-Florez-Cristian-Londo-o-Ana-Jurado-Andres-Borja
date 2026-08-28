"""Funciones de visualización para la simulación de tenis de mesa."""

import numpy as np
import matplotlib.pyplot as plt

from .parameters import (
    TABLE_LENGTH,
    TABLE_WIDTH,
    TABLE_HEIGHT,
)


def plot_trajectory(positions):
    """Muestra la trayectoria 3D de la pelota y la mesa."""
    positions = np.asarray(positions)

    if positions.shape[0] != 3:
        raise ValueError("positions debe tener forma (3, n).")

    figure = plt.figure(figsize=(10, 6))
    axis = figure.add_subplot(111, projection="3d")

    axis.plot(
        positions[0],
        positions[1],
        positions[2],
        linewidth=2,
        label="Trayectoria de la pelota",
    )

    # Mesa
    x = [0, TABLE_LENGTH, TABLE_LENGTH, 0, 0]
    y = [0, 0, TABLE_WIDTH, TABLE_WIDTH, 0]
    z = [TABLE_HEIGHT] * 5

    axis.plot(x, y, z, linewidth=2, label="Mesa")

    axis.set_xlabel("X [mm]")
    axis.set_ylabel("Y [mm]")
    axis.set_zlabel("Z [mm]")
    axis.set_title("Trayectoria 3D de la pelota")
    axis.legend()

    return figure


def plot_position(t, positions):
    """Muestra la posición de la pelota en función del tiempo."""
    t = np.asarray(t)
    positions = np.asarray(positions)

    if positions.shape[0] != 3:
        raise ValueError("positions debe tener forma (3, n).")

    figure, axis = plt.subplots()

    axis.plot(t, positions[0], label="X")
    axis.plot(t, positions[1], label="Y")
    axis.plot(t, positions[2], label="Z")

    axis.set_xlabel("Tiempo [s]")
    axis.set_ylabel("Posición [mm]")
    axis.set_title("Posición de la pelota")
    axis.legend()
    axis.grid(True)

    return figure


def plot_velocity(t, velocities):
    """Muestra la velocidad de la pelota en función del tiempo."""
    t = np.asarray(t)
    velocities = np.asarray(velocities)

    if velocities.shape[0] != 3:
        raise ValueError("velocities debe tener forma (3, n).")

    figure, axis = plt.subplots()

    axis.plot(t, velocities[0], label="Vx")
    axis.plot(t, velocities[1], label="Vy")
    axis.plot(t, velocities[2], label="Vz")

    axis.set_xlabel("Tiempo [s]")
    axis.set_ylabel("Velocidad [mm/s]")
    axis.set_title("Velocidad de la pelota")
    axis.legend()
    axis.grid(True)

    return figure