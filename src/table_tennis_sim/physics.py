"""Funciones fisicas de la simulacion de tenis de mesa."""

import numpy as np

from .parameters import (
    BALL_MASS,
    BALL_ROT_INERTIA,
    DRAG,
    GRAVITY,
    MAGNUS,
    ROT_DRAG,
)


def compute_force(velocity, omega):
    """Calcula la fuerza neta sobre la pelota."""
    gravity_force = BALL_MASS * np.array([0.0, 0.0, -GRAVITY])
    drag_force = -DRAG * velocity
    magnus_force = MAGNUS * np.cross(omega, velocity)

    return gravity_force + drag_force + magnus_force


def compute_acceleration(velocity, omega):
    """Calcula la aceleracion lineal de la pelota."""
    return compute_force(velocity, omega) / BALL_MASS


def compute_torque(omega):
    """Calcula el torque producido por la resistencia rotacional."""
    return -ROT_DRAG * omega


def compute_angular_acceleration(omega):
    """Calcula la aceleracion angular de la pelota."""
    return compute_torque(omega) / BALL_ROT_INERTIA
