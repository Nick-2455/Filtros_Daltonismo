# Documentación del Proyecto: Convolución en Imágenes

## Introducción
La convolución es una operación matemática fundamental en el procesamiento de imágenes y visión por computadora. Se utiliza para aplicar filtros que pueden mejorar, suavizar o detectar características en una imagen. Este proyecto implementa tres filtros de convolución sobre una imagen de entrada:

- **Filtro Laplaciano**: Detecta bordes resaltando los cambios bruscos de intensidad.
- **Filtro Gaussiano**: Suaviza la imagen para reducir ruido y mejorar la calidad visual.
- **Filtro High Boost**: Resalta los detalles para mejorar el contraste y la nitidez.

Este documento describe cómo funciona la convolución, su implementación en Python y cómo usar este código para procesar imágenes.

---

## Conceptos Clave

### ¿Qué es la Convolución?
La convolución en procesamiento de imágenes es una operación que consiste en aplicar un **kernel** (o filtro) sobre una imagen para modificar sus características. Se realiza multiplicando cada píxel por los valores del kernel y sumando los resultados para producir una nueva imagen transformada.

### ¿Qué es un Kernel?
Un kernel es una matriz de valores numéricos que define la transformación que se aplicará a la imagen. Algunos ejemplos incluyen:

- **Bordes** (Laplaciano): `[[0, -1, 0], [-1, 4, -1], [0, -1, 0]]`
- **Suavizado** (Gaussiano): `[[1, 4, 6, 4, 1], [4, 16, 24, 16, 4], [6, 24, 36, 24, 6], [4, 16, 24, 16, 4], [1, 4, 6, 4, 1]] / 256`
- **Realce de Detalles** (High Boost): `[[-1, -1, -1], [-1, 10, -1], [-1, -1, -1]]`

Cada uno de estos filtros afecta la imagen de una manera diferente.

---

## Implementación en Python
El código implementa una función para aplicar convolución a imágenes utilizando OpenCV (`cv2`) y NumPy. Se siguen los siguientes pasos:

1. **Cargar la imagen**: Se lee la imagen de entrada desde `images/image.jpg`.
2. **Convertir a escala de grises**: Para aplicar los filtros de convolución.
3. **Aplicar los filtros**: Se usa una función personalizada para realizar la convolución con los kernels definidos.
4. **Visualizar los resultados**: Se combinan las imágenes en una sola ventana para comparar los efectos de cada filtro, con etiquetas en color rojo.

---

## Instrucciones de Uso
### **Requisitos Previos**
Asegúrate de tener instaladas las siguientes bibliotecas en Python:
```bash
pip install opencv-python numpy
```
### **Ejecución del Código**
1. Coloca la imagen que deseas procesar en la carpeta `images/` con el nombre `image.jpg`.
2. Ejecuta el script con:
```bash
python main.py
```
3. Se abrirá una ventana mostrando la imagen original y los efectos de cada filtro en una sola vista con títulos en color rojo.

---

## Resultados Esperados
Después de ejecutar el código, verás una ventana con las siguientes imágenes combinadas en una sola:
1. **Imagen Original**: La imagen sin modificaciones.
2. **Filtro Laplaciano**: Imagen con bordes resaltados.
3. **Filtro Gaussiano**: Imagen suavizada.
4. **Filtro High Boost**: Imagen con detalles realzados.

Cada imagen tendrá su título en **color rojo** para indicar el filtro aplicado.

---

## Conclusión
Este proyecto muestra cómo la convolución se puede usar para transformar imágenes de manera efectiva. Dependiendo del caso de uso, diferentes filtros pueden mejorar la calidad de la imagen, detectar bordes o resaltar detalles importantes. Además, la integración de los resultados en una sola ventana facilita la comparación entre los distintos efectos aplicados.

Si deseas modificar la implementación, puedes experimentar con diferentes **kernels** y ajustar sus valores para obtener efectos personalizados en las imágenes.
