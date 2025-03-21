# Filtro de Acromatopsia - Conversión a Escala de Grises

## ¿Qué es la Acromatopsia?
La **acromatopsia** es una condición visual en la que las personas no pueden percibir colores y ven el mundo en blanco y negro o escala de grises. Esto se debe a la disfunción o ausencia de los **conos en la retina**, que son responsables de la detección del color. Como resultado, todo se percibe en tonos de blanco, negro y gris. Cabe resaltar el índice de posibilidad de que alguien nazca con esta condición que es de: 1 en cada 30,000 personas que son aproximadamente 270,000 personas en el mundo.

## ¿Cómo funciona el filtro para Acromatopsia?
Este filtro convierte una imagen que nosotros percibimos normal a **blanco y negro** mediante una transformación matemática de los valores de los canales de color RGB (**Rojo, Verde y Azul**) en un solo valor de **intensidad luminosa**.

### Matriz de transformación utilizada:
```python
kernel = np.array([[0.299, 0.587, 0.114],
                  [0.299, 0.587, 0.114],
                  [0.299, 0.587, 0.114]])
```

Esta matriz aplica un **peso diferente** a cada componente de color para reflejar la forma en que el ojo humano percibe la luminosidad de cada color:
- **Rojo (R):** 29.9%
- **Verde (G):** 58.7%
- **Azul (B):** 11.4%

## ¿Cómo se aplica la transformación de color?
Cada píxel en una imagen tiene tres valores: **R (Rojo), G (Verde) y B (Azul)**. Se multiplica cada canal por los coeficientes de la matriz y se combinan los resultados en un único valor, lo que da como resultado la escala de grises.

Ejemplo de transformación:

| **Antes (RGB original)** | **Después (Escala de Grises)** |
|----------------|----------------|
| **(255, 50, 50)**  → Rojo intenso | **(102, 102, 102)** → Gris oscuro |
| **(30, 200, 30)**  → Verde brillante | **(143, 143, 143)** → Gris intermedio |
| **(50, 50, 255)**  → Azul intenso | **(76, 76, 76)** → Gris oscuro |

## ¿Cómo afecta cada color?

| **Color Original** | **Color Transformado** | **Motivo del Cambio** |
|----------------|----------------|----------------|
| **Rojo intenso** | **Gris oscuro** | Tiene menor peso en la luminancia. |
| **Verde brillante** | **Gris intermedio** | Mayor peso en la luminancia. |
| **Azul intenso** | **Gris oscuro** | Menor impacto en la percepción del brillo. |

**El resultado final es una imagen completamente en escala de grises**, simulando la percepción visual de una persona con acromatopsia.

---

## Implementación en Python
El siguiente código carga una imagen, aplica la transformación a escala de grises y muestra el resultado:

## ¿Cómo se usa este filtro en la vida real?
Este filtro tiene diversas aplicaciones en accesibilidad y tecnología:

### 1️⃣ **Simulación para Diseño Inclusivo**
- Permite a los diseñadores y desarrolladores visualizar cómo las personas con acromatopsia perciben las interfaces digitales.
- Ayuda a mejorar el contraste y la legibilidad en interfaces web y gráficos.

### 2️⃣ **Mejora en Análisis de Imágenes**
- Utilizado en visión por computadora para eliminar la influencia del color en el análisis de patrones, pudiendo ver a esta con mas claridad y detalle.
- Facilita la segmentación de objetos en procesamiento de imágenes.

### 3️⃣ **Fotografía y Cine**
- Permite la conversión automática de videos o fotos a blanco y negro de manera realista.
- Usado en cinematografía para crear efectos visuales estilísticos.

### 4️⃣ **Investigación Médica**
- Puede aplicarse en estudios sobre la percepción visual y en tecnologías de asistencia para personas con discapacidades visuales.

## Conclusión
El filtro de acromatopsia es una herramienta útil para **simular, analizar y adaptar contenidos visuales** para personas con esta condición. Su implementación en tecnología y diseño puede mejorar la accesibilidad y la inclusión en diferentes industrias (como la tecnológica).
