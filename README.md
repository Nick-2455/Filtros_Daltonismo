# Filtro de Protanopia - Adaptación de Colores para Daltonismo

## ¿Qué es la Protanopia?
La **Protanopia** es un tipo de daltonismo en el que las personas tienen dificultad para distinguir entre los colores **rojo y verde**. Esto ocurre debido a la ausencia o mal funcionamiento de los **conos de detección del rojo** en la retina del ojo humano. Como resultado, los tonos rojizos y verdosos pueden parecerse a tonos amarillosos.

## ¿Cómo funciona el filtro para Protanopia?
Este filtro aplica una transformación matemática a la imagen para **modificar los colores y hacerlos más distinguibles** para las personas con protanopia. Se basa en una **matriz de corrección** que ajusta la forma en que los canales de color (Rojo, Verde y Azul) se combinan en la imagen.

### Matriz de transformación utilizada:
```python
    protanopia_kernel = np.array([
        [0.152, 1.053, -0.205],
        [0.115, 0.786, 0.099],
        [0.000, 0.000, 1.000]
    ])
```

Esta matriz cambia la forma en que cada píxel de la imagen **mezcla sus componentes de color**. Se aplican cálculos a cada canal **Rojo (R), Verde (G) y Azul (B)** para generar una nueva imagen corregida.


## ** ¿Cómo se aplica la transformación de color?**
Cada píxel de la imagen tiene tres valores: **R (Rojo), G (Verde) y B (Azul)**.  
Para modificarlo, hacemos una multiplicación **matricial** entre los valores de color del píxel y la matriz de transformación.

Ejemplo de transformación:

| **Antes (RGB original)** | **Después (RGB corregido)** |
|----------------|----------------|
| **(255, 50, 50)**  → Rojo intenso | **(166, 164, 50)** → Rojo más equilibrado |
| **(30, 200, 30)**  → Verde brillante | **(103, 105, 71)** → Más diferenciado del rojo |



## ** ¿Cómo afecta cada color?**

| **Color Original** | **Color Transformado** | **Motivo del Cambio** |
|----------------|----------------|----------------|
| **Rojo intenso** | **Ausencia de rojo** | Los personas que sufren protanopia no pueden percibir el rojo. |
| **Verde brillante** | **Toma tonos de amarillo** | Los personas que sufren protanopia no pueden percibir el verde. |
| **Azul** | **Casi sin cambios** | No está afectado por la protanopia. |

**El resultado final es una imagen en la que los amarillo y azul tienen más contraste entre sí**, haciendo que sean más fáciles de diferenciar.

---

## Implementación en Python
El siguiente código carga una imagen, aplica la transformación de colores y muestra el resultado comparado con la imagen original:

## ¿Cómo se usa este filtro en la vida real?
Este filtro es útil en diferentes aplicaciones para mejorar la accesibilidad de personas con daltonismo:

### 1️⃣ **Diseño de Interfaces y Aplicaciones**
- Mejora la visibilidad de colores en **software, aplicaciones y videojuegos**.
- Ayuda a los diseñadores a crear interfaces más accesibles.

### 2️⃣ **Señalización y Mapas**
- Puede aplicarse en **mapas de transporte público** para hacer más distinguibles las rutas de trenes o autobuses.
- En **señalización vial**, para que los semáforos y carteles sean más fáciles de interpretar para daltónicos.

### 3️⃣ **Análisis de Imágenes Médicas**
- En medicina, puede ser útil para permitir que médicos con daltonismo interpreten mejor ciertas imágenes médicas.

### 4️⃣ **E-Commerce y Catálogos Digitales**
- Mejora la experiencia de compra en línea al ajustar los colores de productos para clientes con daltonismo.

## Conclusión
Este filtro es una herramienta poderosa para mejorar la accesibilidad visual en diversas industrias. Implementarlo en sistemas de visión por computadora y diseño de interfaces puede **hacer que la información sea más inclusiva para personas con protanopia**.

