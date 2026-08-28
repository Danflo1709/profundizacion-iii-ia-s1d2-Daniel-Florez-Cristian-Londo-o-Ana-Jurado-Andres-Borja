"""Motor de simulación de tenis de mesa."""

import numpy as np

from .parameters import DT, SIMULATION_TIME
from .physics import (
    compute_acceleration,
    compute_angular_acceleration,
    handle_table_bounce,
)


def simulate(
    position,
    velocity,
    omega,
    dt=DT,
    simulation_time=SIMULATION_TIME,
):
    """Simula el movimiento de la pelota."""

    t = np.arange(0.0, simulation_time + dt, dt)
    n = len(t)

    positions = np.zeros((3, n))
    velocities = np.zeros((3, n))
    accelerations = np.zeros((3, n))
    omegas = np.zeros((3, n))
    alphas = np.zeros((3, n))

    positions[:, 0] = position
    velocities[:, 0] = velocity
    omegas[:, 0] = omega

    for k in range(1, n):
        accelerations[:, k - 1] = compute_acceleration(
            velocities[:, k - 1],
            omegas[:, k - 1],
        )

        alphas[:, k - 1] = compute_angular_acceleration(
            omegas[:, k - 1]
        )

        velocities[:, k] = (
            velocities[:, k - 1]
            + accelerations[:, k - 1] * dt
        )

        positions[:, k] = (
            positions[:, k - 1]
            + velocities[:, k] * dt
        )

        omegas[:, k] = (
            omegas[:, k - 1]
            + alphas[:, k - 1] * dt
        )

        positions[:, k], velocities[:, k], omegas[:, k] = (
            handle_table_bounce(
                positions[:, k],
                velocities[:, k],
                omegas[:, k],
            )
        )

    accelerations[:, -1] = compute_acceleration(
        velocities[:, -1],
        omegas[:, -1],
    )

    alphas[:, -1] = compute_angular_acceleration(
        omegas[:, -1]
    )

    return (
        t,
        positions,
        velocities,
        accelerations,
        omegas,
        alphas,
    )
