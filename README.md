# Simulación de Tenis de Mesa

Proyecto de migración de un modelo de simulación de tenis de mesa desde MATLAB hacia Python.

## Objetivo

Implementar una simulación física de la trayectoria de una pelota de tenis de mesa considerando:

- Gravedad
- Resistencia aerodinámica
- Efecto Magnus
- Rebote sobre la mesa
- Visualización tridimensional

## Estructura del proyecto

```text
.
├── docs/
├── legacy/
├── notebooks/
├── results/
└── src/
    └── table_tennis_sim/
        ├── parameters.py
        ├── physics.py
        ├── simulation.py
        └── visualization.py
```

## Requisitos

Instalar dependencias:

```bash
pip install numpy matplotlib
```

## Ejecución rápida

Ejemplo de uso:

```python
import numpy as np

from table_tennis_sim.simulation import simulate

p0 = np.array([0.0, 762.5, 1065.0])

v0 = np.array([
    7000.0,
    -3000.0,
    -3000.0
])

w0 = np.array([
    0.0,
    0.0,
    75.0 * 2 * np.pi
])

t, pos, vel, acc, omega, alpha = simulate(
    p0,
    v0,
    w0
)
```

## Notebook interactivo

El proyecto incluye:

```text
notebooks/01_simulacion_interactiva.ipynb
```

donde se pueden ejecutar simulaciones y visualizar trayectorias.

## Integrantes

- Daniel Flórez
- Cristian Londoño
- Ana Jurado
- Andrés Borja

## Referencia

Migración realizada a partir del archivo MATLAB:

```text
legacy/TableTennisTests.mlx
```