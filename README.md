# Filtro de Deuteranopía - Adaptación de Colores para Daltonismo

## ¿Qué es la Deuteranopía?
La **deuteranopía** es un tipo de daltonismo en el que las personas tienen dificultad para distinguir entre los colores **rojo y verde**. Esto ocurre debido a la ausencia o mal funcionamiento de los **conos de detección del verde** en la retina del ojo humano. Como resultado, los tonos rojizos y verdosos pueden parecer similares o incluso indistinguibles.

## ¿Cómo funciona el filtro para Deuteranopía?
Este filtro aplica una transformación matemática a la imagen para **modificar los colores y hacerlos más distinguibles** para las personas con deuteranopía. Se basa en una **matriz de corrección** que ajusta la forma en que los canales de color (Rojo, Verde y Azul) se combinan en la imagen.

### Matriz de transformación utilizada:
```python
colorblind_matrix = np.array([[0.43, 0.72, -0.15],
                               [0.34, 0.57, 0.09],
                               [-0.02, 0.03, 1.00]])
```
### Explicación de la matriz:
- **Canal Rojo (R) →** Se reduce su intensidad y se mezcla con el verde.
- **Canal Verde (G) →** Se ajusta para equilibrar mejor con los otros colores.
- **Canal Azul (B) →** Se mantiene prácticamente igual, ya que no es afectado por la deuteranopía.

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
Este filtro es una herramienta poderosa para mejorar la accesibilidad visual en diversas industrias. Implementarlo en sistemas de visión por computadora y diseño de interfaces puede **hacer que la información sea más inclusiva para personas con deuteranopía**.

