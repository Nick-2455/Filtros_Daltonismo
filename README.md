# Documentación de Filtros de Daltonismo

Este documento describe el funcionamiento y objetivo de los diferentes filtros aplicados para simular tipos de daltonismo y acromatopsia en una imagen. Estos filtros permiten visualizar cómo las personas con estas condiciones visuales perciben los colores.

---

## 🌐 Propósito General

El objetivo de aplicar estos filtros es generar conciencia sobre la percepción del color en personas con diferentes tipos de daltonismo, y facilitar el diseño de contenido visual más accesible e inclusivo.

---

## 🔹 Filtro de Deuteranopía

**Nombre:** `apply_deuteranopia_filter`

**Tipo de daltonismo:** Rojo-verde

**Descripción:** Simula la percepción de una persona con deuteranopía, una condición en la que los conos responsables de captar el color verde (conos M) no funcionan correctamente o están ausentes.

**Matriz de transformación:**
```
[[0.43, 0.72, -0.15],
 [0.34, 0.57, 0.09],
 [-0.02, 0.03, 1.00]]
```

**Efecto:** Los tonos verdes y rojos se perciben de forma similar, dificultando su distinción.

---

## 🔹 Filtro de Protanopía

**Nombre:** `apply_protanopia_filter`

**Tipo de daltonismo:** Rojo-verde

**Descripción:** Simula la condición en la que los conos sensibles al rojo (conos L) están ausentes o no funcionan bien.

**Matriz de transformación:**
```
[[0.152, 1.053, -0.205],
 [0.115, 0.786, 0.099],
 [0.000, 0.000, 1.000]]
```

**Efecto:** El rojo pierde intensidad, se vuelve más apagado o incluso oscuro, y se confunde con verdes o marrones.

---

## 🔹 Filtro de Tritanopía

**Nombre:** `apply_tritanopia_filter`

**Tipo de daltonismo:** Azul-amarillo

**Descripción:** Simula la tritanopía, condición donde los conos sensibles al azul (conos S) no están presentes o no funcionan correctamente.

**Matriz de transformación:**
```
[[1.0, 0.0, 0.0],
 [0.0, 1.0, 0.0],
 [-0.395, 0.801, 0.0]]
```

**Efecto:** Las personas con tritanopía tienen dificultad para distinguir entre tonos azules y verdes, o entre amarillos y violetas.

---

## 🔹 Filtro de Acromatopsia

**Nombre:** `apply_acromatopsia_filter`

**Tipo de deficiencia visual:** Pérdida total de percepción del color

**Descripción:** Simula la acromatopsia, una condición muy rara en la que las personas ven exclusivamente en escala de grises debido a la ausencia de conos funcionales.

**Matriz de transformación:**
```
[[0.299, 0.587, 0.114],
 [0.299, 0.587, 0.114],
 [0.299, 0.587, 0.114]]
```

**Efecto:** La imagen se convierte a escala de grises, eliminando por completo cualquier información de color.

---

### **Manual de usuario**

#### **1. Descripción del programa**

Este programa está diseñado para diferenciar los distintos tipos de daltonismo, esto mediante el utilizamiento de las biblotecas de OpenCV, Numpy y Matplotlib. Los filtros van desde simular la forma en la que ve el Deuteranopia, Protanopia, Tritanopia y Acromatopsia.

#### **2. Lenguaje de programación utilizado**

Este programa está desarrollado en el lenguaje de **Python**.

#### **3. Requisitos previos**

Antes de ejecutar el programa, debe tener instalada la versión de Python 3 en su sistema. Puede descargar e instalar Python desde el siguiente enlace oficial:  
[Python Oficial](https://www.python.org/downloads/)

Para lograr ejecutar el codigo el usuario debe tener instaladas las biblotecas de OpenCV, Numpy y Matplotlib.

Esto se logra abrien un panel de ternimal y ejecutando los siguientes comandos, en caso de que ya tenga las librerias instaladas en su python omita este paso.

OpenCV
```bash
pip install opencv-python
```

Numpy
```bash
pip install numpy
```

Matplotlib
```bash
pip install matplotlib
```

una vez instalas la librerias, el codigo no deberia de dar un problema con ellas.

#### **4. Archivos necesarios**

- **Archivo de código fuente:** `main.py` (Este es el archivo que contiene el programa en Python).
- **Archivo de entrada:** El usuario debe de la carpeta `images` donde se encuentra el archivo de  `image6.jpg.webp`, este sera la imagen a la que se le aplicaran los distintos filtros para simular los diferentes tipos de daltonismo.

#### **5. Cómo ejecutar el programa**

Para ejecutar el programa, siga estos pasos:

1. Asegúrese de tener el archivo `image6.jpg.webp` en la carpeta de `images` debido a que el programa los buscara de esta forma.
2. Asegúrese de que la carpeta `images` este dentro de la carpeta donde se encuetra el archivo `main.py`.
3. Abra una terminal o línea de comandos en la carpeta donde esta el `main.py`.
4. Ejecute el siguiente comando para correr el programa:

```bash
python main.py
```

#### **6. Qué esperar como salida**

Cuando ejecute el programa, el script leerá el archivo `image6.jpg.webp`, y le aplicara los diferentes kernels, los cuales emulan los diferentes tipos de daltonismo.

**Deuteranopia**: Dificultad para distinguir el color verde.

**Protanopia**: Dificultad para distinguir el color rojo.

**Tritanopia**: Dificultad para distinguir el color azul.

**Acromatopsia**: Conversión de la imagen a escala de grises.

##### Ejemplo de salida:
![HCAP](https://github.com/user-attachments/assets/07111e9d-aa56-4c24-a78d-0d264861fa46)

---

## 📈 Aplicaciones Prácticas

- Diseño gráfico accesible
- Desarrollo de interfaces y videojuegos
- Material educativo sobre percepción visual
- Pruebas de usabilidad en plataformas digitales

---

## 🏁 Conclusión

Este programa es una herramienta la cual permite que podamos experimentar los diferentes puntos de vistas, que tiene las personas con algun de los daltonismos anteriormente señalas. Lo que puede ser empleado con fines educativos, como para el desarrollo de interfaces accesibles. Una de las cosas que tiene el programa es que su estructura es modular lo que permite que este en un futuro pueda añadir mas filtro o hacerle mantenimiento al codigo.

## Referencias

- Color Universal Design (CUD) / Colorblind Barrier free. (n.d.). https://jfly.uni-koeln.de/color/#pallet
- Gisadminbeers. (2019, June 30). Mapas de diseño para daltónicos - Gis&Beers. Gis&Beers. https://www.gisandbeers.com/mapas-de-diseno-para-daltonicos/
- Machado, G. M. (n.d.). A physiologically-based model for simulation of color vision deficiency. https://www.inf.ufrgs.br/~oliveira/pubs_files/CVD_Simulation/CVD_Simulation.html
