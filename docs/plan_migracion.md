# Plan de migración MATLAB → Python

## Proyecto

Simulación de la trayectoria de una pelota de tenis de mesa considerando efectos físicos como gravedad, arrastre aerodinámico, efecto Magnus y rebotes.

## Objetivo

Migrar el modelo original desarrollado en MATLAB (`legacy/TableTennisTests.mlx`) a una implementación modular en Python, manteniendo el comportamiento general de la simulación y mejorando la organización del código.

## Estrategia de migración

### 1. Preservar el código original

El archivo MATLAB original se conserva en:

```text
legacy/TableTennisTests.mlx
```

como referencia para validar la migración.

### 2. Identificación de componentes

Se identifican los siguientes elementos principales:

- Parámetros físicos.
- Modelo dinámico de la pelota.
- Integración temporal.
- Detección y manejo de rebotes.
- Visualización de resultados.

### 3. Modularización en Python

La implementación se divide en los siguientes módulos:

```text
src/table_tennis_sim/
├── parameters.py
├── physics.py
├── simulation.py
└── visualization.py
```

### 4. Validación

La simulación se ejecuta con condiciones iniciales equivalentes a las utilizadas en MATLAB para verificar que la trayectoria obtenida sea consistente.

### 5. Visualización

Se generan gráficos tridimensionales utilizando Matplotlib para inspeccionar la trayectoria de la pelota.

### 6. Notebook interactivo

Se desarrolla un notebook interactivo para ejecutar simulaciones y modificar parámetros de entrada de manera sencilla.

## Resultado esperado

Obtener una simulación funcional en Python que reproduzca el comportamiento general del modelo MATLAB y facilite futuras extensiones del proyecto.