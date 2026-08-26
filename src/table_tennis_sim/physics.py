"""Funciones fisicas de la simulacion de tenis de mesa."""

import numpy as np

from .parameters import (
    BALL_MASS,
    BALL_RADIUS,
    BALL_ROT_INERTIA,
    DRAG,
    GRAVITY,
    MAGNUS,
    ROT_DRAG,
    TABLE_FRICTION,
    TABLE_HEIGHT,
    TABLE_LENGTH,
    TABLE_RESTITUTION,
    TABLE_WIDTH,
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


def handle_table_bounce(position, velocity, omega):
    """Maneja el rebote de la pelota sobre la superficie de la mesa.

    La pelota rebota unicamente cuando:
    - esta dentro de los limites de la mesa;
    - ha alcanzado la altura de la superficie;
    - esta descendiendo.

    Si la pelota sale por los bordes de la mesa, continua su trayectoria
    y no se produce ningun rebote.
    """
    inside_table = (
        0.0 <= position[0] <= TABLE_LENGTH
        and 0.0 <= position[1] <= TABLE_WIDTH
    )

    table_surface = TABLE_HEIGHT + BALL_RADIUS
    touching_table = position[2] <= table_surface

    descending = velocity[2] < 0.0

    if not (inside_table and touching_table and descending):
        return position, velocity, omega

    position = position.copy()
    velocity = velocity.copy()
    omega = omega.copy()

    # Coloca el centro de la pelota exactamente sobre la superficie.
    position[2] = table_surface

    # Velocidad de la superficie de la pelota debida a la rotacion.
    contact_velocity = np.cross(
        omega,
        np.array([0.0, 0.0, BALL_RADIUS]),
    )

    # Diferencia entre la velocidad de contacto y la velocidad lineal.
    delta_velocity = (
        contact_velocity
        - np.array([velocity[0], velocity[1], 0.0])
    )

    # Friccion durante el contacto con la mesa.
    velocity += TABLE_FRICTION * delta_velocity

    # Transferencia de velocidad lineal a velocidad angular.
    omega += (
        TABLE_FRICTION
        * np.cross(
            delta_velocity,
            np.array([0.0, 0.0, 1.0]),
        )
        / BALL_RADIUS
    )

    # Rebote vertical usando el coeficiente de restitucion.
    velocity[2] = -TABLE_RESTITUTION * velocity[2]

    return position, velocity, omega