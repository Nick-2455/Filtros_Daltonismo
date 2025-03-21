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

## 🔄 Función genérica: `apply_color_filter`

**Uso:** Todas las funciones anteriores utilizan esta función base para aplicar la matriz de conversión de color.

**Funcionamiento:**
1. Convierte la imagen de BGR a RGB.
2. Aplica la transformación matricial con la matriz correspondiente.
3. Ajusta los valores para que estén en el rango [0, 255].

---

## 📈 Aplicaciones Prácticas

- Diseño gráfico accesible
- Desarrollo de interfaces y videojuegos
- Material educativo sobre percepción visual
- Pruebas de usabilidad en plataformas digitales

---

## 🏁 Conclusión

Simular condiciones de daltonismo y acromatopsia es clave para comprender los retos visuales que enfrentan algunas personas. Usar estos filtros ayuda a crear contenido visual inclusivo, promoviendo la accesibilidad y el diseño universal.

