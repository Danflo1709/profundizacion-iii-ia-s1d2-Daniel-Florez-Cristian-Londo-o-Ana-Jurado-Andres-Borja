"""Parámetros de la simulación de tenis de mesa."""

# Propiedades de la pelota
BALL_MASS = 2.7
BALL_RADIUS = 20.25
BALL_ROT_INERTIA = (2 / 3) * BALL_MASS * BALL_RADIUS**2

# Coeficientes de interacción
TABLE_RESTITUTION = 0.77
NET_RESTITUTION = 0.5
TABLE_FRICTION = 0.25

# Resistencia aerodinámica y rotacional
DRAG = 2.7
ROT_DRAG = 350.0
MAGNUS = 0.01

# Dimensiones de la mesa (mm)
TABLE_LENGTH = 2740
TABLE_WIDTH = 1525
TABLE_HEIGHT = 760

# Dimensiones de la red (mm)
NET_HEIGHT = 152.5
NET_EXTRA = 180

# Gravedad (mm/s^2)
GRAVITY = 9800

# Configuración de la simulación
ANIMATE = True
PLOT_PERIOD = 5
YAW = -45
PITCH = 23.5

# Tiempo de simulación
DT = 0.005
SIMULATION_TIME = 1.5
